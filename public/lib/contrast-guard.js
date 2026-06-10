/*!
 * contrast-guard.js — auto-corrige contraste ilegível em slides escuros (REGRA de contraste).
 * Em vez de depender de listas de classes no CSS (.slide-dark .x { color }), mede o contraste
 * REAL (luminância WCAG do texto x fundo efetivo) de cada elemento de texto dentro de um slide
 * escuro e, SÓ quando o contraste está abaixo de 4.5:1, força a melhor cor (escuro ou branco).
 * Não toca em nada que já está legível. Aditivo, idempotente. Carregar DEPOIS do script principal.
 */
(function () {
  'use strict';
  var MIN_RATIO = 4.5;

  function srgb(v) { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }
  function lum(c) { return 0.2126 * srgb(c.r) + 0.7152 * srgb(c.g) + 0.0722 * srgb(c.b); }
  function ratio(a, b) { var hi = Math.max(a, b) + 0.05, lo = Math.min(a, b) + 0.05; return hi / lo; }

  function parseColor(str) {
    if (!str) return null;
    var m = str.match(/rgba?\(\s*([\d.]+)[,\s]+([\d.]+)[,\s]+([\d.]+)(?:[,\s/]+([\d.%]+))?/i);
    if (!m) return null;
    var a = m[4] === undefined ? 1 : (m[4].indexOf('%') > -1 ? parseFloat(m[4]) / 100 : parseFloat(m[4]));
    return { r: +m[1], g: +m[2], b: +m[3], a: a };
  }

  // Fundo efetivo: sobe a árvore até achar uma cor de fundo com opacidade real.
  function effectiveBg(el) {
    var node = el;
    while (node && node.nodeType === 1) {
      var cs = window.getComputedStyle(node);
      // Se há gradiente/imagem clara, é arriscado adivinhar — pulamos para o pai.
      var bc = parseColor(cs.backgroundColor);
      if (bc && bc.a >= 0.5) return bc;
      node = node.parentElement;
    }
    return null; // desconhecido
  }

  function hasOwnText(el) {
    for (var i = 0; i < el.childNodes.length; i++) {
      var n = el.childNodes[i];
      if (n.nodeType === 3 && n.textContent.trim().length) return true;
    }
    return false;
  }

  function fixScope(root) {
    var darkSlides = root.querySelectorAll('.slide-dark, .slide.dark');
    for (var s = 0; s < darkSlides.length; s++) {
      var slide = darkSlides[s];
      var slideBgC = parseColor(window.getComputedStyle(slide).backgroundColor);
      var slideLum = slideBgC && slideBgC.a >= 0.5 ? lum(slideBgC) : 0.05; // slide escuro ~0.05
      var els = slide.querySelectorAll('*');
      for (var i = 0; i < els.length; i++) {
        var el = els[i];
        if (!hasOwnText(el)) continue;
        if (el.tagName === 'SCRIPT' || el.tagName === 'STYLE' || el.tagName === 'svg') continue;
        var cs = window.getComputedStyle(el);
        var fg = parseColor(cs.color);
        if (!fg || fg.a < 0.3) continue;
        var bg = effectiveBg(el);
        var bgLum = bg ? lum(bg) : slideLum;
        if (ratio(lum(fg), bgLum) >= MIN_RATIO) continue; // já legível
        // escolhe a cor que dá mais contraste contra o fundo
        var target = bgLum > 0.45 ? '#1a1a2e' : '#ffffff';
        el.style.setProperty('color', target, 'important');
      }
    }
  }

  function run() { try { fixScope(document); } catch (e) { /* nunca quebra a página */ } }

  if (document.readyState !== 'loading') run();
  else document.addEventListener('DOMContentLoaded', run);

  // Re-roda ao entrar nos slides / trocar de slide (cobre conteúdo revelado dinamicamente).
  ['enterSlideMode', 'goToSlide', 'startLesson'].forEach(function (fn) {
    if (typeof window[fn] === 'function') {
      var orig = window[fn];
      window[fn] = function () { var r = orig.apply(this, arguments); setTimeout(run, 60); return r; };
    }
  });
  // Conteúdo revelado por clique (vocab, dialogue Next Line, comprehension, etc.)
  document.addEventListener('click', function () { setTimeout(run, 80); }, true);
})();
