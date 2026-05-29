#!/usr/bin/env node
/**
 * Generate 2 missing ElevenLabs listening exercise MP3s for Roberto Rezende.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=sk_... node scripts/generate-roberto-rezende-listening.js
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) {
  console.error('ERROR: set ELEVENLABS_API_KEY env var first.');
  process.exit(1);
}

const VOICES = {
  arthur: 'sfJopaWaOtauCD3HKX6Q',
  ellen:  'BIvP0GN1cAtSRTxNHnWS',
};
const MODEL_ID = 'eleven_multilingual_v2';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-rezende');

if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const items = [
  {
    file: 'listening1_pipeline_update.mp3',
    voice: 'arthur',
    text: 'Hi Marco, it is Roberto. Just a quick update on the pipeline this week. We have three new clients in the agricultural segment. I am currently working on a proposal for the largest one. The forecast for this quarter looks very promising. I also need to follow up with two accounts from last month. Oh, and I am preparing for the Agrishow trade fair. It is going to be a great opportunity to network. Talk to you later.',
  },
  {
    file: 'listening2_sales_meeting.mp3',
    voice: 'ellen',
    text: 'Good morning, Roberto. Let us start with the pipeline update. How many potential clients do you currently have? And what segments are we focusing on this quarter? I understand you oversee the industrial, agricultural, and generator segments. The headquarters is expecting a detailed forecast by Friday. Can you also follow up with the key accounts from the trade fair? We need to report our progress to Mr. Zhang by the end of the week.',
  },
];

function generate(item) {
  return new Promise((resolve, reject) => {
    const outPath = path.join(OUTPUT_DIR, item.file);
    if (fs.existsSync(outPath)) {
      console.log(`SKIP (exists): ${item.file}`);
      return resolve();
    }

    const voiceId = VOICES[item.voice];
    const body = JSON.stringify({
      text: item.text,
      model_id: MODEL_ID,
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.3 },
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Accept': 'audio/mpeg',
      },
    };

    console.log(`Generating: ${item.file} (${item.voice})...`);

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let errBody = '';
        res.on('data', (d) => errBody += d);
        res.on('end', () => {
          console.error(`ERROR ${res.statusCode} for ${item.file}: ${errBody}`);
          reject(new Error(`HTTP ${res.statusCode}`));
        });
        return;
      }
      const chunks = [];
      res.on('data', (chunk) => chunks.push(chunk));
      res.on('end', () => {
        const buffer = Buffer.concat(chunks);
        fs.writeFileSync(outPath, buffer);
        console.log(`OK: ${item.file} (${(buffer.length / 1024).toFixed(1)} KB)`);
        resolve();
      });
    });

    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

(async () => {
  for (const item of items) {
    await generate(item);
    // Small delay between API calls
    await new Promise(r => setTimeout(r, 500));
  }
  console.log('\nDone! Generated listening audio files for Roberto Rezende.');
})();
