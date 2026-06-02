/**
 * fix-checkorder-all.js
 *
 * Fixes checkOrder in ALL student/professor HTML files.
 * Handles all formatting variants (2-space, 4-space, one-line, minified, const).
 * Skips zilaudio (completely different implementation).
 *
 * Usage: node scripts/fix-checkorder-all.js [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const DIRS = [
  path.join(__dirname, '..', 'public', 'aluno'),
  path.join(__dirname, '..', 'public', 'professor')
];
const DRY_RUN = process.argv.includes('--dry-run');

const NEW_FN = `function checkOrder(containerId) {
  var container = document.getElementById(containerId);
  var items = Array.from(container.querySelectorAll('.order-item'));
  var selected = orderSelection[containerId] || [];
  if (selected.length !== items.length) {
    var allCorrect = true;
    items.forEach(function(item, idx) {
      if (parseInt(item.dataset.order) === idx + 1) { item.classList.add('correct-order'); item.querySelector('.order-num').textContent = idx + 1; }
      else { allCorrect = false; item.style.borderColor = 'var(--danger)'; item.classList.add('wrong'); setTimeout(function() { item.classList.remove('wrong'); item.style.borderColor = ''; }, 1000); }
    });
    if (allCorrect) updateProgress();
    return;
  }
  var allCorrect = true;
  selected.forEach(function(item, idx) {
    if (parseInt(item.dataset.order) === idx + 1) { item.classList.add('correct-order'); item.querySelector('.order-num').textContent = idx + 1; }
    else { allCorrect = false; item.style.borderColor = 'var(--danger)'; item.classList.add('wrong'); setTimeout(function() { item.classList.remove('wrong'); item.style.borderColor = ''; item.querySelector('.order-num').textContent = '?'; }, 1000); }
  });
  if (!allCorrect) orderSelection[containerId] = [];
  else updateProgress();
}`;

function extractFunction(html, startPos) {
  // Find the opening brace after function checkOrder(...)
  let braceStart = html.indexOf('{', startPos);
  if (braceStart === -1) return null;

  let depth = 0;
  let i = braceStart;
  while (i < html.length) {
    if (html[i] === '{') depth++;
    else if (html[i] === '}') {
      depth--;
      if (depth === 0) return { start: startPos, end: i + 1 };
    }
    i++;
  }
  return null;
}

function processFile(filePath, label) {
  let html = fs.readFileSync(filePath, 'utf-8');
  const file = path.basename(filePath);

  // Find function checkOrder
  // Match both: "function checkOrder(containerId)" and "function checkOrder(listId)"
  const match = html.match(/(\s*)function checkOrder\((containerId|listId)\)/);
  if (!match) return 'no-function';

  // Skip zilaudio (different implementation with dataset.correct)
  if (match[2] === 'listId' || html.includes('list.dataset.correct')) {
    console.log(`  SKIP (different impl): ${label}/${file}`);
    return 'skipped';
  }

  const indent = match[1]; // preserve leading whitespace
  const startPos = match.index + indent.length; // start after indent

  const fnBounds = extractFunction(html, html.indexOf('function checkOrder', match.index));
  if (!fnBounds) {
    console.log(`  ERROR: could not find function bounds: ${label}/${file}`);
    return 'error';
  }

  const oldFn = html.substring(fnBounds.start, fnBounds.end);

  // Check if already fixed (has the DOM-check fallback)
  if (oldFn.includes('items.forEach(function(item, idx)') && !oldFn.includes('alert(')) {
    console.log(`  Already fixed: ${label}/${file}`);
    return 'already-fixed';
  }

  // Replace
  const newHtml = html.substring(0, fnBounds.start) + NEW_FN + html.substring(fnBounds.end);

  if (!DRY_RUN) {
    fs.writeFileSync(filePath, newHtml);
  }
  console.log(`  ${DRY_RUN ? '[DRY] ' : ''}Fixed: ${label}/${file}`);
  return 'fixed';
}

console.log(DRY_RUN ? '=== DRY RUN ===' : '=== FIXING checkOrder ===\n');

let total = { fixed: 0, skipped: 0, error: 0, already: 0 };

for (const dir of DIRS) {
  if (!fs.existsSync(dir)) continue;
  const label = path.basename(dir);
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();

  for (const file of files) {
    const result = processFile(path.join(dir, file), label);
    if (result === 'fixed') total.fixed++;
    else if (result === 'skipped') total.skipped++;
    else if (result === 'error') total.error++;
    else if (result === 'already-fixed') total.already++;
  }
}

console.log(`\nTotal: ${total.fixed} fixed, ${total.already} already ok, ${total.skipped} skipped, ${total.error} errors`);
