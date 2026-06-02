/**
 * generate-all-ordering-audio.js
 *
 * Generates ElevenLabs audio for ALL ordering exercises.
 * Extracts sentences from HTML in correct data-order, generates MP3.
 *
 * Voices: Riley (women), Ash (men)
 *
 * Usage:
 *   node scripts/generate-all-ordering-audio.js
 *   node scripts/generate-all-ordering-audio.js --dry-run
 *   node scripts/generate-all-ordering-audio.js --student=carlos-vinicius-vale-bassan
 *   node scripts/generate-all-ordering-audio.js --missing-only  (skip if MP3 exists)
 */

const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const RILEY_ID = 'hA4zGnmTwX2NQiTRMt7o';  // Female neutral
const ASH_ID = 'VU16byTywsWv5JpI8rbc';      // Male neutral

const ALUNO_DIR = path.join(__dirname, '..', 'public', 'aluno');
const AUDIO_BASE = path.join(__dirname, '..', 'public', 'audio');

const DRY_RUN = process.argv.includes('--dry-run');
const MISSING_ONLY = process.argv.includes('--missing-only');
const STUDENT_FILTER = process.argv.find(a => a.startsWith('--student='));
const SPECIFIC_STUDENT = STUDENT_FILTER ? STUDENT_FILTER.split('=')[1] : null;

const GENDER_MAP = {
  'vanessa-maluf': 'F', 'tuca-dias': 'M', 'tania-rosa': 'F',
  'simone-quiles-de-santana-marques': 'F', 'rubens-tofolo': 'M',
  'roberto-rezende': 'M', 'roberto-pires': 'M', 'rafael-gasparelli-lima': 'M',
  'percival-jr': 'M', 'patricia-ruffo': 'F', 'natalie-viegas': 'F',
  'milton-sayegh': 'M', 'marlene-landucci': 'F', 'mark-kazuyoshi-seki-omagari': 'M',
  'maria-claudia-curimbaba': 'F', 'maisa-de-oliveira-santos': 'F',
  'luiz-bressane': 'M', 'karina-macedo': 'F',
  'gleice-leonardo-rocha-de-souza': 'F', 'gabriela-pires': 'F',
  'gabriela-paulucci': 'F', 'elaine-mieko-pinho': 'F',
  'eduardo-chiba': 'M', 'eduarda-gabriel': 'F', 'diogo-leal': 'M',
  'daniela-feitoza': 'F', 'dienane-brandao-de-mesquita': 'F',
  'carolina-paludetto-rodrigues': 'F', 'carlos-vinicius-vale-bassan': 'M',
  'andreia-heins': 'F', 'aline-sberci': 'F', 'zilaudio': 'F',
  'pricila-adamo': 'F'
};

function getBaseSlug(slug) {
  return slug.replace(/-aula\d+$/, '').replace(/-backup-a2$/, '');
}

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
    .replace(/&lsquo;/g, "'")
    .replace(/&rsquo;/g, "'")
    .replace(/&mdash;/g, '—')
    .replace(/&ndash;/g, '–')
    .replace(/\u201c/g, '')
    .replace(/\u201d/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

function extractExercises(html) {
  const exercises = [];
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

    if (items.length === 0) continue; // Skip broken HTML

    const correctText = items.map(i => i.text).join(' ');
    const audioFile = containerId.replace(/-/g, '_') + '_ordering.mp3';

    // Get current audioMap path
    const audioMapRegex = new RegExp(`"\\[${containerId}\\]"\\s*:\\s*"([^"]+)"`);
    const audioMapMatch = audioMapRegex.exec(html);
    const currentPath = audioMapMatch ? audioMapMatch[1] : null;

    exercises.push({ containerId, items, correctText, audioFile, currentPath });
  }

  return exercises;
}

async function generateAudio(text, voiceId, outputPath) {
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
    throw new Error(`ElevenLabs ${resp.status}: ${err.substring(0, 200)}`);
  }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  if (!DRY_RUN && !API_KEY) {
    console.error('Set ELEVENLABS_API_KEY or use --dry-run');
    process.exit(1);
  }

  const files = fs.readdirSync(ALUNO_DIR)
    .filter(f => f.endsWith('.html'))
    .filter(f => {
      if (!SPECIFIC_STUDENT) return true;
      const slug = f.replace('.html', '');
      return slug === SPECIFIC_STUDENT || getBaseSlug(slug) === SPECIFIC_STUDENT;
    })
    .sort();

  let totalGenerated = 0;
  let totalSkipped = 0;
  let totalErrors = 0;
  let totalExercises = 0;

  for (const file of files) {
    const slug = file.replace('.html', '');
    const baseSlug = getBaseSlug(slug);
    const gender = GENDER_MAP[baseSlug] || 'F';
    const voiceId = gender === 'M' ? ASH_ID : RILEY_ID;
    const voiceName = gender === 'M' ? 'Ash' : 'Riley';

    const html = fs.readFileSync(path.join(ALUNO_DIR, file), 'utf-8');
    const exercises = extractExercises(html);
    if (exercises.length === 0) continue;

    const audioDir = path.join(AUDIO_BASE, baseSlug);

    console.log(`\n${slug} (${voiceName}) — ${exercises.length} exercises`);

    for (const ex of exercises) {
      totalExercises++;
      const outputPath = path.join(audioDir, ex.audioFile);

      // Skip if MP3 exists and --missing-only
      if (MISSING_ONLY && fs.existsSync(outputPath)) {
        console.log(`  SKIP (exists): ${ex.containerId}`);
        totalSkipped++;
        continue;
      }

      // Also check the current audioMap path
      if (MISSING_ONLY && ex.currentPath) {
        const currentFullPath = path.join(__dirname, '..', 'public', ex.currentPath);
        if (fs.existsSync(currentFullPath)) {
          console.log(`  SKIP (exists at ${path.basename(ex.currentPath)}): ${ex.containerId}`);
          totalSkipped++;
          continue;
        }
      }

      console.log(`  ${ex.containerId}: "${ex.correctText.substring(0, 60)}..."`);

      if (DRY_RUN) {
        console.log(`    [DRY] Would generate: ${ex.audioFile}`);
        totalGenerated++;
        continue;
      }

      if (!fs.existsSync(audioDir)) fs.mkdirSync(audioDir, { recursive: true });

      try {
        const bytes = await generateAudio(ex.correctText, voiceId, outputPath);
        console.log(`    Generated: ${ex.audioFile} (${bytes} bytes)`);
        totalGenerated++;
        // Rate limit
        await new Promise(r => setTimeout(r, 600));
      } catch (err) {
        console.error(`    ERROR: ${err.message}`);
        totalErrors++;
      }
    }
  }

  console.log('\n' + '='.repeat(50));
  console.log(`Total: ${totalExercises} exercises`);
  console.log(`Generated: ${totalGenerated}, Skipped: ${totalSkipped}, Errors: ${totalErrors}`);
}

main().catch(err => { console.error(err); process.exit(1); });
