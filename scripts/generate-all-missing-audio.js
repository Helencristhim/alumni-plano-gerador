const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = path.join(__dirname, '..', 'public');

if (!API_KEY) { console.error('ELEVENLABS_API_KEY not set'); process.exit(1); }

// Read all missing entries from both HTML files
const files = [
  path.join(BASE_DIR, 'professor', 'maisa-de-oliveira-santos.html'),
  path.join(BASE_DIR, 'aluno', 'maisa-de-oliveira-santos.html')
];

const allMissing = new Map();

files.forEach(file => {
  const html = fs.readFileSync(file, 'utf8');
  const match = html.match(/var audioMap = ({[\s\S]*?});/);
  const map = JSON.parse(match[1]);
  Object.entries(map).forEach(([text, relPath]) => {
    const fullPath = path.join(BASE_DIR, relPath);
    if (!fs.existsSync(fullPath) && !allMissing.has(text)) {
      allMissing.set(text, fullPath);
    }
  });
});

console.log(`Total missing audio files: ${allMissing.size}\n`);

function chooseVoice(text) {
  // Single words → Arthur (vocab/drilling)
  if (!text.includes(' ')) return ARTHUR_ID;
  // Sentences starting with I/My/We → Ellen (student perspective)
  if (/^(I |I'|My |We |Our |She )/.test(text)) return ELLEN_ID;
  // Questions → Arthur
  if (text.endsWith('?')) return ARTHUR_ID;
  // Default alternate based on hash
  const hash = text.split('').reduce((a, c) => a + c.charCodeAt(0), 0);
  return hash % 2 === 0 ? ARTHUR_ID : ELLEN_ID;
}

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true }
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
        res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body.slice(0, 200)}`)));
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
  const entries = Array.from(allMissing.entries());
  let generated = 0, failed = 0, skipped = 0;

  for (let i = 0; i < entries.length; i++) {
    const [text, filepath] = entries[i];

    // Ensure directory exists
    const dir = path.dirname(filepath);
    if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });

    // Skip if somehow exists now
    if (fs.existsSync(filepath)) { skipped++; continue; }

    const voiceId = chooseVoice(text);
    const voiceName = voiceId === ELLEN_ID ? 'Ellen' : 'Arthur';

    try {
      process.stdout.write(`[${i+1}/${entries.length}] (${voiceName}) ${text.slice(0, 60)}...`);
      const buf = await generateAudio(text, voiceId);
      fs.writeFileSync(filepath, buf);
      generated++;
      console.log(` OK ${(buf.length/1024).toFixed(0)}KB`);
      await new Promise(r => setTimeout(r, 120));
    } catch (err) {
      console.log(` FAIL: ${err.message.slice(0, 80)}`);
      // Retry once
      try {
        await new Promise(r => setTimeout(r, 5000));
        const buf = await generateAudio(text, voiceId);
        fs.writeFileSync(filepath, buf);
        generated++;
        console.log(`  Retry OK`);
      } catch (e2) {
        failed++;
        console.log(`  Retry FAIL`);
      }
      await new Promise(r => setTimeout(r, 2000));
    }
  }

  console.log(`\n===== DONE =====`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped: ${skipped}`);
  console.log(`Failed: ${failed}`);
}

main().catch(console.error);
