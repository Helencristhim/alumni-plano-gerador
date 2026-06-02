/**
 * Grupo 1 — Correções universais IN CLASS (zero risco)
 * 1. scrollTop = 0 no goToSlide
 * 2. Remover justify-content:center do .slide + adicionar ::before/::after flex:1 + padding-top:4.5rem
 * 3. revealVCard/revealVocab classList.add → classList.toggle
 *
 * REGRA MASTER: NÃO altera conteúdo, layout ou funcionalidade existente.
 * Apenas corrige bugs de navegação e interação.
 */

const fs = require('fs');
const path = require('path');
const glob = require('path');

const DIR = path.join(__dirname, '..', 'public', 'professor');

// Find all aula files
const files = fs.readdirSync(DIR).filter(f => f.match(/-aula\d+\.html$/) && f !== 'patricia-ruffo-aula5.html');

let stats = { scrollReset: 0, justifyFix: 0, toggleFix: 0, skipped: [] };

for (const file of files) {
  const filePath = path.join(DIR, file);
  let html = fs.readFileSync(filePath, 'utf8');
  const original = html;
  let changes = [];

  // === FIX 1: scroll reset in goToSlide ===
  // Pattern: goToSlide function that sets classList but doesn't reset scrollTop
  if (html.includes('goToSlide') && !html.includes('scrollTop')) {
    // Find the pattern: slides[currentSlide].classList.add('active');\n  updateSlide();
    const pattern1 = /slides\[currentSlide\]\.classList\.add\('active'\);\s*\n(\s*)updateSlide\(\);/;
    if (pattern1.test(html)) {
      html = html.replace(pattern1, (match, indent) => {
        return `slides[currentSlide].classList.add('active');\n${indent}slides[currentSlide].scrollTop = 0;\n${indent}updateSlide();`;
      });
      changes.push('scrollReset');
      stats.scrollReset++;
    }
  }

  // === FIX 2: justify-content:center on .slide → remove + add ::before/::after ===
  if (html.includes('justify-content:center') && html.includes('.slide {') || html.includes('.slide{')) {
    // Remove justify-content:center from the .slide flex definition
    // Pattern in the slide CSS line
    const jcPattern = /(display:flex;\s*flex-direction:column;)\s*justify-content:center;(\s*align-items:center;)/;
    if (jcPattern.test(html)) {
      html = html.replace(jcPattern, '$1$2');
      changes.push('removeJustifyCenter');
    }

    // Add padding-top and ::before/::after if not already present
    if (!html.includes('padding-top:4.5rem') && !html.includes('padding-top: 4.5rem')) {
      // Find .slide.active line and add after it
      const activePattern = /\.slide\.active\s*\{[^}]+\}/;
      const activeMatch = html.match(activePattern);
      if (activeMatch) {
        const insertAfter = activeMatch[0];
        html = html.replace(insertAfter, insertAfter + '\n.slide { padding-top:4.5rem; padding-bottom:4rem; }\n.slide::before, .slide::after { content:\'\'; flex:1; }\n');
        changes.push('addPaddingAndFlex');
        stats.justifyFix++;
      }
    }
  } else if (!html.includes('justify-content:center') && !html.includes('padding-top:4.5rem') && !html.includes('padding-top: 4.5rem')) {
    // File doesn't have justify-content issue but may still need padding
    // Check if it has the slide system
    if (html.includes('.slide.active')) {
      const activePattern = /\.slide\.active\s*\{[^}]+\}/;
      const activeMatch = html.match(activePattern);
      if (activeMatch) {
        const insertAfter = activeMatch[0];
        html = html.replace(insertAfter, insertAfter + '\n.slide { padding-top:4.5rem; padding-bottom:4rem; }\n.slide::before, .slide::after { content:\'\'; flex:1; }\n');
        changes.push('addPaddingAndFlex(noJC)');
        stats.justifyFix++;
      }
    }
  }

  // === FIX 3: vocab reveal toggle ===
  // Pattern: classList.add('revealed') with guard → classList.toggle('revealed') without guard
  // Common patterns:
  // a) if (card.classList.contains('revealed')) return;\n  card.classList.add('revealed');
  // b) if (card.classList.contains('revealed')) { ... return; } card.classList.add('revealed');
  const togglePatternA = /if\s*\(card\.classList\.contains\('revealed'\)\)\s*return;\s*\n\s*card\.classList\.add\('revealed'\);/g;
  if (togglePatternA.test(html)) {
    html = html.replace(togglePatternA, "card.classList.toggle('revealed');");
    changes.push('vocabToggle');
    stats.toggleFix++;
  }

  // Also check for revealVocab pattern (some files use this name)
  const togglePatternB = /if\s*\(el\.classList\.contains\('revealed'\)\)\s*return;\s*\n\s*el\.classList\.add\('revealed'\);/g;
  if (togglePatternB.test(html)) {
    html = html.replace(togglePatternB, "el.classList.toggle('revealed');");
    if (!changes.includes('vocabToggle')) { changes.push('vocabToggle'); stats.toggleFix++; }
  }

  // Pattern with 'this' instead of card/el
  const togglePatternC = /if\s*\(this\.classList\.contains\('revealed'\)\)\s*return;\s*\n\s*this\.classList\.add\('revealed'\);/g;
  if (togglePatternC.test(html)) {
    html = html.replace(togglePatternC, "this.classList.toggle('revealed');");
    if (!changes.includes('vocabToggle')) { changes.push('vocabToggle'); stats.toggleFix++; }
  }

  // Save if changes were made
  if (html !== original) {
    fs.writeFileSync(filePath, html);
    console.log('[OK] ' + file + ' — ' + changes.join(', '));
  } else {
    stats.skipped.push(file);
    console.log('[SKIP] ' + file + ' — no patterns matched');
  }
}

console.log('\n=== SUMMARY ===');
console.log('Scroll reset: ' + stats.scrollReset + ' files');
console.log('Justify-content fix: ' + stats.justifyFix + ' files');
console.log('Vocab toggle: ' + stats.toggleFix + ' files');
console.log('Skipped: ' + stats.skipped.length + ' files');
if (stats.skipped.length > 0) {
  console.log('Skipped files: ' + stats.skipped.join(', '));
}
