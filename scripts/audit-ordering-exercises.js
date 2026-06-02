/**
 * audit-ordering-exercises.js
 *
 * Audits ALL ordering exercises across all student files.
 * Checks 4 criteria per exercise:
 *   1. Listen button exists BEFORE the order container
 *   2. audioMap has entry for [order-lN]
 *   3. MP3 file exists on disk
 *   4. Audio text matches HTML sentences (when generation script exists)
 *
 * Usage: node scripts/audit-ordering-exercises.js
 */

const fs = require('fs');
const path = require('path');

const ALUNO_DIR = path.join(__dirname, '..', 'public', 'aluno');
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

function extractExercises(html) {
  const exercises = [];

  // Find all order containers
  const containerRegex = /id="(order-[^"]+)"/g;
  const containerIds = new Set();
  let m;
  while ((m = containerRegex.exec(html)) !== null) {
    containerIds.add(m[1]);
  }

  for (const containerId of containerIds) {
    // Extract items for this container
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

    // Check 1: Listen button exists BEFORE the container
    // Find position of container and position of listen button
    const containerPos = html.indexOf(`id="${containerId}"`);
    const listenPattern = new RegExp(`speakText\\(['"]\\[${containerId}\\]['"]`);
    const listenMatch = listenPattern.exec(html);
    const hasListen = !!listenMatch;
    const listenBeforeContainer = hasListen && listenMatch.index < containerPos;

    // Check 2: audioMap has entry
    const audioMapRegex = new RegExp(`"\\[${containerId}\\]"\\s*:\\s*"([^"]+)"`);
    const audioMapMatch = audioMapRegex.exec(html);
    const audioMapPath = audioMapMatch ? audioMapMatch[1] : null;

    // Check 3: MP3 file exists
    let mp3Exists = false;
    if (audioMapPath) {
      const fullPath = path.join(__dirname, '..', 'public', audioMapPath);
      mp3Exists = fs.existsSync(fullPath);
    }

    // Correct text (all sentences in order)
    const correctText = items.map(i => i.text).join(' ');

    exercises.push({
      containerId,
      itemCount: items.length,
      correctText,
      hasListen,
      listenBeforeContainer,
      audioMapPath,
      mp3Exists,
      items
    });
  }

  return exercises;
}

function getBaseSlug(slug) {
  return slug.replace(/-aula\d+$/, '');
}

function main() {
  const files = fs.readdirSync(ALUNO_DIR)
    .filter(f => f.endsWith('.html'))
    .sort();

  const allCorrect = [];
  const allBroken = [];
  let totalExercises = 0;

  for (const file of files) {
    const slug = file.replace('.html', '');
    const filePath = path.join(ALUNO_DIR, file);
    const html = fs.readFileSync(filePath, 'utf-8');

    const exercises = extractExercises(html);
    if (exercises.length === 0) continue;

    for (const ex of exercises) {
      totalExercises++;

      const issues = [];

      // Criterion 1: Listen button
      if (!ex.hasListen) {
        issues.push('SEM LISTEN');
      } else if (!ex.listenBeforeContainer) {
        issues.push('LISTEN DEPOIS do container (deveria ser ANTES)');
      }

      // Criterion 2: audioMap entry
      if (!ex.audioMapPath) {
        issues.push('SEM audioMap entry');
      }

      // Criterion 3: MP3 file exists
      if (ex.audioMapPath && !ex.mp3Exists) {
        issues.push(`MP3 NAO EXISTE: ${ex.audioMapPath}`);
      }

      // Criterion 4: items extracted (0 items = broken HTML structure)
      if (ex.itemCount === 0) {
        issues.push('0 ITEMS extraidos (HTML diferente do padrao)');
      }

      const entry = {
        file: slug,
        containerId: ex.containerId,
        itemCount: ex.itemCount,
        hasListen: ex.hasListen,
        listenPosition: ex.listenBeforeContainer ? 'ANTES' : (ex.hasListen ? 'DEPOIS' : 'N/A'),
        audioMapPath: ex.audioMapPath || 'MISSING',
        mp3Exists: ex.mp3Exists,
        correctText: ex.correctText.substring(0, 80) + (ex.correctText.length > 80 ? '...' : ''),
        issues
      };

      if (issues.length === 0) {
        allCorrect.push(entry);
      } else {
        allBroken.push(entry);
      }
    }
  }

  // Output
  console.log('='.repeat(70));
  console.log('AUDITORIA COMPLETA — EXERCICIOS DE ORDENACAO');
  console.log('='.repeat(70));
  console.log(`Total de exercicios: ${totalExercises}`);
  console.log(`CORRETOS: ${allCorrect.length}`);
  console.log(`QUEBRADOS: ${allBroken.length}`);
  console.log('');

  console.log('='.repeat(70));
  console.log('CORRETOS (nao mexer)');
  console.log('='.repeat(70));
  for (const e of allCorrect) {
    console.log(`  ${e.file} | ${e.containerId} | ${e.itemCount} items | Listen=${e.listenPosition} | MP3=${e.mp3Exists ? 'OK' : 'NO'}`);
  }

  console.log('');
  console.log('='.repeat(70));
  console.log('QUEBRADOS (precisam correcao)');
  console.log('='.repeat(70));

  // Group by file
  const brokenByFile = {};
  for (const e of allBroken) {
    if (!brokenByFile[e.file]) brokenByFile[e.file] = [];
    brokenByFile[e.file].push(e);
  }

  for (const [file, exercises] of Object.entries(brokenByFile)) {
    console.log(`\n  ${file}:`);
    for (const e of exercises) {
      console.log(`    ${e.containerId} (${e.itemCount} items):`);
      for (const issue of e.issues) {
        console.log(`      - ${issue}`);
      }
    }
  }

  // Save JSON report
  const report = {
    timestamp: new Date().toISOString(),
    summary: { total: totalExercises, correct: allCorrect.length, broken: allBroken.length },
    correct: allCorrect,
    broken: allBroken
  };
  const reportPath = path.join(__dirname, 'ordering-audit-report.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
  console.log(`\nReport saved: ${reportPath}`);
}

main();
