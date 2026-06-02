/**
 * update-ordering-audiomap.js
 *
 * Updates audioMap entries for ordering exercises to point to the new
 * standardized filenames (order_lN_ordering.mp3).
 *
 * Usage: node scripts/update-ordering-audiomap.js [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const DIRS = [
  path.join(__dirname, '..', 'public', 'aluno'),
  path.join(__dirname, '..', 'public', 'professor')
];
const DRY_RUN = process.argv.includes('--dry-run');

function getBaseSlug(slug) {
  return slug.replace(/-aula\d+$/, '').replace(/-backup-a2$/, '');
}

function processFile(filePath, label) {
  const file = path.basename(filePath);
  const slug = file.replace('.html', '');
  const baseSlug = getBaseSlug(slug);
  let html = fs.readFileSync(filePath, 'utf-8');
  let modified = false;
  const fixes = [];

  // Find all audioMap entries for ordering
  const orderMapRegex = /("(\[order-[^\]]+\])")\s*:\s*"([^"]+)"/g;
  let match;
  while ((match = orderMapRegex.exec(html)) !== null) {
    const fullKey = match[1]; // "[order-l1]"
    const containerId = match[2].replace(/[\[\]]/g, ''); // order-l1
    const currentPath = match[3];
    const newFilename = containerId.replace(/-/g, '_') + '_ordering.mp3';
    const newPath = `/audio/${baseSlug}/${newFilename}`;

    if (currentPath !== newPath) {
      html = html.replace(
        `${fullKey}: "${currentPath}"`,
        `${fullKey}: "${newPath}"`
      );
      modified = true;
      fixes.push(`${containerId}: ${path.basename(currentPath)} -> ${newFilename}`);
    }
  }

  if (modified) {
    // Remove duplicate entries (some files have duplicates like Carlos order-l3)
    // Find and deduplicate
    const seen = new Set();
    const lines = html.split('\n');
    const cleanLines = [];
    for (const line of lines) {
      const dupMatch = line.match(/"(\[order-[^\]]+\])"\s*:/);
      if (dupMatch) {
        if (seen.has(dupMatch[1])) {
          fixes.push(`removed duplicate: ${dupMatch[1]}`);
          continue; // skip duplicate
        }
        seen.add(dupMatch[1]);
      }
      cleanLines.push(line);
    }
    html = cleanLines.join('\n');

    if (!DRY_RUN) {
      fs.writeFileSync(filePath, html);
    }
    console.log(`  ${DRY_RUN ? '[DRY] ' : ''}${label}/${file}: ${fixes.join(', ')}`);
  }

  return fixes.length > 0;
}

console.log(DRY_RUN ? '=== DRY RUN ===' : '=== UPDATING AUDIOMAP ===\n');

let total = 0;
for (const dir of DIRS) {
  if (!fs.existsSync(dir)) continue;
  const label = path.basename(dir);
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();
  for (const file of files) {
    if (processFile(path.join(dir, file), label)) total++;
  }
}

console.log(`\nTotal files updated: ${total}`);
