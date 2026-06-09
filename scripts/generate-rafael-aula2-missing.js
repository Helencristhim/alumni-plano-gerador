#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = { ash: 'VU16byTywsWv5JpI8rbc', riley: 'hA4zGnmTwX2NQiTRMt7o' };
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-de-andrade-brandao');

// Extract audioMap from HTML to get text↔filename mapping
const html = fs.readFileSync(path.join(__dirname, '..', 'public', 'professor', 'rafael-de-andrade-brandao-aula2.html'), 'utf8');
const mapMatch = html.match(/var audioMap = \{([\s\S]*?)\};/);
if (!mapMatch) { console.error('Could not find audioMap'); process.exit(1); }

const entries = [];
const lines = mapMatch[1].split('\n');
for (const line of lines) {
  const m = line.match(/"([^"]+)":\s*"\/audio\/rafael-de-andrade-brandao\/([^"]+)"/);
  if (m) entries.push({ text: m[1], file: m[2] });
}

// Determine voice: dialogue ana=riley, rafael=ash, general alternate
let altToggle = false;
const phrases = entries.filter(e => !fs.existsSync(path.join(OUTPUT_DIR, e.file))).map(e => {
  let voice;
  if (e.file.includes('dia_ana') || e.file.includes('_ana_')) voice = VOICES.riley;
  else if (e.file.includes('dia_rafael') || e.file.includes('_rafael_')) voice = VOICES.ash;
  else if (e.file.includes('listening_intro') || e.file.includes('listening1')) voice = VOICES.ash;
  else if (e.file.includes('listening_meeting') || e.file.includes('listening2')) voice = VOICES.riley;
  else { voice = altToggle ? VOICES.riley : VOICES.ash; altToggle = !altToggle; }
  return { text: e.text, file: e.file, voice };
});

async function gen(text, voiceId, outPath) {
  const r = await fetch(API_URL + '/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()).substring(0, 200));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  console.log('Missing: ' + phrases.length + ' files');
  let ok = 0, fail = 0;
  for (const p of phrases) {
    const out = path.join(OUTPUT_DIR, p.file);
    try {
      const sz = await gen(p.text, p.voice, out);
      ok++;
      console.log('  OK: ' + p.file + ' (' + Math.round(sz/1024) + 'KB)');
      await new Promise(r => setTimeout(r, 500));
    } catch(e) {
      fail++;
      console.error('  FAIL: ' + p.file + ' - ' + e.message);
    }
  }
  console.log('\nDone! OK: ' + ok + ', FAIL: ' + fail);
}
main();
