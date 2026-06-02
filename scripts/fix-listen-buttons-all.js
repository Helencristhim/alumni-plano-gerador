/**
 * fix-listen-buttons-all.js
 *
 * Fixes Listen buttons in ALL ordering exercises:
 * 1. Adds Listen button where missing (BEFORE the order container)
 * 2. Moves Listen button to BEFORE the container if it's AFTER
 * 3. Adds audioMap entry if missing
 *
 * Usage: node scripts/fix-listen-buttons-all.js [--dry-run]
 */

const fs = require('fs');
const path = require('path');

const ALUNO_DIR = path.join(__dirname, '..', 'public', 'aluno');
const PROFESSOR_DIR = path.join(__dirname, '..', 'public', 'professor');
const DRY_RUN = process.argv.includes('--dry-run');

const LISTEN_BTN_TEMPLATE = `<button class="btn btn-listen" onclick="speakText('[ORDER_ID]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg>
        Listen
      </button>`;

function getBaseSlug(slug) {
  return slug.replace(/-aula\d+$/, '');
}

function decodeEntities(str) {
  return str
    .replace(/&amp;/g, '&')
    .replace(/&#39;/g, "'")
    .replace(/&ldquo;/g, '')
    .replace(/&rdquo;/g, '')
    .replace(/&#227;/g, 'ã')
    .replace(/\s+/g, ' ')
    .trim();
}

function generateAudioFilename(containerId) {
  return containerId.replace(/-/g, '_') + '_ordering.mp3';
}

function processFile(filePath, label) {
  const file = path.basename(filePath);
  const slug = file.replace('.html', '');
  const baseSlug = getBaseSlug(slug);
  let html = fs.readFileSync(filePath, 'utf-8');
  let modified = false;
  const fixes = [];

  // Find all order containers
  const containerRegex = /id="(order-[^"]+)"/g;
  const containerIds = new Set();
  let m;
  while ((m = containerRegex.exec(html)) !== null) {
    containerIds.add(m[1]);
  }

  if (containerIds.size === 0) return null;

  for (const containerId of containerIds) {
    const containerPos = html.indexOf(`id="${containerId}"`);
    if (containerPos === -1) continue;

    // Check if Listen button exists for this container
    const listenPattern = new RegExp(`speakText\\(['"]\\[${containerId}\\]['"]`);
    const listenMatch = listenPattern.exec(html);
    const hasListen = !!listenMatch;
    const listenBeforeContainer = hasListen && listenMatch.index < containerPos;

    // Check audioMap entry
    const audioMapRegex = new RegExp(`"\\[${containerId}\\]"\\s*:\\s*"[^"]+"`);
    const hasAudioMap = audioMapRegex.test(html);

    if (hasListen && listenBeforeContainer && hasAudioMap) continue; // All good

    // FIX 1: Add audioMap entry if missing
    if (!hasAudioMap) {
      const audioFile = generateAudioFilename(containerId);
      const audioPath = `/audio/${baseSlug}/${audioFile}`;
      const newEntry = `  "[${containerId}]": "${audioPath}",`;

      // Find the audioMap opening
      const audioMapPos = html.indexOf('audioMap');
      if (audioMapPos !== -1) {
        // Find first entry after audioMap = {
        const openBrace = html.indexOf('{', audioMapPos);
        if (openBrace !== -1) {
          // Insert after opening brace + newline
          const insertPos = openBrace + 1;
          const nextChar = html[insertPos];
          const prefix = nextChar === '\n' ? '\n' : '\n';
          html = html.substring(0, insertPos) + prefix + newEntry + html.substring(insertPos);
          modified = true;
          fixes.push(`audioMap added: [${containerId}]`);
        }
      }
    }

    // FIX 2: Listen button missing or in wrong position
    if (!hasListen) {
      // Add Listen button BEFORE the order container div
      const containerDiv = `<div class="order-container" id="${containerId}">`;
      const containerDivPos = html.indexOf(containerDiv);
      if (containerDivPos !== -1) {
        const btnHtml = LISTEN_BTN_TEMPLATE.replace('ORDER_ID', containerId);
        html = html.substring(0, containerDivPos) + btnHtml + '\n      ' + html.substring(containerDivPos);
        modified = true;
        fixes.push(`Listen added: ${containerId}`);
      }
    } else if (!listenBeforeContainer) {
      // Listen exists but AFTER container - need to move it
      // Find and remove the existing listen button
      const btnRegex = new RegExp(
        `<button[^>]*speakText\\(['"]\\[${containerId}\\]['"][^>]*>[\\s\\S]*?<\\/button>`,
        ''
      );
      const btnMatch = btnRegex.exec(html);
      if (btnMatch && btnMatch.index > containerPos) {
        // Remove from current position
        html = html.substring(0, btnMatch.index) + html.substring(btnMatch.index + btnMatch[0].length);

        // Add BEFORE the container
        const containerDiv = `<div class="order-container" id="${containerId}">`;
        const newContainerPos = html.indexOf(containerDiv);
        if (newContainerPos !== -1) {
          const btnHtml = LISTEN_BTN_TEMPLATE.replace('ORDER_ID', containerId);
          html = html.substring(0, newContainerPos) + btnHtml + '\n      ' + html.substring(newContainerPos);
          modified = true;
          fixes.push(`Listen moved BEFORE: ${containerId}`);
        }
      }
    }
  }

  if (modified) {
    if (!DRY_RUN) {
      fs.writeFileSync(filePath, html);
    }
    console.log(`  ${DRY_RUN ? '[DRY] ' : ''}${label}/${file}: ${fixes.join(', ')}`);
  }

  return fixes.length > 0 ? fixes : null;
}

console.log(DRY_RUN ? '=== DRY RUN ===' : '=== FIXING LISTEN BUTTONS ===\n');

let totalFixes = 0;
for (const dir of [ALUNO_DIR, PROFESSOR_DIR]) {
  if (!fs.existsSync(dir)) continue;
  const label = path.basename(dir);
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html')).sort();
  for (const file of files) {
    const result = processFile(path.join(dir, file), label);
    if (result) totalFixes += result.length;
  }
}

console.log(`\nTotal fixes applied: ${totalFixes}`);
