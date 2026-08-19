// Supabase client-side config (publishable key is safe for browser)
const SUPABASE_URL = 'https://xxdggcopydghbmgqqebq.supabase.co';
const SUPABASE_ANON_KEY = 'sb_publishable_RjekGapp8WtVbDx0J8etDg_hVq7na29';
const sb = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

/* ==========================================================================
 * ACESSO DO ALUNO — pede a senha antes de liberar a pagina
 * --------------------------------------------------------------------------
 * Mora aqui porque este arquivo ja e carregado no <head> de todos os materiais
 * (1423 dos 1427). Assim o bloqueio vale para todo mundo sem editar um unico HTML
 * de aluno — o legado nao e tocado (REGRA 30).
 *
 * De onde veio: em 19/08/2026 o Pre-class do rafael-pelizaro apareceu inteiro
 * respondido, das aulas 1 a 20, porque alguem abriu o LINK DO ALUNO e fez os
 * exercicios. O aluno entao encontra tudo pronto e nao consegue fazer o proprio
 * material.
 *
 * O que protege e o que nao protege — sem ilusao:
 *   PROTEGE      uso casual: link aberto por engano, colega curioso, teste na pagina
 *                errada. E o caso real acima.
 *   NAO PROTEGE  quem sabe usar F12 ou curl. O HTML continua servido estaticamente;
 *                isto esconde a tela, nao o arquivo. Fechar de verdade exige middleware
 *                segurando o proprio HTML.
 *
 * FAIL-OPEN de proposito: se a API cair, responder erro ou a env var nao existir, o
 * material ABRE. Trancar 123 alunos para fora por causa de uma falha nossa seria pior
 * do que o problema que isto resolve.
 * ======================================================================== */
(function () {
  var caminho = location.pathname;
  if (caminho.indexOf('/aluno/') === -1) return;      // so a visao do aluno
  if (location.protocol === 'file:') return;          // testes locais e auditorias

  var slug = decodeURIComponent(caminho.split('/').pop())
    .replace(/\.html$/, '')
    .replace(/-aula\d+$/, '');                        // a senha e do ALUNO, nao da aula
  if (!slug) return;

  var chave = 'alumni-acesso-' + slug;
  try { if (localStorage.getItem(chave) === 'ok') return; } catch (e) { return; }

  var esconde = document.createElement('style');
  esconde.textContent = 'body{visibility:hidden!important}';
  document.head.appendChild(esconde);

  function liberar() {
    try { localStorage.setItem(chave, 'ok'); } catch (e) {}
    if (esconde.parentNode) esconde.parentNode.removeChild(esconde);
    var o = document.getElementById('alumni-gate');
    if (o && o.parentNode) o.parentNode.removeChild(o);
  }

  function perguntar() {
    var o = document.createElement('div');
    o.id = 'alumni-gate';
    o.setAttribute('style', 'position:fixed;inset:0;z-index:2147483647;visibility:visible;' +
      'background:#f5f5f0;display:flex;align-items:center;justify-content:center;padding:24px;' +
      'font:400 16px/1.5 -apple-system,BlinkMacSystemFont,"Inter",sans-serif');
    o.innerHTML =
      '<div style="background:#fff;border:1px solid #d4d4cc;border-radius:14px;padding:32px 28px;' +
      'max-width:360px;width:100%;text-align:center;box-shadow:0 4px 24px rgba(0,0,0,.06)">' +
      '<div style="font:600 13px/1.4 -apple-system,sans-serif;letter-spacing:.08em;' +
      'text-transform:uppercase;color:#003080;margin-bottom:10px">Alumni by Better</div>' +
      '<div style="color:#2d2d3a;margin-bottom:20px">Digite o seu código de acesso</div>' +
      '<input id="alumni-gate-in" inputmode="numeric" autocomplete="off" maxlength="8" ' +
      'aria-label="Código de acesso" ' +
      'style="width:100%;padding:12px;font:600 22px/1 -apple-system,sans-serif;text-align:center;' +
      'letter-spacing:.3em;border:2px solid #d4d4cc;border-radius:8px;background:#fafaf7;color:#1a1a2e">' +
      '<div id="alumni-gate-erro" role="alert" style="min-height:20px;margin-top:8px;font-size:13px;color:#dc2626"></div>' +
      '<button id="alumni-gate-ok" style="width:100%;margin-top:8px;padding:12px;font:600 15px/1 -apple-system,sans-serif;' +
      'color:#fff;background:#003080;border:2px solid #003080;border-radius:8px;cursor:pointer">Entrar</button>' +
      '<div style="margin-top:14px;font-size:12px;color:#5c5c6c">Não sabe o código? Fale com a sua professora.</div>' +
      '</div>';
    document.body.appendChild(o);

    var input = document.getElementById('alumni-gate-in');
    var erro = document.getElementById('alumni-gate-erro');
    var botao = document.getElementById('alumni-gate-ok');
    input.focus();

    function tentar() {
      var v = (input.value || '').trim();
      if (!v) return;
      botao.disabled = true; botao.textContent = 'Verificando...'; erro.textContent = '';
      fetch('/api/acesso', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ slug: slug, senha: v })
      }).then(function (r) {
        return r.json().catch(function () { return { ok: r.ok }; });
      }).then(function (d) {
        if (d && d.ok) return liberar();
        erro.textContent = 'Código incorreto.';
        input.value = ''; input.focus();
        botao.disabled = false; botao.textContent = 'Entrar';
      }).catch(function () {
        liberar();   // FAIL-OPEN: falha de rede não tranca o aluno
      });
    }
    botao.addEventListener('click', tentar);
    input.addEventListener('keydown', function (e) { if (e.key === 'Enter') tentar(); });
  }

  // Se a env var não estiver configurada, o servidor responde semSenha e nem chegamos a
  // perguntar — o material abre normalmente.
  function iniciar() {
    fetch('/api/acesso', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ slug: slug })
    }).then(function (r) {
      return r.json().catch(function () { return null; });
    }).then(function (d) {
      if (d && d.ok && d.semSenha) return liberar();
      perguntar();
    }).catch(function () {
      liberar();   // FAIL-OPEN
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar);
  else iniciar();
})();
