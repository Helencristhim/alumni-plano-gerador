/**
 * INTENSIVO — ponte do feedback entre os dois arquivos (Supabase)
 *
 * O molde Private Black nasceu como UM arquivo com troca de visão: o professor escreve o
 * feedback e a aluna lê o mesmo localStorage. Aqui são DOIS arquivos, em dois navegadores
 * — o material do professor e o link da aluna. Sem esta ponte, o que o professor escreve
 * não chega a lugar nenhum.
 *
 * O que atravessa: só o espaço COMPARTILHADO do registro (papelDe() === 'compartilhado'),
 * que é exatamente o feedback para a aluna (sfb_l{n}_worked / _develop) e o status da aula
 * (af_l{n}_status, que move a barra e os carimbos do cabeçalho). Nada do espaço do
 * professor (avaliação, evidência, ação) e nada do espaço da aluna (as respostas dela)
 * passam por aqui.
 *
 * Direção: o PROFESSOR escreve (upsert com debounce), a ALUNA lê (no load, ao voltar para
 * a aba e a cada 60s). A aluna nunca escreve neste canal — se escrevesse, uma aba dela
 * aberta durante a aula apagaria o feedback recém-digitado.
 *
 * Requer, nesta ordem, ANTES deste arquivo:
 *   supabase.min.js · /lib/supabase-config.js · o script do material (define ld/grava/…)
 *   window.INTENSIVO = { slug: 'rita-rodrigues', papel: 'professor' | 'aluno' }
 *
 * FAIL-OPEN: sem Supabase, sem rede ou com erro, o material funciona igual — só não
 * atravessa. Nada aqui pode impedir a aula de acontecer.
 */
(function () {
  'use strict';

  var cfg = window.INTENSIVO;
  if (!cfg || !cfg.slug || typeof sb === 'undefined') return;
  if (typeof ld !== 'function' || typeof grava !== 'function') return;

  var TABELA = 'student_activity';
  var TIPO = 'intensivo-compartilhado';
  var ESPERA = 1500;

  function compartilhado() {
    var d = ld();
    return d.compartilhado || {};
  }

  /* ---------------- professor: escreve ---------------- */
  var timer = null;

  function empurra() {
    timer = null;
    var estado = compartilhado();
    sb.from(TABELA).upsert({
      student_slug: cfg.slug,
      view_type: TIPO,
      state: estado,
      updated_at: new Date().toISOString()
    }, { onConflict: 'student_slug,view_type' }).then(function (r) {
      if (r && r.error) console.warn('[intensivo-sync] não subiu:', r.error.message);
    });
  }

  function agenda() {
    if (timer) clearTimeout(timer);
    timer = setTimeout(empurra, ESPERA);
  }

  /* ---------------- aluna: lê ---------------- */
  function repinta() {
    /* cada um destes existe no arquivo da aluna e é o que o feedback muda na tela */
    if (typeof sfBuild === 'function') sfBuild();
    if (typeof hubPaint === 'function') hubPaint();
    if (typeof lcStatus === 'function') lcStatus();
  }

  function puxa() {
    sb.from(TABELA).select('state').eq('student_slug', cfg.slug).eq('view_type', TIPO)
      .maybeSingle().then(function (r) {
        if (!r || r.error || !r.data || !r.data.state) return;
        var vindo = r.data.state, d = ld(), mudou = false, k;
        for (k in vindo) {
          if (!Object.prototype.hasOwnProperty.call(vindo, k)) continue;
          if (d.compartilhado[k] === vindo[k]) continue;
          d.compartilhado[k] = vindo[k];
          mudou = true;
        }
        if (!mudou) return;
        grava(d);
        repinta();
      });
  }

  if (cfg.papel === 'professor') {
    /* o material já grava tudo em localStorage por persSave(); o que se acrescenta aqui é
       o envio. Envolver persSave em vez de ouvir 'input' pega TODOS os campos do registro
       sem depender de quais existem na tela hoje. */
    var original = window.persSave;
    if (typeof original === 'function') {
      window.persSave = function (el) {
        var r = original.apply(this, arguments);
        try {
          var k = el && el.getAttribute && el.getAttribute('data-k');
          if (k && typeof papelDe === 'function' && papelDe(k) === 'compartilhado') agenda();
        } catch (e) {}
        return r;
      };
    }
    window.addEventListener('beforeunload', function () { if (timer) { clearTimeout(timer); empurra(); } });
  } else {
    puxa();
    document.addEventListener('visibilitychange', function () { if (!document.hidden) puxa(); });
    setInterval(puxa, 60000);
  }
})();
