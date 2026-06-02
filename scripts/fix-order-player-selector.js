/**
 * Fixes the order player JS selector in all files.
 * Changes from CSS selector (broken with brackets) to JS filter.
 */
const fs = require('fs');
const path = require('path');

const DIRS = [
  path.join(__dirname, '..', 'public', 'aluno'),
  path.join(__dirname, '..', 'public', 'professor')
];

const OLD_LINE = `document.querySelectorAll('.btn-listen[onclick*="order-"],.btn-listen[onclick*="order_"]').forEach(function(btn) {
    var m = btn.getAttribute('onclick').match(/speakText\\(['"](\\/\\[[^\\]]+\\])['"]/);
    if (!m) return;
    var key = m[1];
    var src = audioMap[key] || audioMap[key.replace(/\\\\'/g,"'")];`;

const NEW_LINE = `document.querySelectorAll('button[onclick]').forEach(function(btn) {
    var oc = btn.getAttribute('onclick') || '';
    if (oc.indexOf('speakText') === -1 || oc.indexOf('order') === -1) return;
    var m = oc.match(/speakText\\(['"](\\/\\[[^\\]]+\\])['"]/);
    if (!m) return;
    var key = m[1];
    var src = audioMap[key] || audioMap[key.replace(/\\\\'/g,"'")];`;

let total = 0;
for (const dir of DIRS) {
  if (!fs.existsSync(dir)) continue;
  for (const file of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
    const fp = path.join(dir, file);
    let html = fs.readFileSync(fp, 'utf-8');
    if (html.includes("'.btn-listen[onclick") && html.includes('ORDER PLAYER')) {
      html = html.replace(OLD_LINE, NEW_LINE);
      fs.writeFileSync(fp, html);
      console.log(`Fixed: ${path.basename(dir)}/${file}`);
      total++;
    }
  }
}
console.log(`\nTotal: ${total}`);
