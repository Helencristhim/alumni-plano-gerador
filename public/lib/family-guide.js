/**
 * FAMILY GUIDE — Alumni by Better
 * Injeta a tab "Family Guide" nos hubs professor/aluno.
 *
 * POR QUE ISTO EXISTE
 * -------------------
 * O Perfil 360 do Gabriel Fernandes fecha o campo 14 (avaliacao e criterios) com
 * "family guide por aula". O material foi entregue sem ele: as cinco aulas subiram,
 * a familia nao tinha por onde acompanhar, e a Helen cobrou (04/09/2026). Esta tab
 * e a entrega desse combinado.
 *
 * POR QUE UMA LIB E NAO UM BLOCO NO HTML
 * --------------------------------------
 * Mesmo caminho da tab irma "Resumos das Aulas" (`resumos-aula.js`), e pelo mesmo
 * motivo escrito la: os hubs ja publicados carregam `/lib/controle-aulas.js`, entao
 * uma tab nova chega a todos SEM editar HTML de aluno nenhum (REGRA 30 — o legado e
 * intocavel). Alem disso a tab sobrevive a `insert_hub.py`: o hub e reescrito a cada
 * aula nova, e um bloco cravado no HTML se perderia no proximo build.
 *
 * INERTE PARA QUEM NAO TEM CONTEUDO
 * ---------------------------------
 * O conteudo vem de `/data/family-guide/{slug}.json`. Aluno sem arquivo recebe 404,
 * a funcao retorna e NENHUMA tab e injetada — nem um pixel muda nos outros 152 hubs.
 * E por isso que este arquivo pode ser carregado por todo mundo sem risco.
 *
 * O CONTEUDO E EM PORTUGUES, DE PROPOSITO
 * ---------------------------------------
 * A REGRA 13 (zero portugues) vale para a tela de APRENDIZAGEM — o IN CLASS e os
 * exercicios. Esta tab nao e material do aluno: e recado para a mae, que nao fala
 * ingles. O portugues aqui e o idioma do destinatario, nao um vazamento.
 *
 * NAO ENTRA AQUI: DIAGNOSTICO
 * ---------------------------
 * O laudo do aluno tem hipotese diagnostica que a mae trouxe pela metade na
 * consultoria, e o Perfil 360 deixa em aberto se ela quer isso no family guide. Ate
 * ela decidir, a orientacao aparece SO como comportamento ("nao cobre rapidez"),
 * nunca como diagnostico. Se a decisao mudar, muda-se o JSON, nao este arquivo.
 *
 * Requisitos no HTML hospedeiro (ja satisfeitos por controle-aulas.js, que carrega este):
 *   - window.STUDENT_SLUG definido
 *   - switchTab() existente
 *   - um container .tabs e pelo menos um .tab-content
 */
(function() {
  'use strict';

  if (window.__FAMILY_GUIDE_LOADED) return;
  window.__FAMILY_GUIDE_LOADED = true;

  var slug = window.STUDENT_SLUG;
  if (!slug) return;

  var tabsContainer = document.querySelector('.tabs');
  if (!tabsContainer) return;

  var allTabContents = document.querySelectorAll('.tab-content');
  if (!allTabContents.length) return;

  // Busca ANTES de injetar: sem conteudo, nenhuma tab aparece.
  fetch('/data/family-guide/' + encodeURIComponent(slug) + '.json', { cache: 'no-cache' })
    .then(function(r) { return r.ok ? r.json() : null; })
    .then(function(data) { if (data) inject(data); })
    .catch(function() { /* sem family guide para este aluno — silencio proposital */ });

  function inject(data) {
    injectStyles();

    var tabBtn = document.createElement('button');
    tabBtn.className = 'tab-btn';
    tabBtn.setAttribute('onclick', "switchTab('family')");
    tabBtn.textContent = data.titulo || 'Family Guide';
    tabsContainer.appendChild(tabBtn);

    var tabContent = document.createElement('div');
    tabContent.className = 'tab-content';
    tabContent.id = 'tab-family';
    var last = allTabContents[allTabContents.length - 1];
    if (last && last.parentNode) {
      last.parentNode.insertBefore(tabContent, last.nextSibling);
    } else {
      return;
    }

    tabContent.innerHTML = render(data);
  }

  function render(d) {
    var html = '<div class="fg-head">' +
      '<div class="fg-title">' + escHTML(d.titulo || 'Family Guide') + '</div>' +
      (d.subtitulo ? '<div class="fg-sub">' + escHTML(d.subtitulo) + '</div>' : '') +
      '</div>';

    if (d.sempre && d.sempre.itens && d.sempre.itens.length) {
      html += '<div class="fg-card fg-always">' +
        '<h4 class="fg-always-title">' + escHTML(d.sempre.titulo || 'Sempre') + '</h4>' +
        '<ol class="fg-always-list">' +
        d.sempre.itens.map(function(i) {
          return '<li><strong>' + escHTML(i.t) + '.</strong> ' + escHTML(i.d) + '</li>';
        }).join('') +
        '</ol></div>';
    }

    if (d.tarefa_regra) {
      html += '<p class="fg-rule">' + escHTML(d.tarefa_regra) + '</p>';
    }

    (d.aulas || []).forEach(function(a, idx) {
      html += '<details class="fg-lesson"' + (idx === 0 ? ' open' : '') + '>' +
        '<summary class="fg-summary">' +
          '<span class="fg-num">' + escHTML(pad(a.n)) + '</span>' +
          '<span class="fg-lesson-title">' + escHTML(a.titulo || '') + '</span>' +
          '<span class="fg-chev" aria-hidden="true">&#9662;</span>' +
        '</summary>' +
        '<div class="fg-body">' +
          row('O que ele estudou', escHTML(a.tema)) +
          row('O inglês da aula', a.ingles || '') +
          row('O que ele já consegue fazer', escHTML(a.conquista)) +
          row('Tarefa de casa', escHTML(a.tarefa)) +
          (a.jantar ? '<div class="fg-dinner">' +
            '<div class="fg-dinner-label">Para perguntar no jantar</div>' +
            '<div class="fg-dinner-en">&ldquo;' + escHTML(a.jantar.en) + '&rdquo;</div>' +
            '<div class="fg-dinner-pt">' + escHTML(a.jantar.pt) + '</div>' +
          '</div>' : '') +
          (a.repare ? '<div class="fg-note"><strong>Repare:</strong> ' + escHTML(a.repare) + '</div>' : '') +
        '</div>' +
      '</details>';
    });

    if (d.fecho) html += '<p class="fg-close">' + escHTML(d.fecho) + '</p>';
    return html;
  }

  // `valor` ja vem escapado pelo chamador, ou e HTML editorial confiavel do JSON
  // (so o campo `ingles`, que usa <em> para marcar exemplo em ingles).
  function row(rotulo, valor) {
    if (!valor) return '';
    return '<div class="fg-row"><div class="fg-label">' + escHTML(rotulo) + '</div>' +
           '<div class="fg-value">' + valor + '</div></div>';
  }

  function pad(n) { return (n < 10 ? '0' : '') + n; }

  function injectStyles() {
    var style = document.createElement('style');
    style.textContent = [
      // Pega o acento do aluno quando existir; o navy do sistema e so o fallback.
      '#tab-family { --fg-accent: var(--accent, #003080); }',
      '.fg-head { margin-bottom: 1.4rem; }',
      '.fg-title { font:600 1.4rem/1.3 "Cormorant Garamond",Georgia,serif;color:#1a1a2e; }',
      '.fg-sub { font:400 .88rem/1.55 "Inter",sans-serif;color:#777;max-width:62ch;margin-top:.25rem; }',
      '.fg-card { background:#fff;border:1px solid #d4d4cc;border-radius:12px;padding:1.2rem 1.4rem;box-shadow:0 2px 8px rgba(0,0,0,.04); }',
      '.fg-always { border-left:4px solid var(--fg-accent);margin-bottom:1.1rem; }',
      '.fg-always-title { font:600 .95rem/1.4 "Inter",sans-serif;color:#1a1a2e;margin-bottom:.7rem; }',
      '.fg-always-list { margin:0;padding-left:1.1rem;display:flex;flex-direction:column;gap:.6rem; }',
      '.fg-always-list li { font:400 .88rem/1.6 "Inter",sans-serif;color:#4a4a5a; }',
      '.fg-always-list strong { color:#1a1a2e; }',
      '.fg-rule { font:400 .85rem/1.6 "Inter",sans-serif;color:#5c5c6c;border-left:2px solid #d4d4cc;padding-left:1rem;margin:0 0 1.4rem;max-width:66ch; }',
      '.fg-lesson { background:#fff;border:1px solid #d4d4cc;border-radius:12px;margin-bottom:.7rem;overflow:hidden; }',
      '.fg-summary { display:flex;align-items:center;gap:.9rem;padding:.95rem 1.2rem;cursor:pointer;list-style:none;min-height:44px; }',
      '.fg-summary::-webkit-details-marker { display:none; }',
      '.fg-summary:focus-visible { outline:3px solid var(--fg-accent);outline-offset:-3px; }',
      '.fg-num { display:flex;align-items:center;justify-content:center;min-width:38px;height:38px;background:var(--fg-accent);color:#fff;border-radius:9px;font:700 .95rem/1 "Inter",sans-serif;flex-shrink:0; }',
      '.fg-lesson-title { flex:1;font:600 1rem/1.35 "Cormorant Garamond",Georgia,serif;color:#1a1a2e;font-size:1.08rem; }',
      '.fg-chev { color:#999;font-size:.8rem;transition:transform .2s; }',
      '.fg-lesson[open] .fg-chev { transform:rotate(180deg); }',
      '.fg-body { padding:0 1.2rem 1.2rem;border-top:1px solid #eeeee8; }',
      '.fg-row { display:grid;grid-template-columns:minmax(140px,190px) 1fr;gap:.4rem 1.2rem;padding:.85rem 0;border-bottom:1px solid #f2f2ec; }',
      '.fg-row:last-of-type { border-bottom:none; }',
      '.fg-label { font:600 .72rem/1.4 "Inter",sans-serif;text-transform:uppercase;letter-spacing:.06em;color:#8a8a96;padding-top:.15rem; }',
      '.fg-value { font:400 .89rem/1.65 "Inter",sans-serif;color:#3a3a48; }',
      '.fg-value em { color:var(--fg-accent);font-style:italic;font-weight:500; }',
      '.fg-dinner { background:#f7f7f2;border:1px solid #e6e6de;border-radius:10px;padding:.9rem 1.1rem;margin-top:.9rem; }',
      '.fg-dinner-label { font:600 .68rem/1.4 "Inter",sans-serif;text-transform:uppercase;letter-spacing:.08em;color:var(--fg-accent);margin-bottom:.4rem; }',
      '.fg-dinner-en { font:600 .98rem/1.45 "Cormorant Garamond",Georgia,serif;font-size:1.05rem;color:#1a1a2e; }',
      '.fg-dinner-pt { font:400 .84rem/1.55 "Inter",sans-serif;color:#6a6a78;margin-top:.3rem; }',
      '.fg-note { font:400 .86rem/1.6 "Inter",sans-serif;color:#4a4a5a;margin-top:.9rem;padding-top:.8rem;border-top:1px dashed #e0e0d8; }',
      '.fg-note strong { color:#1a1a2e; }',
      '.fg-close { font:400 .86rem/1.6 "Inter",sans-serif;color:#777;margin-top:1.2rem;max-width:66ch; }',
      '@media (max-width:640px) {',
      '  .fg-row { grid-template-columns:1fr;gap:.15rem; }',
      '}',
      '@media (prefers-reduced-motion:reduce) { .fg-chev { transition:none; } }'
    ].join('\n');
    document.head.appendChild(style);
  }

  function escHTML(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; }

})();
