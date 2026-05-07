#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICE_ID = 'pNInz6obpgDQGcFmaJgB';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'daniela-feitoza');

const missing = [
  "Centauro is the market leader in sportswear.",
  "Great conference, isn't it?",
  "Great event, isn't it?",
  "Hi! I'm Daniela, an IT Manager from Brazil. I'm here to learn about new SAP solutions for our retail operations.",
  "Hi, I'm Daniela. I'm an IT Manager at SPF Group.",
  "Hi, I'm Daniela. Nice to meet you.",
  "I manage the IT department.",
  "I need a new server for the project.",
  "I oversee all technology projects.",
  "I work at the SPF Group.",
  "I work at the SPF Group. It's a large distributor in Brazil.",
  "I'm based in Sao Paulo and I'm responsible for SAP implementation.",
  "It was great talking to you. Let's keep in touch.",
  "Nice to meet you.",
  "She is an experienced IT manager.",
  "Sorry, could you say that again?",
  "That's really interesting. Tell me more.",
  "The IT department has an important role in the company.",
  "The conference starts at 9 AM.",
  "We work in the retail industry.",
  "What do you do?",
  "Where are you from?",
  "Centauro is the market leader in sportswear retail in Brazil. We are the only retailer with an exclusive Nike partnership. Our technology infrastructure, including SAP, is one of the most advanced in the industry."
];

function textToFilename(t) {
  return t.toLowerCase().replace(/[^a-z0-9\s]/g, '').replace(/\s+/g, '_').substring(0, 60) + '.mp3';
}

async function gen(text, filename) {
  const fp = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(fp) && fs.statSync(fp).size > 1000) { console.log(`  [skip] ${filename}`); return fp; }
  const r = await fetch(`${API_URL}/${VOICE_ID}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Accept': 'audio/mpeg' },
    body: JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
  });
  if (!r.ok) { console.error(`  [ERR] ${r.status}`); return null; }
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(fp, buf);
  console.log(`  [ok] ${filename} (${buf.length}b)`);
  return fp;
}

async function main() {
  console.log(`Generating ${missing.length} missing audio files...`);
  const entries = [];
  for (let i = 0; i < missing.length; i++) {
    const t = missing[i];
    const fn = textToFilename(t);
    console.log(`[${i+1}/${missing.length}] "${t.substring(0,50)}"`);
    const r = await gen(t, fn);
    if (r) entries.push(`        "${t.replace(/"/g, '\\"')}": "/audio/daniela-feitoza/${fn}"`);
    if (i < missing.length - 1) await new Promise(r => setTimeout(r, 150));
  }
  console.log('\n--- Add these to audioMap ---');
  console.log(entries.join(',\n'));
  fs.writeFileSync('/tmp/missing-audiomap-entries.txt', entries.join(',\n'));
}
main().catch(console.error);
