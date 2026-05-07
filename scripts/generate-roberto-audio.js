#!/usr/bin/env node
/**
 * Generate ElevenLabs MP3 audios for Roberto Pires — Lessons 1-5 (Block 1).
 * Reads scripts/roberto-audio-list.json (built by build-roberto-audio-list.js).
 *
 * Usage (PowerShell):
 *   $env:ELEVENLABS_API_KEY = "sk_..."
 *   node scripts/generate-roberto-audio.js
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
  arthur: 'pNInz6obpgDQGcFmaJgB',
  ellen:  'CwhRBWXzGAHq8TQ4Fs17',
};
const MODEL_ID = 'eleven_multilingual_v2';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');
const LIST_PATH = path.join(__dirname, 'roberto-audio-list.json');

if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const list = JSON.parse(fs.readFileSync(LIST_PATH, 'utf8'));

function tts(text, voiceId) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text,
      model_id: MODEL_ID,
      voice_settings: { stability: 0.5, similarity_boost: 0.75 },
    });
    const req = https.request({
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'xi-api-key': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
        'Content-Length': Buffer.byteLength(data),
      },
    }, (res) => {
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => {
        if (res.statusCode !== 200) {
          return reject(new Error(`HTTP ${res.statusCode}: ${Buffer.concat(chunks).toString()}`));
        }
        resolve(Buffer.concat(chunks));
      });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  console.log(`Generating ${list.length} audios in ${OUTPUT_DIR}...`);
  let ok = 0, skip = 0, fail = 0;
  for (let i = 0; i < list.length; i++) {
    const item = list[i];
    const out = path.join(OUTPUT_DIR, item.filename);
    if (fs.existsSync(out) && fs.statSync(out).size > 1000) {
      skip++;
      continue;
    }
    try {
      const buf = await tts(item.text, VOICES[item.voice]);
      fs.writeFileSync(out, buf);
      ok++;
      if (i % 10 === 0 || i === list.length - 1) {
        console.log(`  [${i + 1}/${list.length}] ok=${ok} skip=${skip} fail=${fail}`);
      }
    } catch (e) {
      fail++;
      console.error(`  FAIL ${item.filename}: ${e.message}`);
    }
    // Soft rate-limit pause
    await new Promise(r => setTimeout(r, 250));
  }
  console.log(`Done. ok=${ok} skip=${skip} fail=${fail}`);
}

main().catch((e) => { console.error(e); process.exit(1); });
