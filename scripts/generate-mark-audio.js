#!/usr/bin/env node
/**
 * Generate ElevenLabs MP3 audios for Mark Kazuyoshi Seki Omagari — Aula 1.
 * Extracts every speakText('...') argument and data-phrase value from the
 * authored fragments, assigns voice (dialogue by data-voice; student/vocab = Arthur;
 * Emma/Sofia = Ellen), generates MP3s, and writes _mark-audiomap.json.
 *
 * Usage:  ELEVENLABS_API_KEY=sk_... node scripts/generate-mark-audio.js
 */
const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: set ELEVENLABS_API_KEY'); process.exit(1); }

const VOICES = { arthur: 'sfJopaWaOtauCD3HKX6Q', ellen: 'BIvP0GN1cAtSRTxNHnWS' };
const MODEL_ID = 'eleven_multilingual_v2';
const ROOT = path.join(__dirname, '..');
const SLUG = 'mark-kazuyoshi-seki-omagari';
const OUT_DIR = path.join(ROOT, 'public', 'audio', SLUG);
const FRAGMENTS = ['_mark-maincontent.html', '_mark-slides.html'].map(f => path.join(ROOT, f));
if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

// ---- extraction ----
// Decode the HTML entities that the browser decodes at runtime, so audioMap keys
// and TTS text match exactly what speakText() receives in the page.
function decode(s) {
  return s
    .replace(/&quot;/g, '"').replace(/&#0?39;/g, "'").replace(/&apos;/g, "'")
    .replace(/&iacute;/g, 'í').replace(/&atilde;/g, 'ã').replace(/&aacute;/g, 'á')
    .replace(/&eacute;/g, 'é').replace(/&ecirc;/g, 'ê').replace(/&oacute;/g, 'ó')
    .replace(/&ocirc;/g, 'ô').replace(/&ccedil;/g, 'ç').replace(/&uacute;/g, 'ú')
    .replace(/&agrave;/g, 'à').replace(/&atilde;/g, 'ã').replace(/&amp;/g, '&');
}
function unesc(s) { return decode(s.replace(/\\'/g, "'").replace(/\\"/g, '"')); }
const phrases = new Map();            // phrase -> voice
function add(phrase, voice) {
  phrase = phrase.trim();
  if (!phrase) return;
  if (!phrases.has(phrase)) phrases.set(phrase, voice);
}

// speakText(...) handling BOTH ' and " delimiters (after entity decode)
function speakArgs(html) {
  const out = [];
  const re = /speakText\(\s*(['"])((?:\\.|(?!\1).)*)\1/g; let m;
  while ((m = re.exec(html))) out.push(unesc(m[2]));
  return out;
}

// 1) Dialogue voices FIRST (authoritative): one block per dialogue-line.
let combined = '';
for (const fp of FRAGMENTS) combined += fs.readFileSync(fp, 'utf8');
const dec = decode(combined);
{
  const blocks = dec.split('<div class="dialogue-line"');
  for (let i = 1; i < blocks.length; i++) {
    const b = blocks[i];
    const vm = b.match(/data-voice="([a-z]+)"/);
    const sp = speakArgs(b.slice(0, b.indexOf('</div></div>') > -1 ? b.indexOf('</div></div>') + 12 : 400));
    if (vm && sp.length) phrases.set(sp[0].trim(), vm[1] === 'ellen' ? 'ellen' : 'arthur');
  }
}
// 2) Everything else as Arthur (add() won't override the dialogue assignments above).
for (const raw of [combined]) {
  const html = decode(raw);
  let m;
  const dq = /data-phrase="([^"]*)"/g;  while ((m = dq.exec(html))) add(m[1].trim(), 'arthur');
  const sq = /data-phrase='([^']*)'/g;  while ((m = sq.exec(html))) add(m[1].trim(), 'arthur');
  for (const p of speakArgs(html)) add(p, 'arthur');
}

// ---- two single-MP3 listenings (sound-first) ----
const LISTENINGS = [
  { file: 'aula1_listening1.mp3', voice: 'arthur',
    text: "Hello! My name is Daniel. I am twelve years old. I live in Lisbon, Portugal. I go to school every morning, and I play basketball after class. My favorite game is Minecraft. On weekends, I watch movies with my family." },
  { file: 'aula1_listening2.mp3', voice: 'ellen',
    text: "Hi, I'm Sofia. I'm thirteen years old and I'm from Argentina. I love languages and I want to meet new people. I study English and I play volleyball. What about you?" },
];

// ---- filename ----
const used = new Set();
function fname(phrase) {
  let base = phrase.toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '').slice(0, 56) || 'audio';
  let f = base + '.mp3', i = 2;
  while (used.has(f)) { f = base + '_' + (i++) + '.mp3'; }
  used.add(f); return f;
}

function tts(text, voiceId) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({ text, model_id: MODEL_ID, voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const req = https.request({ hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voiceId}`, method: 'POST',
      headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg', 'Content-Length': Buffer.byteLength(data) } },
      (res) => { const c = []; res.on('data', d => c.push(d)); res.on('end', () => res.statusCode === 200 ? resolve(Buffer.concat(c)) : reject(new Error('HTTP ' + res.statusCode + ': ' + Buffer.concat(c).toString().slice(0, 200)))); });
    req.on('error', reject); req.write(data); req.end();
  });
}

async function main() {
  const audioMap = {};
  const items = [...phrases.entries()].map(([text, voice]) => ({ text, voice, file: fname(text), map: true }));
  for (const l of LISTENINGS) items.push({ text: l.text, voice: l.voice, file: l.file, map: false });
  console.log(`Generating ${items.length} audios (${phrases.size} phrases + ${LISTENINGS.length} listenings) in ${OUT_DIR}`);
  let ok = 0, skip = 0, fail = 0;
  for (let i = 0; i < items.length; i++) {
    const it = items[i];
    const out = path.join(OUT_DIR, it.file);
    const rel = `/audio/${SLUG}/${it.file}`;
    if (it.map) audioMap[it.text] = rel;
    if (fs.existsSync(out) && fs.statSync(out).size > 1000) { skip++; continue; }
    try { fs.writeFileSync(out, await tts(it.text, VOICES[it.voice])); ok++; }
    catch (e) { fail++; console.error('  FAIL', it.file, e.message); }
    if (i % 10 === 0 || i === items.length - 1) console.log(`  [${i + 1}/${items.length}] ok=${ok} skip=${skip} fail=${fail}`);
    await new Promise(r => setTimeout(r, 220));
  }
  fs.writeFileSync(path.join(ROOT, '_mark-audiomap.json'), JSON.stringify(audioMap, null, 2));
  console.log(`Done. ok=${ok} skip=${skip} fail=${fail}. audioMap entries=${Object.keys(audioMap).length} -> _mark-audiomap.json`);
}
main();
