/**
 * audit-ordering-audio-match.js
 *
 * Verifies that the audio TEXT used to generate each ordering MP3
 * matches the ACTUAL sentences in the HTML (in correct data-order).
 *
 * Compares generation scripts vs HTML content.
 * For exercises without generation scripts, flags as UNVERIFIABLE.
 */

const fs = require('fs');
const path = require('path');

const ALUNO_DIR = path.join(__dirname, '..', 'public', 'aluno');
const SCRIPTS_DIR = __dirname;
const AUDIO_BASE = path.join(__dirname, '..', 'public', 'audio');

function decodeEntities(str) {
  return str
    .replace(/&amp;/g, '&')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&#227;/g, 'ã')
    .replace(/&#xe3;/gi, 'ã')
    .replace(/&ldquo;/g, '')
    .replace(/&rdquo;/g, '')
    .replace(/&mdash;/g, '—')
    .replace(/&ndash;/g, '–')
    .replace(/\u201c/g, '')
    .replace(/\u201d/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function normalizeText(str) {
  return str
    .replace(/[""'']/g, '')
    .replace(/&/g, 'and')
    .replace(/M&A/gi, 'M and A')
    .replace(/[^a-zA-Z0-9\s.,!?'()-]/g, '')
    .replace(/\s+/g, ' ')
    .toLowerCase()
    .trim();
}

function extractExercisesFromHTML(html) {
  const exercises = {};
  const containerRegex = /id="(order-[^"]+)"/g;
  const containerIds = new Set();
  let m;
  while ((m = containerRegex.exec(html)) !== null) {
    containerIds.add(m[1]);
  }

  for (const containerId of containerIds) {
    const itemRegex = new RegExp(
      `data-order="(\\d+)"[^>]*onclick="selectOrderItem\\(this,'${containerId}'\\)"[\\s\\S]*?<span class="order-text">([\\s\\S]*?)</span>`,
      'g'
    );
    const items = [];
    let itemMatch;
    while ((itemMatch = itemRegex.exec(html)) !== null) {
      const order = parseInt(itemMatch[1]);
      let text = decodeEntities(itemMatch[2]).replace(/^[""\s]+|[""\s]+$/g, '').trim();
      items.push({ order, text });
    }
    items.sort((a, b) => a.order - b.order);
    const correctText = items.map(i => i.text).join(' ');
    exercises[containerId] = { items, correctText };
  }
  return exercises;
}

function extractTextsFromScript(scriptContent) {
  const texts = {};
  // Match patterns like: { file: '...', key: '[order-lN]', text: "..." }
  // or { file: '...', text: "..." } with key derived from file
  const entryRegex = /\{[^}]*?file:\s*['"]([^'"]+)['"][^}]*?text:\s*(['"`])([\s\S]*?)\2[^}]*?\}/g;
  let match;
  while ((match = entryRegex.exec(scriptContent)) !== null) {
    const file = match[1];
    const text = match[3];
    // Try to find key
    const keyMatch = scriptContent.substring(match.index, match.index + match[0].length).match(/key:\s*['"]([^'"]+)['"]/);
    let key = keyMatch ? keyMatch[1] : null;
    if (!key) {
      // Derive from filename: order_l1_xxx.mp3 -> [order-l1]
      const fileMatch = file.match(/order[_-]l(\d+)/i);
      if (fileMatch) key = `[order-l${fileMatch[1]}]`;
    }
    if (key) {
      // Remove brackets for container ID
      const containerId = key.replace(/[\[\]]/g, '');
      texts[containerId] = text;
    }
  }
  return texts;
}

function findGenerationScripts(baseSlug) {
  const scripts = [];
  const allFiles = fs.readdirSync(SCRIPTS_DIR);
  const patterns = [
    `generate-${baseSlug}-order`,
    `generate-order-${baseSlug}`,
    `generate-${baseSlug}-audio`,
    `generate-audio-${baseSlug}`,
  ];
  // Also check parent dir
  const parentDir = path.join(SCRIPTS_DIR, '..');
  const parentFiles = fs.readdirSync(parentDir).filter(f => f.endsWith('.js'));

  for (const f of [...allFiles, ...parentFiles.map(pf => '../' + pf)]) {
    if (!f.endsWith('.js')) continue;
    const lower = f.toLowerCase();
    if (lower.includes(baseSlug) && (lower.includes('order') || lower.includes('audio'))) {
      scripts.push(path.join(SCRIPTS_DIR, f));
    }
  }
  return scripts;
}

function main() {
  const files = fs.readdirSync(ALUNO_DIR)
    .filter(f => f.endsWith('.html'))
    .sort();

  const results = {
    matched: [],      // Audio text == HTML text
    mismatched: [],   // Audio text != HTML text
    unverifiable: [], // No generation script found
    noItems: []       // 0 items extracted
  };

  for (const file of files) {
    const slug = file.replace('.html', '');
    const baseSlug = slug.replace(/-aula\d+$/, '');
    const filePath = path.join(ALUNO_DIR, file);
    const html = fs.readFileSync(filePath, 'utf-8');

    const exercises = extractExercisesFromHTML(html);
    if (Object.keys(exercises).length === 0) continue;

    // Find all generation scripts for this student
    const scriptPaths = findGenerationScripts(baseSlug);
    let scriptTexts = {};
    for (const sp of scriptPaths) {
      try {
        const content = fs.readFileSync(sp, 'utf-8');
        const texts = extractTextsFromScript(content);
        Object.assign(scriptTexts, texts);
      } catch (e) {}
    }

    // Also check audioMap in the HTML for the MP3 path, then find which script generated it
    const audioMapRegex = /"\[(order-[^\]]+)\]"\s*:\s*"([^"]+)"/g;
    let amMatch;
    const audioMapEntries = {};
    while ((amMatch = audioMapRegex.exec(html)) !== null) {
      audioMapEntries[amMatch[1]] = amMatch[2];
    }

    for (const [containerId, exercise] of Object.entries(exercises)) {
      if (exercise.items.length === 0) {
        results.noItems.push({ slug, containerId });
        continue;
      }

      const htmlText = normalizeText(exercise.correctText);
      const scriptText = scriptTexts[containerId] ? normalizeText(scriptTexts[containerId]) : null;

      if (!scriptText) {
        results.unverifiable.push({
          slug,
          containerId,
          itemCount: exercise.items.length,
          audioMapPath: audioMapEntries[containerId] || 'NONE',
          htmlPreview: exercise.correctText.substring(0, 100)
        });
      } else {
        // Compare
        const match = htmlText === scriptText;
        // Also check partial match (in case of minor formatting differences)
        const partialMatch = !match && (
          htmlText.includes(scriptText.substring(0, 50)) ||
          scriptText.includes(htmlText.substring(0, 50))
        );

        const entry = {
          slug,
          containerId,
          itemCount: exercise.items.length,
          audioMapPath: audioMapEntries[containerId] || 'NONE',
          htmlPreview: exercise.correctText.substring(0, 80),
          scriptPreview: scriptTexts[containerId].substring(0, 80)
        };

        if (match || partialMatch) {
          entry.matchType = match ? 'EXACT' : 'PARTIAL';
          results.matched.push(entry);
        } else {
          entry.htmlFull = exercise.correctText;
          entry.scriptFull = scriptTexts[containerId];
          results.mismatched.push(entry);
        }
      }
    }
  }

  // Output
  console.log('='.repeat(70));
  console.log('AUDITORIA DE MATCH: AUDIO vs FRASES HTML');
  console.log('='.repeat(70));
  console.log(`MATCH (audio = frases): ${results.matched.length}`);
  console.log(`MISMATCH (audio != frases): ${results.mismatched.length}`);
  console.log(`NAO VERIFICAVEL (sem script): ${results.unverifiable.length}`);
  console.log(`SEM ITEMS (HTML diferente): ${results.noItems.length}`);

  if (results.matched.length > 0) {
    console.log('\n' + '='.repeat(70));
    console.log('MATCH — Audio bate com frases (CORRETOS)');
    console.log('='.repeat(70));
    for (const e of results.matched) {
      console.log(`  ${e.slug} | ${e.containerId} | ${e.matchType}`);
    }
  }

  if (results.mismatched.length > 0) {
    console.log('\n' + '='.repeat(70));
    console.log('MISMATCH — Audio NAO bate com frases (PRECISAM REGERAR)');
    console.log('='.repeat(70));
    for (const e of results.mismatched) {
      console.log(`\n  ${e.slug} | ${e.containerId}:`);
      console.log(`    HTML:   "${e.htmlPreview}..."`);
      console.log(`    AUDIO:  "${e.scriptPreview}..."`);
    }
  }

  if (results.unverifiable.length > 0) {
    console.log('\n' + '='.repeat(70));
    console.log('NAO VERIFICAVEL — Sem script de geracao encontrado');
    console.log('='.repeat(70));
    for (const e of results.unverifiable) {
      console.log(`  ${e.slug} | ${e.containerId} | ${e.itemCount} items | audioMap: ${e.audioMapPath}`);
    }
  }

  // Save
  const reportPath = path.join(__dirname, 'ordering-audio-match-report.json');
  fs.writeFileSync(reportPath, JSON.stringify(results, null, 2));
  console.log(`\nReport: ${reportPath}`);
}

main();
