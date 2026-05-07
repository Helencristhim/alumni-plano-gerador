#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICE_ID = 'pNInz6obpgDQGcFmaJgB';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'daniela-feitoza');

if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }

const phrases = fs.readFileSync('/tmp/daniela-all-phrases-v2.txt', 'utf-8').trim().split('\n').filter(Boolean);

function textToFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9\s]/g, '').replace(/\s+/g, '_').substring(0, 60) + '.mp3';
}

async function generateAudio(text, filename) {
  const filePath = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(filePath) && fs.statSync(filePath).size > 1000) {
    console.log(`  [skip] ${filename}`);
    return filePath;
  }
  const response = await fetch(`${API_URL}/${VOICE_ID}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Accept': 'audio/mpeg' },
    body: JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
  });
  if (!response.ok) { console.error(`  [ERR] ${filename}: ${response.status}`); return null; }
  const buffer = Buffer.from(await response.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  console.log(`  [ok] ${filename} (${buffer.length}b)`);
  return filePath;
}

async function main() {
  console.log(`Processing ${phrases.length} phrases...`);
  const audioMap = {};
  let ok = 0, skip = 0, fail = 0;
  for (let i = 0; i < phrases.length; i++) {
    const text = phrases[i];
    const filename = textToFilename(text);
    console.log(`[${i+1}/${phrases.length}] "${text.substring(0, 55)}"`);
    const filePath = path.join(OUTPUT_DIR, filename);
    const existed = fs.existsSync(filePath) && fs.statSync(filePath).size > 1000;
    const result = await generateAudio(text, filename);
    if (result) { audioMap[text] = `/audio/daniela-feitoza/${filename}`; existed ? skip++ : ok++; }
    else fail++;
    if (i < phrases.length - 1 && !existed) await new Promise(r => setTimeout(r, 150));
  }
  fs.writeFileSync(path.join(OUTPUT_DIR, 'audioMap.json'), JSON.stringify(audioMap, null, 2));
  console.log(`\nDone! ${ok} new, ${skip} skipped, ${fail} failed.`);

  // Output the audioMap as JS for embedding in HTML
  const jsLines = Object.entries(audioMap).map(([k,v]) => `        "${k.replace(/"/g, '\\"')}": "${v}"`);
  fs.writeFileSync('/tmp/daniela-audiomap-js.txt', '    const audioMap = {\n' + jsLines.join(',\n') + '\n    };');
  console.log('JS audioMap saved to /tmp/daniela-audiomap-js.txt');
}
main().catch(console.error);
