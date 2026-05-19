#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for ALL speakText phrases in the professor HTML.
 * Rebuilds audioMap.json with correct text->filepath mapping.
 */
const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICE_ID = 'sfJopaWaOtauCD3HKX6Q'; // Arthur
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'daniela-feitoza');

if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

// Read all phrases from the extracted file
const phrasesFile = '/tmp/daniela-all-phrases.txt';
const phrases = fs.readFileSync(phrasesFile, 'utf-8').trim().split('\n').filter(Boolean);

function textToFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9\s]/g, '').replace(/\s+/g, '_').substring(0, 60) + '.mp3';
}

async function generateAudio(text, filename) {
  const filePath = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(filePath) && fs.statSync(filePath).size > 1000) {
    console.log(`  [skip] ${filename} exists (${fs.statSync(filePath).size}b)`);
    return filePath;
  }

  const response = await fetch(`${API_URL}/${VOICE_ID}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'xi-api-key': API_KEY,
      'Accept': 'audio/mpeg'
    },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    })
  });

  if (!response.ok) {
    const err = await response.text();
    console.error(`  [ERROR] ${filename}: ${response.status} ${err.substring(0, 100)}`);
    return null;
  }

  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  console.log(`  [ok] ${filename} (${buffer.length}b)`);
  return filePath;
}

async function main() {
  console.log(`Generating ${phrases.length} audio files...`);
  const audioMap = {};
  let ok = 0, fail = 0;

  for (let i = 0; i < phrases.length; i++) {
    const text = phrases[i];
    const filename = textToFilename(text);
    console.log(`[${i+1}/${phrases.length}] "${text.substring(0, 60)}"`);

    const result = await generateAudio(text, filename);
    if (result) {
      audioMap[text] = `/audio/daniela-feitoza/${filename}`;
      ok++;
    } else {
      fail++;
    }
    if (i < phrases.length - 1) await new Promise(r => setTimeout(r, 150));
  }

  // Save audioMap
  const mapPath = path.join(OUTPUT_DIR, 'audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMap, null, 2));
  console.log(`\nDone! ${ok} ok, ${fail} failed. Map: ${mapPath}`);
}

main().catch(console.error);
