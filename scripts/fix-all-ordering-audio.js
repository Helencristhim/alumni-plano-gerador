/**
 * fix-all-ordering-audio.js
 *
 * Scans ALL student HTML files for ordering exercises,
 * extracts the correct sentence order from data-order attributes,
 * and generates ElevenLabs audio for each ordering exercise.
 * Also reports which files are missing Listen buttons.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=xxx node scripts/fix-all-ordering-audio.js
 *
 *   --dry-run : only report, don't generate audio
 *   --student=slug : only process a specific student
 */

const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';

const ALUNO_DIR = path.join(__dirname, '..', 'public', 'aluno');
const AUDIO_BASE = path.join(__dirname, '..', 'public', 'audio');

const DRY_RUN = process.argv.includes('--dry-run');
const STUDENT_FILTER = process.argv.find(a => a.startsWith('--student='));
const SPECIFIC_STUDENT = STUDENT_FILTER ? STUDENT_FILTER.split('=')[1] : null;

// Gender mapping (F=Ellen, M=Arthur)
const GENDER_MAP = {
  'vanessa-maluf': 'F', 'tuca-dias': 'M', 'tania-rosa': 'F',
  'simone-quiles-de-santana-marques': 'F', 'rubens-tofolo': 'M',
  'roberto-rezende': 'M', 'roberto-pires': 'M', 'rafael-gasparelli-lima': 'M',
  'percival-jr': 'M', 'patricia-ruffo': 'F', 'natalie-viegas': 'F',
  'milton-sayegh': 'M', 'marlene-landucci': 'F', 'mark-kazuyoshi-seki-omagari': 'M',
  'maria-claudia-curimbaba': 'F', 'maisa-de-oliveira-santos': 'F',
  'luiz-bressane': 'M', 'luiz-bressane-backup-a2': 'M',
  'karina-macedo': 'F', 'gleice-leonardo-rocha-de-souza': 'F',
  'gabriela-pires': 'F', 'gabriela-paulucci': 'F', 'elaine-mieko-pinho': 'F',
  'eduardo-chiba': 'M', 'eduarda-gabriel': 'F', 'diogo-leal': 'M',
  'daniela-feitoza': 'F', 'carolina-paludetto-rodrigues': 'F',
  'carlos-vinicius-vale-bassan': 'M', 'andreia-heins': 'F',
  'aline-sberci': 'F', 'zilaudio': 'F', 'pricila-adamo': 'F',
  'dienane-brandao-de-mesquita': 'F'
};

function getSlugFromFilename(filename) {
  return filename.replace('.html', '');
}

function getBaseSlug(slug) {
  // tania-rosa-aula2 -> tania-rosa (for audio directory)
  return slug.replace(/-aula\d+$/, '');
}

function getVoiceId(slug) {
  const baseSlug = getBaseSlug(slug);
  const gender = GENDER_MAP[baseSlug] || 'F';
  return gender === 'M' ? ARTHUR_ID : ELLEN_ID;
}

function getVoiceName(slug) {
  const baseSlug = getBaseSlug(slug);
  const gender = GENDER_MAP[baseSlug] || 'F';
  return gender === 'M' ? 'Arthur' : 'Ellen';
}

function extractOrderingExercises(html, slug) {
  const exercises = [];

  // Find all order containers with their IDs
  const containerRegex = /<div[^>]*class="order-container"[^>]*id="(order-[^"]+)"[^>]*>([\s\S]*?)<\/div>\s*(?:<\/div>\s*)?<button[^>]*onclick="checkOrder/g;

  let match;
  while ((match = containerRegex.exec(html)) !== null) {
    const containerId = match[1];
    const containerHtml = match[2];

    // Extract all order items
    const itemRegex = /<div[^>]*class="order-item"[^>]*data-order="(\d+)"[^>]*>[\s\S]*?<span class="order-text">([\s\S]*?)<\/span>/g;
    const items = [];
    let itemMatch;

    while ((itemMatch = itemRegex.exec(containerHtml)) !== null) {
      const order = parseInt(itemMatch[1]);
      let text = itemMatch[2]
        .replace(/&amp;/g, '&')
        .replace(/&quot;/g, '"')
        .replace(/&#39;/g, "'")
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/\s+/g, ' ')
        .replace(/^[""\s]+|[""\s]+$/g, '')
        .trim();
      items.push({ order, text });
    }

    // Sort by data-order to get correct sequence
    items.sort((a, b) => a.order - b.order);

    // Check if Listen button exists for this container
    const listenPattern = new RegExp(`speakText\\(['"]\\[${containerId}\\]['"]`, 'g');
    const hasListen = listenPattern.test(html);

    // Check if audioMap has entry for this container
    const audioMapPattern = new RegExp(`"\\[${containerId}\\]"\\s*:\\s*"([^"]+)"`, 'g');
    const audioMapMatch = audioMapPattern.exec(html);
    const audioMapEntry = audioMapMatch ? audioMapMatch[1] : null;

    // Generate the combined text (all sentences in correct order)
    const correctText = items.map(i => i.text).join(' ');

    // Generate filename
    const fileSlug = containerId.replace(/-/g, '_');
    const fileName = `${fileSlug}_ordering.mp3`;

    exercises.push({
      containerId,
      items,
      correctText,
      hasListen,
      audioMapEntry,
      audioFile: fileName,
      audioMapKey: `[${containerId}]`
    });
  }

  return exercises;
}

async function generateAudio(text, voiceId, outputPath) {
  if (DRY_RUN) {
    console.log(`  [DRY RUN] Would generate: ${path.basename(outputPath)}`);
    return;
  }

  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    })
  });

  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`ElevenLabs error for ${path.basename(outputPath)}: ${resp.status} - ${err}`);
  }

  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  console.log(`  Generated: ${path.basename(outputPath)} (${buffer.length} bytes)`);
}

async function processStudent(filename) {
  const slug = getSlugFromFilename(filename);
  const baseSlug = getBaseSlug(slug);
  const filePath = path.join(ALUNO_DIR, filename);
  const html = fs.readFileSync(filePath, 'utf-8');

  const exercises = extractOrderingExercises(html, slug);
  if (exercises.length === 0) return null;

  const voiceId = getVoiceId(slug);
  const voiceName = getVoiceName(slug);
  const audioDir = path.join(AUDIO_BASE, baseSlug);

  console.log(`\n=== ${slug} (${voiceName}) — ${exercises.length} ordering exercise(s) ===`);

  const results = {
    slug,
    baseSlug,
    voiceName,
    exercises: [],
    missingListenButtons: [],
    audioGenerated: 0,
    audioMapUpdates: []
  };

  for (const ex of exercises) {
    console.log(`  ${ex.containerId}: ${ex.items.length} items, Listen=${ex.hasListen ? 'YES' : 'MISSING'}`);
    console.log(`    Text: "${ex.correctText.substring(0, 100)}..."`);

    if (!ex.hasListen) {
      results.missingListenButtons.push(ex.containerId);
    }

    // Determine output path
    const outputPath = path.join(audioDir, ex.audioFile);

    // Check if we need the audioMap entry
    const expectedAudioPath = `/audio/${baseSlug}/${ex.audioFile}`;
    if (!ex.audioMapEntry || ex.audioMapEntry !== expectedAudioPath) {
      results.audioMapUpdates.push({
        key: ex.audioMapKey,
        value: expectedAudioPath,
        oldValue: ex.audioMapEntry
      });
    }

    // Generate audio
    if (!fs.existsSync(audioDir)) {
      fs.mkdirSync(audioDir, { recursive: true });
    }

    try {
      await generateAudio(ex.correctText, voiceId, outputPath);
      results.audioGenerated++;
    } catch (err) {
      console.error(`  ERROR: ${err.message}`);
    }

    results.exercises.push(ex);

    // Rate limit: wait 500ms between requests
    if (!DRY_RUN) {
      await new Promise(resolve => setTimeout(resolve, 500));
    }
  }

  return results;
}

async function main() {
  if (!DRY_RUN && !API_KEY) {
    console.error('Set ELEVENLABS_API_KEY or use --dry-run');
    process.exit(1);
  }

  console.log(DRY_RUN ? '=== DRY RUN MODE ===' : '=== GENERATING AUDIO ===');

  const files = fs.readdirSync(ALUNO_DIR)
    .filter(f => f.endsWith('.html'))
    .filter(f => !SPECIFIC_STUDENT || getSlugFromFilename(f) === SPECIFIC_STUDENT || getBaseSlug(getSlugFromFilename(f)) === SPECIFIC_STUDENT);

  const allResults = [];
  let totalExercises = 0;
  let totalMissingListen = 0;
  let totalAudioGenerated = 0;
  let totalAudioMapUpdates = 0;

  for (const file of files) {
    const result = await processStudent(file);
    if (result) {
      allResults.push(result);
      totalExercises += result.exercises.length;
      totalMissingListen += result.missingListenButtons.length;
      totalAudioGenerated += result.audioGenerated;
      totalAudioMapUpdates += result.audioMapUpdates.length;
    }
  }

  // Summary
  console.log('\n' + '='.repeat(60));
  console.log('SUMMARY');
  console.log('='.repeat(60));
  console.log(`Students with ordering exercises: ${allResults.length}`);
  console.log(`Total ordering exercises: ${totalExercises}`);
  console.log(`Audio files generated: ${totalAudioGenerated}`);
  console.log(`Missing Listen buttons: ${totalMissingListen}`);
  console.log(`AudioMap entries needing update: ${totalAudioMapUpdates}`);

  if (totalMissingListen > 0) {
    console.log('\n--- FILES NEEDING LISTEN BUTTONS ---');
    for (const r of allResults) {
      if (r.missingListenButtons.length > 0) {
        console.log(`  ${r.slug}: ${r.missingListenButtons.join(', ')}`);
      }
    }
  }

  if (totalAudioMapUpdates > 0) {
    console.log('\n--- AUDIOMAP ENTRIES NEEDING UPDATE ---');
    for (const r of allResults) {
      for (const u of r.audioMapUpdates) {
        console.log(`  ${r.slug}: ${u.key} -> "${u.value}" (was: "${u.oldValue || 'MISSING'}")`);
      }
    }
  }

  // Write report JSON for use by the fix script
  const reportPath = path.join(__dirname, 'ordering-audit-report.json');
  fs.writeFileSync(reportPath, JSON.stringify(allResults, null, 2));
  console.log(`\nReport saved to: ${reportPath}`);
}

main().catch(err => { console.error(err); process.exit(1); });
