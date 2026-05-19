const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_VOICE_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_VOICE_ID = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'maisa-de-oliveira-santos');

if (!API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY not set');
  process.exit(1);
}

const MISSING_PHRASES = [
  { text: "Ana is very reliable and direct.", voice: "ellen" },
  { text: "Ricardo is always busy but very friendly.", voice: "arthur" },
  { text: "David is very professional and strategic.", voice: "ellen" },
  { text: "Maísa is confident and strategic.", voice: "arthur" },
  { text: "He is very friendly and supportive.", voice: "ellen" },
  { text: "Our team is strategic and direct.", voice: "arthur" },
  { text: "We deal with complex transactions.", voice: "ellen" },
];

function textToFilename(text) {
  return text.toLowerCase()
    .replace(/[^a-z0-9 ]/g, '')
    .trim()
    .replace(/ +/g, '_')
    .substring(0, 60) + '.mp3';
}

function generateAudio(text, voiceName) {
  return new Promise((resolve, reject) => {
    const voiceId = voiceName === 'arthur' ? ARTHUR_VOICE_ID : ELLEN_VOICE_ID;
    const filename = textToFilename(text);
    const filepath = path.join(OUTPUT_DIR, filename);

    if (fs.existsSync(filepath)) {
      console.log(`SKIP (exists): ${filename}`);
      return resolve();
    }

    const data = JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Accept': 'audio/mpeg'
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', d => body += d);
        res.on('end', () => {
          console.error(`ERROR ${res.statusCode} for "${text}": ${body}`);
          reject(new Error(`HTTP ${res.statusCode}`));
        });
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => {
        fs.writeFileSync(filepath, Buffer.concat(chunks));
        console.log(`OK: ${filename} (${voiceName})`);
        resolve();
      });
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  console.log(`Generating ${MISSING_PHRASES.length} missing audio files...`);
  for (const phrase of MISSING_PHRASES) {
    await generateAudio(phrase.text, phrase.voice);
    await new Promise(r => setTimeout(r, 500)); // rate limit
  }
  console.log('Done!');
}

main().catch(console.error);
