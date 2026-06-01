#!/usr/bin/env node
/* Andreia Heins — Aula 1. Extrai frases speakText do professor/andreia-heins.html,
   monta audioMap e gera MP3s (Arthur/Ellen) + os 2 listenings. Idempotente. */
const https = require('https');
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q'; // male
const ELLEN  = 'BIvP0GN1cAtSRTxNHnWS'; // female
const MODEL_ID = 'eleven_multilingual_v2';
const SLUG = 'andreia-heins';
const ROOT = __dirname;
const OUT_DIR = path.join(ROOT, 'public', 'audio', SLUG);
fs.mkdirSync(OUT_DIR, { recursive: true });

const ENTITIES = {
  '&quot;': '"', '&amp;': '&', '&#39;': "'", '&apos;': "'",
  '&atilde;': 'ã', '&otilde;': 'õ', '&ccedil;': 'ç',
  '&aacute;': 'á', '&eacute;': 'é', '&iacute;': 'í', '&oacute;': 'ó', '&uacute;': 'ú',
  '&acirc;': 'â', '&ecirc;': 'ê', '&ocirc;': 'ô', '&agrave;': 'à',
};
function decode(s) { return s.replace(/&[a-zA-Z#0-9]+;/g, m => ENTITIES[m] !== undefined ? ENTITIES[m] : m); }
function safeName(text) {
  let n = text.toLowerCase().replace(/['’]/g, '').replace(/[^a-z0-9]+/g, '_').replace(/^_+|_+$/g, '');
  if (n.length > 50) n = n.substring(0, 50).replace(/_+$/, '');
  return n + '.mp3';
}

// ---- Extract phrases from professor file ----
const SRC = path.join(ROOT, 'public', 'professor', 'andreia-heins.html');
const html = fs.readFileSync(SRC, 'utf8');
const phrases = new Set();
const re = /speakText\((.*?),\s*this\)/g;
let m;
while ((m = re.exec(html)) !== null) {
  let arg = m[1].trim();
  if (arg.startsWith("'") && arg.endsWith("'")) arg = arg.slice(1, -1);
  else if (arg.startsWith('"') && arg.endsWith('"')) arg = arg.slice(1, -1);
  arg = decode(arg);
  if (arg.startsWith('[') ) continue;       // skip placeholders like [order-l1]
  if (!arg) continue;
  phrases.add(arg);
}
// Also data-phrase="..." (read by speakPhrase / listenBlank) — these need MP3s too
const reDP = /data-phrase="([^"]*)"/g;
while ((m = reDP.exec(html)) !== null) {
  const arg = decode(m[1].trim());
  if (arg && !arg.startsWith('[')) phrases.add(arg);
}

// ---- Arthur (male) phrases: Mark / Medtronic rep lines ----
const ARTHUR_PHRASES = new Set([
  // Aula 1 — Mark (Medtronic rep)
  "Hi Andreia, thanks for joining. Could you introduce yourself?",
  "Great. What are you responsible for now?",
  "Perfect. So you are our main stakeholder for this project?",
  "Wonderful. Let us walk you through the system.",
  // Aula 2 — Dr. Alan (colleague)
  "Andreia, I would love to hear your story. How did you start in nursing?",
  "The ICU is tough. What did you do there?",
  "Impressive. And how did you move into robotic surgery?",
  "That is a big milestone. What was the hardest part?",
  // Aula 3 — Tom (new team member)
  "Andreia, what does a normal day look like for you?",
  "And then? What do you usually do?",
  "Do you report to anyone?",
  "What is your top priority?",
]);

// ---- Build audioMap ----
const audioMap = {};
const jobs = [];
const usedNames = {};
for (const p of phrases) {
  let fname = safeName(p);
  if (usedNames[fname] && usedNames[fname] !== p) {
    let i = 2; const base = fname.replace(/\.mp3$/, '');
    while (usedNames[base + '_' + i + '.mp3']) i++;
    fname = base + '_' + i + '.mp3';
  }
  usedNames[fname] = p;
  audioMap[p] = `/audio/${SLUG}/${fname}`;
  jobs.push({ text: p, file: path.join(OUT_DIR, fname), voice: ARTHUR_PHRASES.has(p) ? ARTHUR : ELLEN });
}

// ---- Listening tracks (data-src, not in audioMap) — fixed filenames matching the HTML ----
const LISTEN1 = "Good afternoon, everyone. My name is Andreia Heins. My background is in nursing, and I currently work at Hospital Albert Einstein in São Paulo. I am responsible for the robotic surgery program, and I deal with international suppliers like Medtronic and Stryker. Last year, I transitioned into robotic surgery, and I am excited about this new chapter.";
const LISTEN2 = "Hi Andreia, thank you for joining the call. Before we start, could you introduce yourself and tell us about your role? Also, who do you usually deal with on your team?";
jobs.push({ text: LISTEN1, file: path.join(OUT_DIR, 'listening1_self_introduction.mp3'), voice: ELLEN });
jobs.push({ text: LISTEN2, file: path.join(OUT_DIR, 'listening2_meeting_opener.mp3'), voice: ARTHUR });

// Aula 2 listenings
const LISTEN3 = "Hello. Let me tell you my career story. I graduated from nursing school in 2008, and I started in the ICU, where I worked the night shift for six years. I specialized in intensive care. During the pandemic, I led a small team and I got promoted to coordinator. My biggest challenge was learning a new system for robotic surgery, but I made it work.";
const LISTEN4 = "Andreia, I would love to understand your journey. Where and when did you start your career? And tell me, what was your biggest challenge along the way, and your proudest achievement?";
jobs.push({ text: LISTEN3, file: path.join(OUT_DIR, 'listening_aula2_career_story.mp3'), voice: ELLEN });
jobs.push({ text: LISTEN4, file: path.join(OUT_DIR, 'listening_aula2_mentor_questions.mp3'), voice: ARTHUR });

// Aula 3 listenings
const LISTEN5 = "Let me tell you about my normal day. My routine starts at seven. I always check my schedule first. I usually coordinate the surgical team in the morning, and I monitor the equipment before every surgery. I report to the medical director, and I often give her updates. Safety is always my top priority, so we never skip the safety check.";
const LISTEN6 = "Andreia, I am new here, so I would love to understand your routine. What time does your day start, and what do you do first? Also, how often do you coordinate the team, and who do you report to?";
jobs.push({ text: LISTEN5, file: path.join(OUT_DIR, 'listening_aula3_routine.mp3'), voice: ELLEN });
jobs.push({ text: LISTEN6, file: path.join(OUT_DIR, 'listening_aula3_colleague_questions.mp3'), voice: ARTHUR });

fs.writeFileSync(path.join(ROOT, '_andreia-audiomap.json'), JSON.stringify(audioMap, null, 2));
console.log('audioMap entries:', Object.keys(audioMap).length);
console.log('total audio jobs (incl. listenings):', jobs.length);
if (process.env.DRY) {
  jobs.forEach(j => console.log((j.voice === ELLEN ? '[E] ' : '[A] ') + j.text.slice(0, 70)));
  process.exit(0);
}

function generate(text, voice) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ text, model_id: MODEL_ID, voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const options = {
      hostname: 'api.elevenlabs.io', port: 443,
      path: `/v1/text-to-speech/${voice}?output_format=mp3_44100_128`,
      method: 'POST',
      headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY },
    };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let b = ''; res.on('data', c => b += c); res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${b}`))); return; }
      const chunks = []; res.on('data', c => chunks.push(c)); res.on('end', () => resolve(Buffer.concat(chunks)));
    });
    req.on('error', reject); req.write(postData); req.end();
  });
}
const sleep = ms => new Promise(r => setTimeout(r, ms));

(async () => {
  let made = 0, skipped = 0, failed = 0;
  for (const j of jobs) {
    if (fs.existsSync(j.file) && fs.statSync(j.file).size > 1000) { skipped++; continue; }
    try {
      const buf = await generate(j.text, j.voice);
      fs.writeFileSync(j.file, buf); made++; process.stdout.write('.'); await sleep(180);
    } catch (e) { failed++; console.error('\nFAIL:', j.text.slice(0, 40), '->', e.message); await sleep(500); }
  }
  console.log(`\nDONE. made=${made} skipped=${skipped} failed=${failed}`);
  if (failed > 0) process.exit(1);
})();
