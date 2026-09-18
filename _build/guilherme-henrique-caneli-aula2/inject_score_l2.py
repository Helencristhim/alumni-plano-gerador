#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Poe nos hubs do Guilherme a NOTA por atividade e o painel de nota final.

DE ONDE VEIO
------------
Comparando a aula 2 com o modelo w11_l11e.html do professor, tudo batia menos
uma coisa: no modelo dele cada atividade tem contador ("Correct: 0/6") e a licao
fecha com um painel de nota. Aqui quem media era a barra de progresso do hub, que
conta quanto o aluno FEZ, nao quanto ele ACERTOU. Para quem esta medindo se esta
pronto para uma prova, "4 de 6 no gapped text" vale mais que "78% da aula feita".

O QUE MUDA DE MECANICA, E POR QUE PRECISA MUDAR
-----------------------------------------------
No modelo do professor a questao TRAVA na primeira resposta (dataset.done): ela
conta o acerto, revela a correta e nao deixa tentar de novo. As primitivas do hub
fazem o contrario -- erro some depois de 1,5 s e o aluno tenta ate acertar. Isso e
certo para treino e inutil para nota: a nota fecharia 100% sempre.

Entao, e SO dentro de um bloco .cpe-exam, as tres funcoes de correcao passam a
valer uma tentativa. Fora dele -- nas outras sete aulas do mesmo hub, na aba de
complementares, em qualquer outro aluno -- elas continuam exatamente como eram: o
wrapper delega para a funcao original quando o elemento nao esta num bloco de
prova. Nada foi reescrito; o original continua sendo chamado.

O PROGRESSO CONTINUA SENDO PROGRESSO
------------------------------------
Item respondido ganha .correct, que e o que updateProgress conta como feito, e o
errado ganha TAMBEM .cpe-miss, que vence no CSS e pinta de vermelho. Se o errado
nao ganhasse .correct, a aula ficaria eternamente abaixo de 100% para quem errou
uma questao -- a mesma armadilha que ja tinha tirado o Writing do .think-card.
Barra = quanto fez. Nota = quanto acertou. Sao duas perguntas diferentes.

ONDE A NOTA MORA
----------------
localStorage, chave propria ('...-exam-l2'), por INDICE do item dentro do bloco.
Se o conteudo do bloco mudar de tamanho, os indices deixam de casar: aula que
ganha ou perde questao tem de ganhar data-exam novo, senao a nota antiga gruda na
questao errada. A chave tambem e descartada quando o aluno reseta o progresso (o
resetProgress do hub apaga a chave principal, e a nota sem ela nao significa nada).

Idempotente: roda de novo sem duplicar nada.
USO (da raiz): python3 _build/guilherme-henrique-caneli-aula2/inject_score_l2.py
"""
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
SLUG = 'guilherme-henrique-caneli'
PROF = os.path.join(ROOT, 'public', 'professor', SLUG + '.html')
ALUNO = os.path.join(ROOT, 'public', 'aluno', SLUG + '.html')

MARK_CSS = '/* === CPE: nota por atividade e nota final (aula 2) === */'
MARK_JS = '/* === CPE: motor da nota (aula 2) === */'
MARK_CSS_END = '/* === fim CPE nota === */'
MARK_JS_END = '/* === fim CPE motor da nota === */'

CSS = MARK_CSS + '''
.cpe-count { display:flex;align-items:baseline;gap:.6rem;flex-wrap:wrap;margin:0 0 .7rem;padding:.45rem .85rem;border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:0 8px 8px 0;background:var(--bg-elevated); }
.cpe-count-label { font-weight:700;color:var(--accent);letter-spacing:.08em;text-transform:uppercase;font-size:.68rem; }
.cpe-count-n { font-size:.82rem;font-weight:600;font-variant-numeric:tabular-nums;color:var(--text-mid); }
.cpe-count-n b { font-size:1.05rem;color:var(--text-mid); }
.cpe-count-state { margin-left:auto;color:var(--text-dim);font-size:.72rem;font-style:italic; }
.cpe-count.on .cpe-count-n b { color:var(--accent); }
.cpe-count.full { border-left-color:var(--success); }
.cpe-exam .fill-blank-item.cpe-miss .blank-input.correct { border-bottom-color:var(--danger);color:var(--danger); }
.cpe-exam .match-row.cpe-miss.correct { background:var(--danger-bg);border-color:var(--danger-border); }
.cpe-exam .quiz-option.cpe-miss { background:var(--danger-bg);border-color:var(--danger-border);color:var(--danger); }
.cpe-exam .cpe-locked { pointer-events:none; }
.cpe-exam .match-row select:disabled { opacity:1;color:var(--text);-webkit-text-fill-color:var(--text);background:transparent;cursor:default; }
.cpe-answer { margin:.3rem 0 .4rem;font-size:.78rem;line-height:1.6;color:var(--danger); }
.cpe-answer.ok { color:var(--success); }
.cpe-answer b { color:var(--text); }
.cpe-why { display:block;color:var(--text-dim);font-style:italic;margin-top:.15rem; }
.cpe-warn { margin:.5rem 0 0;font-size:.78rem;color:var(--danger);font-weight:600; }
.match-grid > .cpe-answer { width:100%;margin:-.2rem 0 .2rem .2rem; }
.cpe-grade { margin:1.8rem 0 .4rem;border:1px solid var(--border);border-radius:12px;background:var(--bg-card);padding:1.1rem 1.25rem; }
.cpe-grade-head h4 { margin:0;font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:700; }
.cpe-grade-sub { display:block;font-size:.74rem;color:var(--text-dim);margin:.15rem 0 .9rem;line-height:1.5; }
.cpe-grade-row { display:grid;grid-template-columns:minmax(88px,1.1fr) 2fr auto;gap:.8rem;align-items:center;padding:.42rem 0;border-bottom:1px solid var(--border);font-size:.84rem; }
.cpe-grade-name { font-weight:600; }
.cpe-grade-bar { height:6px;background:var(--border);border-radius:3px;overflow:hidden; }
.cpe-grade-fill { display:block;height:100%;width:0;background:var(--accent);border-radius:3px;transition:width .35s; }
.cpe-grade-n { font-variant-numeric:tabular-nums;color:var(--text-dim);font-size:.8rem; }
.cpe-grade-n b { color:var(--text);font-size:.92rem; }
.cpe-grade-total { display:flex;align-items:baseline;gap:.8rem;margin-top:.9rem;font-weight:700;font-size:.9rem; }
.cpe-grade-score { font-variant-numeric:tabular-nums;color:var(--text-mid); }
.cpe-grade-pct { margin-left:auto;font-family:'Cormorant Garamond',serif;font-size:1.9rem;line-height:1;color:var(--accent); }
.cpe-grade-band { margin-top:.35rem;font-size:.85rem;color:var(--text-mid);line-height:1.55; }
.cpe-grade-note { margin-top:.7rem;font-size:.75rem;color:var(--text-dim);line-height:1.65; }
.cpe-prompts { display:flex;flex-direction:column;gap:.5rem; }
.cpe-prompt { display:flex;gap:.75rem;align-items:baseline;padding:.6rem .85rem;border:1px solid var(--border);border-radius:8px;background:var(--bg-elevated);font-size:.88rem;line-height:1.65; }
.cpe-prompt-n { flex:0 0 1rem;font-weight:700;color:var(--accent);font-size:.8rem; }
.cpe-motion { border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:0 10px 10px 0;padding:.9rem 1.15rem;margin-bottom:.9rem;background:var(--bg-elevated); }
.cpe-motion-head { font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;color:var(--accent);font-weight:700; }
.cpe-motion-text { font-family:'Cormorant Garamond',serif;font-size:1.28rem;line-height:1.35;margin:.3rem 0 .55rem; }
.cpe-motion-rules { font-size:.85rem;line-height:1.7;color:var(--text-mid);margin:0; }
''' + MARK_CSS_END

JS = MARK_JS + '''
(function () {
  var KEY = 'SLUG-exam-l2', MAIN = 'SLUG-aluno';
  var store = {};
  try {
    store = JSON.parse(localStorage.getItem(KEY) || '{}') || {};
    // Progresso resetado: a nota sozinha nao significa nada, e os indices dela
    // apontariam para itens que voltaram a estar em branco.
    if (!localStorage.getItem(MAIN)) { localStorage.removeItem(KEY); store = {}; }
  } catch (e) { store = {}; }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(store)); } catch (e) {} }
  function esc(t) { var d = document.createElement('div'); d.textContent = t == null ? '' : t; return d.innerHTML; }
  function blk(el) { return (el && el.closest) ? el.closest('.cpe-exam') : null; }
  function items(b) { return b.querySelectorAll('.match-row, .fill-blank-item, .quiz-item'); }
  function idxOf(b, el) { return Array.prototype.indexOf.call(items(b), el); }
  function rec(b, i, ok, got) {
    var id = b.dataset.exam;
    if (i < 0) return;
    if (!store[id]) store[id] = {};
    if (store[id][i] === undefined) { store[id][i] = { o: ok ? 1 : 0, g: got || '' }; save(); }
  }
  function note(host, after, html, ok) {
    if (host.querySelector && host.querySelector('.cpe-answer')) return;
    var d = document.createElement('div');
    d.className = 'cpe-answer' + (ok ? ' ok' : '');
    d.innerHTML = html;
    if (after && after.parentNode) after.parentNode.insertBefore(d, after.nextSibling);
    else host.appendChild(d);
  }
  function warn(b, msg) {
    var w = b.querySelector('.cpe-warn');
    if (!w) { w = document.createElement('div'); w.className = 'cpe-warn'; b.appendChild(w); }
    w.textContent = msg;
  }

  // ── travar um item, deixando a resposta certa a vista (como no modelo) ──
  function lockBlank(item, ok, got) {
    if (item.dataset.cpeDone) return;
    item.dataset.cpeDone = '1';
    var input = item.querySelector('.blank-input');
    if (!input) return;
    var answer = input.dataset.answer || '';
    input.classList.remove('wrong');
    input.classList.add('correct');
    input.readOnly = true;
    var hintEl = item.querySelector('.blank-hint-feedback');
    if (hintEl) hintEl.classList.remove('visible');
    if (ok) { if (!input.value) input.value = answer; }
    else {
      item.classList.add('cpe-miss');
      input.value = answer;
      note(item, null, 'You wrote <b>' + (got ? esc(got) : '(nothing)') + '</b>. The answer is <b>' +
           esc(answer) + '</b>.' + (input.dataset.hint ? '<span class="cpe-why">' + esc(input.dataset.hint) + '</span>' : ''), false);
    }
    var btn = item.querySelector('.check-btn');
    if (btn) { btn.disabled = true; btn.classList.add('cpe-locked'); btn.textContent = ok ? 'Correct' : 'Answered'; }
  }
  function lockQuiz(item, chosen, ok) {
    if (item.dataset.cpeDone) return;
    item.dataset.cpeDone = '1';
    item.querySelectorAll('.quiz-option').forEach(function (o) {
      o.classList.remove('wrong');
      o.classList.add('cpe-locked');
      if (o.dataset.correct === 'true') o.classList.add('correct');
    });
    if (!ok && chosen) chosen.classList.add('cpe-miss');
  }
  function lockRow(row, ok, got) {
    if (row.dataset.cpeDone) return;
    row.dataset.cpeDone = '1';
    var sel = row.querySelector('select');
    var picked = '';
    if (sel) {
      if (got) { for (var i = 0; i < sel.options.length; i++) { if (sel.options[i].value === got) { picked = sel.options[i].textContent; break; } } }
      sel.value = row.dataset.answer || '';
      sel.disabled = true;
      sel.classList.add('cpe-locked');
    }
    row.classList.remove('wrong');
    row.classList.add('correct');
    if (!ok) {
      row.classList.add('cpe-miss');
      note(row.parentNode, row, picked ? ('You chose <b>' + esc(picked) + '</b>. The answer is now shown above.')
                                       : 'Left blank. The answer is now shown above.', false);
    }
  }

  // ── contador e painel ──
  function paint(b) {
    var v = store[b.dataset.exam] || {}, right = 0, done = 0, total = parseInt(b.dataset.total, 10) || 0;
    for (var k in v) { if (Object.prototype.hasOwnProperty.call(v, k)) { done++; if (v[k].o) right++; } }
    var c = b.querySelector('.cpe-count');
    if (!c) return;
    var n = c.querySelector('b'); if (n) n.textContent = right;
    var st = c.querySelector('.cpe-count-state');
    if (st) {
      st.textContent = done === 0 ? 'one attempt each'
        : (done < total ? (done + ' of ' + total + ' answered')
        : (right === total ? 'perfect paper' : 'finished, ' + (total - right) + ' to review'));
    }
    c.classList.toggle('on', done > 0);
    c.classList.toggle('full', total > 0 && done >= total);
  }
  function grade() {
    var panel = document.getElementById('cpe-grade-l2');
    if (!panel) return;
    var byPaper = {}, right = 0, total = 0, done = 0;
    document.querySelectorAll('.cpe-exam').forEach(function (b) {
      var p = b.dataset.paper || 'Other', t = parseInt(b.dataset.total, 10) || 0;
      var v = store[b.dataset.exam] || {}, r = 0, d = 0;
      for (var k in v) { if (Object.prototype.hasOwnProperty.call(v, k)) { d++; if (v[k].o) r++; } }
      if (!byPaper[p]) byPaper[p] = { r: 0, t: 0 };
      byPaper[p].r += r; byPaper[p].t += t;
      right += r; total += t; done += d;
    });
    panel.querySelectorAll('.cpe-grade-row').forEach(function (row) {
      var p = byPaper[row.dataset.paper];
      if (!p) return;
      var n = row.querySelector('.cpe-grade-n b'); if (n) n.textContent = p.r;
      var f = row.querySelector('.cpe-grade-fill'); if (f) f.style.width = (p.t ? Math.round(p.r / p.t * 100) : 0) + '%';
    });
    var sc = panel.querySelector('.cpe-grade-score b'); if (sc) sc.textContent = right;
    // O numero grande e o acerto sobre o que JA FOI RESPONDIDO, nao sobre a prova
    // inteira: no meio da aula, "5 de 75" vira 7% e se le como reprovacao quando e
    // so aula pela metade. No fim, respondido == total e o numero e a nota mesmo.
    var pct = done ? Math.round(right / done * 100) : 0;
    var pe = panel.querySelector('.cpe-grade-pct'); if (pe) pe.textContent = pct + '%';
    var band = panel.querySelector('.cpe-grade-band');
    if (band) {
      var txt;
      if (done === 0) txt = 'Nothing answered yet. Each task counts your first answer only.';
      else if (done < total) {
        txt = 'Accuracy on the ' + done + ' questions answered so far. The grade arrives when all ' +
              total + ' are done.';
      }
      else if (pct >= 80) txt = 'Grade A on this paper. At this level the exam is no longer the difficulty.';
      else if (pct >= 75) txt = 'Grade B on this paper.';
      else if (pct >= 60) txt = 'Grade C on this paper, which is a pass at Proficiency.';
      else if (pct >= 45) txt = 'Below a Proficiency pass and above a C1 one. On a real paper this reports as C1.';
      else txt = 'Below C1 on this paper. Look at which paper lost the marks before you look at the total.';
      band.textContent = txt;
    }
  }

  // ── uma tentativa so, e so dentro de .cpe-exam ──
  var oBlank = window.checkBlank, oMatch = window.checkMatch,
      oQuiz = window.selectQuiz, oVerify = window.verifyAllMatches;

  window.checkBlank = function (btn) {
    var item = btn.closest ? btn.closest('.fill-blank-item') : null, b = blk(item);
    if (!b) return oBlank.apply(this, arguments);
    if (item.dataset.cpeDone) return;
    var input = item.querySelector('.blank-input');
    var got = (input.value || '').trim();
    var a = (input.dataset.answer || '').toLowerCase().trim();
    var alt = input.dataset.alt ? input.dataset.alt.toLowerCase().trim() : null;
    var v = got.toLowerCase();
    var ok = (v !== '' && v === a) || (alt !== null && v !== '' && v === alt);
    rec(b, idxOf(b, item), ok, got);
    lockBlank(item, ok, got);
    paint(b); grade();
    if (typeof updateProgress === 'function') updateProgress();
  };

  window.selectQuiz = function (o) {
    var item = o.closest ? o.closest('.quiz-item') : null, b = blk(item);
    if (!b) return oQuiz.apply(this, arguments);
    if (item.dataset.cpeDone) return;
    var ok = o.dataset.correct === 'true';
    rec(b, idxOf(b, item), ok, ok ? '' : (o.textContent || '').trim());
    lockQuiz(item, o, ok);
    paint(b); grade();
    if (typeof updateProgress === 'function') updateProgress();
  };

  // Em bloco de prova o <select> nao corrige sozinho: quem corrige e o botao
  // Check, uma vez so, como no modelo do professor ("complete both tasks, then
  // check"). Sem isso a primeira escolha ja entregaria a resposta.
  window.checkMatch = function (sel) {
    var row = sel.closest ? sel.closest('.match-row') : null, b = blk(row);
    if (!b) return oMatch.apply(this, arguments);
    if (row.dataset.cpeDone) return;
    var w = b.querySelector('.cpe-warn'); if (w) w.textContent = '';
  };

  window.verifyAllMatches = function (gridId) {
    var grid = document.getElementById(gridId), b = blk(grid);
    if (!b) return oVerify.apply(this, arguments);
    if (b.dataset.cpeDone) return;
    var rows = grid.querySelectorAll('.match-row'), faltam = 0;
    rows.forEach(function (r) { var s = r.querySelector('select'); if (!s || !s.value) faltam++; });
    if (faltam) {
      warn(b, 'Answer all ' + rows.length + ' before you check. This task is scored once, on what is on the screen.');
      return;
    }
    b.dataset.cpeDone = '1';
    rows.forEach(function (r) {
      var s = r.querySelector('select'), got = s ? s.value : '';
      var ok = got === r.dataset.answer;
      rec(b, idxOf(b, r), ok, got);
      lockRow(r, ok, got);
    });
    var w = b.querySelector('.cpe-warn'); if (w) w.remove();
    var vb = b.querySelector('.verify-all-btn');
    if (vb) { vb.disabled = true; vb.classList.add('cpe-locked'); vb.textContent = 'Scored'; }
    paint(b); grade();
    if (typeof updateProgress === 'function') updateProgress();
  };

  // ── volta o que ja foi respondido (o loadState do hub so devolve .correct) ──
  function restore() {
    document.querySelectorAll('.cpe-exam').forEach(function (b) {
      var v = store[b.dataset.exam], list = items(b), rowLocked = false;
      if (v) {
        Object.keys(v).forEach(function (k) {
          var el = list[parseInt(k, 10)];
          if (!el) return;
          var ok = !!v[k].o, got = v[k].g || '';
          if (el.classList.contains('fill-blank-item')) lockBlank(el, ok, got);
          else if (el.classList.contains('quiz-item')) {
            var chosen = null;
            if (!ok && got) {
              el.querySelectorAll('.quiz-option').forEach(function (o) {
                if ((o.textContent || '').trim() === got) chosen = o;
              });
            }
            lockQuiz(el, chosen, ok);
          } else { lockRow(el, ok, got); rowLocked = true; }
        });
        if (rowLocked) {
          b.dataset.cpeDone = '1';
          var vb = b.querySelector('.verify-all-btn');
          if (vb) { vb.disabled = true; vb.classList.add('cpe-locked'); vb.textContent = 'Scored'; }
        }
      }
      paint(b);
    });
    grade();
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', restore);
  else restore();
})();
''' + MARK_JS_END
JS = JS.replace('SLUG', SLUG)


def troca(s, ini, fim, novo):
    """Troca o bloco ja injetado, para este script poder rodar de novo depois de
    uma correcao. Sem isto, a segunda versao da nota nunca chegaria ao hub."""
    i = s.index(ini)
    j = s.index(fim, i) + len(fim)
    return s[:i] + novo + s[j:]


def injeta_css(s, css):
    k = s.rindex('</style>')
    return s[:k] + '\n' + css + '\n' + s[k:]


def injeta_js(s, js):
    for m in reversed(list(re.finditer(r'<script(?![^>]*\bsrc=)[^>]*>', s))):
        fim = s.index('</script>', m.end())
        return s[:fim] + '\n' + js + '\n' + s[fim:]
    raise AssertionError('nenhum <script> inline no hub')


def main():
    for path in (PROF, ALUNO):
        s = open(path, encoding='utf-8').read()
        antes = len(s)
        if MARK_CSS in s:
            s = troca(s, MARK_CSS, MARK_CSS_END, CSS)
        else:
            s = injeta_css(s, CSS)
        if MARK_JS in s:
            s = troca(s, MARK_JS, MARK_JS_END, JS)
        else:
            # depende das funcoes do hub: o wrapper guarda a original e a chama de
            # volta fora dos blocos de prova. Se alguma sumir, o bloco todo morre.
            for fn in ('checkBlank', 'selectQuiz', 'checkMatch', 'verifyAllMatches', 'updateProgress'):
                assert 'function %s(' % fn in s, 'hub sem %s: %s' % (fn, path)
            s = injeta_js(s, JS)
        if len(s) == antes:
            print('  = %s ja tinha a nota' % os.path.relpath(path, ROOT))
            continue
        open(path, 'w', encoding='utf-8').write(s)
        print('  + %s: +%d bytes' % (os.path.relpath(path, ROOT), len(s) - antes))


if __name__ == '__main__':
    main()
