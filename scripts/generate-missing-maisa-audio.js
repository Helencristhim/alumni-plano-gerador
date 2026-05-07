const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_VOICE_ID = 'pNInz6obpgDQGcFmaJgB';
const ELLEN_VOICE_ID = 'CwhRBWXzGAHq8TQ4Fs17';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'maisa-de-oliveira-santos');
const MAP_PATH = path.join(OUTPUT_DIR, 'audioMap.json');

if (!API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY not set');
  process.exit(1);
}

// All missing phrases extracted from the new HTML audioMap
const MISSING_PHRASES = [
  // Single words (use Arthur voice)
  { text: "nationality", voice: "arthur" },
  { text: "colleague", voice: "arthur" },
  { text: "executive", voice: "arthur" },
  { text: "introduce", voice: "arthur" },
  { text: "travel", voice: "arthur" },
  { text: "appointment", voice: "arthur" },
  { text: "quarter", voice: "arthur" },
  { text: "figure", voice: "arthur" },
  { text: "rate", voice: "arthur" },
  { text: "growth", voice: "arthur" },
  { text: "approximately", voice: "arthur" },
  { text: "friendly", voice: "arthur" },
  { text: "professional", voice: "arthur" },
  { text: "experienced", voice: "arthur" },
  { text: "direct", voice: "arthur" },
  { text: "reliable", voice: "arthur" },
  { text: "strategic", voice: "arthur" },
  { text: "easygoing", voice: "arthur" },
  { text: "describe", voice: "arthur" },

  // Sentences - alternate Arthur and Ellen
  { text: "My name is Maisa.", voice: "ellen" },
  { text: "I live in Sao Paulo.", voice: "ellen" },
  { text: "I am 35 years old.", voice: "ellen" },
  { text: "I'm 35 years old.", voice: "ellen" },
  { text: "She works at a financial firm.", voice: "arthur" },
  { text: "I feel nervous when I speak English.", voice: "ellen" },
  { text: "Where are you from?", voice: "arthur" },
  { text: "What do you do?", voice: "arthur" },
  { text: "I'm based in Sao Paulo.", voice: "ellen" },
  { text: "I am based in Sao Paulo.", voice: "ellen" },
  { text: "He is from the United States.", voice: "arthur" },
  { text: "She is my colleague from the finance team.", voice: "ellen" },
  { text: "David is an executive at our firm.", voice: "arthur" },
  { text: "The investment market is changing.", voice: "arthur" },
  { text: "Our firm has offices in two countries.", voice: "ellen" },
  { text: "Let me introduce my team.", voice: "ellen" },
  { text: "Our office is in the financial district.", voice: "arthur" },
  { text: "My team has five people.", voice: "ellen" },
  { text: "I handle international accounts.", voice: "ellen" },
  { text: "The report is due on Friday.", voice: "arthur" },
  { text: "I deal with complex transactions.", voice: "ellen" },
  { text: "I have an appointment at 10 AM.", voice: "ellen" },
  { text: "The quarterly revenue was 2.3 million.", voice: "arthur" },
  { text: "The exchange rate is approximately five to one.", voice: "arthur" },
  { text: "Annual growth was around 8 percent.", voice: "arthur" },
  { text: "The interest rate went up.", voice: "arthur" },
  { text: "We need the figures by Thursday.", voice: "ellen" },
  { text: "My manager is friendly and experienced.", voice: "ellen" },
  { text: "She is reliable and strategic.", voice: "arthur" },
  { text: "He is always busy but easygoing.", voice: "arthur" },
  { text: "Can you describe your colleague?", voice: "ellen" },
  { text: "He travels to Sao Paulo every quarter.", voice: "arthur" },
  { text: "My name is Maisa. I work in finance. Nice to meet you.", voice: "ellen" },
  { text: "I'm from Brazil. I'm based in Sao Paulo.", voice: "ellen" },
  { text: "I manage client portfolios at our firm.", voice: "ellen" },
  { text: "The meeting is at 2:30 PM. We have around 80 clients.", voice: "ellen" },
  { text: "He is very professional and experienced.", voice: "arthur" },
  { text: "How are you?", voice: "arthur" },
  { text: "Good morning!", voice: "arthur" },
  { text: "My office is on the third floor.", voice: "ellen" },
];

function sanitizeFilename(text) {
  return text.toLowerCase()
    .replace(/[áàâã]/g, 'a')
    .replace(/[éèê]/g, 'e')
    .replace(/[íì]/g, 'i')
    .replace(/[óòôõ]/g, 'o')
    .replace(/[úù]/g, 'u')
    .replace(/ç/g, 'c')
    .replace(/[^a-z0-9\s]/g, '_')
    .replace(/\s+/g, '_')
    .replace(/_+/g, '_')
    .replace(/^_|_$/g, '')
    + '.mp3';
}

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75,
        style: 0.0,
        use_speaker_boost: true
      }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Content-Length': Buffer.byteLength(data)
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode === 429) {
        console.log('  Rate limited, waiting 30s...');
        setTimeout(() => resolve(generateAudio(text, voiceId)), 30000);
        return;
      }

      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', chunk => body += chunk);
        res.on('end', () => {
          reject(new Error(`HTTP ${res.statusCode}: ${body}`));
        });
        return;
      }

      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  // Load existing audioMap
  let audioMap = {};
  if (fs.existsSync(MAP_PATH)) {
    audioMap = JSON.parse(fs.readFileSync(MAP_PATH, 'utf8'));
  }

  console.log(`Generating ${MISSING_PHRASES.length} missing audio files...\n`);
  let generated = 0;
  let skipped = 0;
  let failed = 0;

  for (let i = 0; i < MISSING_PHRASES.length; i++) {
    const { text, voice } = MISSING_PHRASES[i];
    const filename = sanitizeFilename(text);
    const filepath = path.join(OUTPUT_DIR, filename);
    const relPath = `/audio/maisa-de-oliveira-santos/${filename}`;

    if (fs.existsSync(filepath)) {
      console.log(`[${i+1}/${MISSING_PHRASES.length}] SKIP (exists): ${text}`);
      audioMap[text] = relPath;
      skipped++;
      continue;
    }

    const voiceId = voice === 'ellen' ? ELLEN_VOICE_ID : ARTHUR_VOICE_ID;
    const voiceName = voice === 'ellen' ? 'Ellen' : 'Arthur';

    try {
      console.log(`[${i+1}/${MISSING_PHRASES.length}] Generating (${voiceName}): ${text}`);
      const audioBuffer = await generateAudio(text, voiceId);
      fs.writeFileSync(filepath, audioBuffer);
      audioMap[text] = relPath;
      generated++;
      console.log(`  OK - ${(audioBuffer.length / 1024).toFixed(1)}KB`);

      // Rate limit: 150ms between requests
      await new Promise(r => setTimeout(r, 150));
    } catch (err) {
      console.error(`  FAILED: ${err.message}`);
      failed++;

      // Retry once after 5s
      try {
        await new Promise(r => setTimeout(r, 5000));
        console.log(`  Retrying: ${text}`);
        const audioBuffer = await generateAudio(text, voiceId);
        fs.writeFileSync(filepath, audioBuffer);
        audioMap[text] = relPath;
        generated++;
        failed--;
        console.log(`  OK (retry) - ${(audioBuffer.length / 1024).toFixed(1)}KB`);
      } catch (retryErr) {
        console.error(`  RETRY FAILED: ${retryErr.message}`);
      }

      await new Promise(r => setTimeout(r, 2000));
    }
  }

  // Save updated audioMap
  fs.writeFileSync(MAP_PATH, JSON.stringify(audioMap, null, 2));

  console.log(`\n===== SUMMARY =====`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped (existing): ${skipped}`);
  console.log(`Failed: ${failed}`);
  console.log(`Total in audioMap: ${Object.keys(audioMap).length}`);
  console.log(`audioMap saved to: ${MAP_PATH}`);
}

main().catch(console.error);
