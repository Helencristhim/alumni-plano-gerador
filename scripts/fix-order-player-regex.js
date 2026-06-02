const fs = require('fs');
const path = require('path');

const DIRS = [
  path.join(__dirname, '..', 'public', 'aluno'),
  path.join(__dirname, '..', 'public', 'professor')
];

// Exact string as it appears in the files
const BAD = `oc.match(/speakText\\(['"](\\/\\[[^\\]]+\\])['"]/);`;
const GOOD = `oc.match(/speakText\\(['"](\\/?(\\[[^\\]]+\\]))['"]/);`;

let total = 0;
for (const dir of DIRS) {
  if (!fs.existsSync(dir)) continue;
  for (const file of fs.readdirSync(dir).filter(f => f.endsWith('.html'))) {
    const fp = path.join(dir, file);
    let html = fs.readFileSync(fp, 'utf-8');
    if (!html.includes('ORDER PLAYER')) continue;
    if (html.includes(BAD)) {
      html = html.replace(BAD, GOOD);
      fs.writeFileSync(fp, html);
      console.log(`Fixed: ${path.basename(dir)}/${file}`);
      total++;
    } else {
      console.log(`OK/skip: ${path.basename(dir)}/${file}`);
    }
  }
}
console.log(`\nTotal fixed: ${total}`);
