#!/usr/bin/env node
/**
 * Generate ElevenLabs MP3 audios for Mark Kazuyoshi — B2 Aula 1.
 * Reads the professor HTML directly, extracts speakText and data-phrase,
 * assigns voice (dialogue by data-voice; student/vocab = Arthur since Mark is male).
 *
 * Usage:  ELEVENLABS_API_KEY=sk_... node scripts/generate-mark-b2-audio.js
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
const HTML_FILE = path.join(ROOT, 'public', 'professor', SLUG + '.html');

if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });

// ---- decode HTML entities ----
function decode(s) {
  return s
    .replace(/&quot;/g, '"').replace(/&#0?39;/g, "'").replace(/&apos;/g, "'")
    .replace(/&iacute;/g, 'í').replace(/&atilde;/g, 'ã').replace(/&aacute;/g, 'á')
    .replace(/&eacute;/g, 'é').replace(/&ecirc;/g, 'ê').replace(/&oacute;/g, 'ó')
    .replace(/&ocirc;/g, 'ô').replace(/&ccedil;/g, 'ç').replace(/&uacute;/g, 'ú')
    .replace(/&agrave;/g, 'à').replace(/&amp;/g, '&').replace(/&mdash;/g, '—')
    .replace(/&middot;/g, '·').replace(/&hellip;/g, '...');
}
function unesc(s) { return decode(s.replace(/\\'/g, "'").replace(/\\"/g, '"')); }

const phrases = new Map(); // phrase -> voice
function add(phrase, voice) {
  phrase = phrase.trim();
  if (!phrase || phrase.length < 2) return;
  if (!phrases.has(phrase)) phrases.set(phrase, voice);
}

// ---- extraction ----
function speakArgs(html) {
  const out = [];
  const re = /speakText\(\s*(['"])((?:\\.|(?!\1).)*)\1/g; let m;
  while ((m = re.exec(html))) out.push(unesc(m[2]));
  return out;
}

const raw = fs.readFileSync(HTML_FILE, 'utf8');
const dec = decode(raw);

// 1) Dialogue voices FIRST
{
  const blocks = dec.split('dialogue-line');
  for (let i = 1; i < blocks.length; i++) {
    const b = blocks[i];
    const vm = b.match(/data-voice="([a-z]+)"/);
    const sp = speakArgs(b.slice(0, 500));
    if (vm && sp.length) {
      for (const p of sp) phrases.set(p.trim(), vm[1] === 'ellen' ? 'ellen' : 'arthur');
    }
  }
}

// 2) Everything else
{
  let m;
  const dq = /data-phrase="([^"]*)"/g; while ((m = dq.exec(dec))) add(m[1].trim(), 'arthur');
  const sq = /data-phrase='([^']*)'/g; while ((m = sq.exec(dec))) add(m[1].trim(), 'arthur');
  for (const p of speakArgs(dec)) add(p, 'arthur');
}

// 3) Listening MP3s (full-length audio for sound-first exercises)
const LISTENINGS = [
  {
    file: 'aula1_listening1.mp3', voice: 'arthur',
    text: "I started playing video games when I was about nine. At first, it was just something I did for fun after school. But then I joined an online team, and everything changed. We practiced together three times a week, and I realized I was developing real skills — not just in the game, but in communication and teamwork. I have been competing in online tournaments for about four years now, and I have won several regional competitions. People sometimes underestimate gamers, but the truth is, it takes discipline, strategy, and the ability to keep up with constantly changing situations. Gaming has taught me more about teamwork than almost anything else in my life."
  },
  {
    file: 'aula1_listening2.mp3', voice: 'ellen',
    text: "Balancing school and competitive sports is one of the hardest things I have ever done. I have been training as a swimmer since I was seven, and for the past two years, I have been waking up at five in the morning every single day to practice before school. My friends sometimes do not understand why I cannot hang out after class, but I have learned to manage my time carefully. I think what people often underestimate about student athletes is our discipline. We are not just playing a sport — we are learning how to set goals, deal with failure, and push through when things get tough. It has completely changed my perspective on what I am capable of."
  }
];

// ---- file naming ----
function toFilename(text) {
  return text.toLowerCase()
    .replace(/[^a-z0-9 ]/g, '')
    .replace(/ +/g, '_')
    .slice(0, 60);
}

// ---- generate MP3 ----
function generateMP3(text, voiceId, outPath) {
  return new Promise((resolve, reject) => {
    if (fs.existsSync(outPath)) {
      console.log('  SKIP (exists):', path.basename(outPath));
      return resolve(outPath);
    }
    const body = JSON.stringify({
      text,
      model_id: MODEL_ID,
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    });
    const opts = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'xi-api-key': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
        'Content-Length': Buffer.byteLength(body)
      }
    };
    const req = https.request(opts, res => {
      if (res.statusCode !== 200) {
        let errBody = '';
        res.on('data', d => errBody += d);
        res.on('end', () => { console.error('  ERROR', res.statusCode, errBody.slice(0, 200)); reject(new Error(res.statusCode)); });
        return;
      }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => {
        fs.writeFileSync(outPath, Buffer.concat(chunks));
        console.log('  OK:', path.basename(outPath));
        resolve(outPath);
      });
    });
    req.on('error', reject);
    req.write(body);
    req.end();
  });
}

// ---- main ----
async function main() {
  console.log(`\n=== Mark B2 Audio Generator ===`);
  console.log(`Phrases: ${phrases.size}`);
  console.log(`Listenings: ${LISTENINGS.length}\n`);

  const audioMap = {};
  let alternateVoice = false;

  // Generate phrase audios
  for (const [phrase, voice] of phrases) {
    const fname = toFilename(phrase) + '.mp3';
    const outPath = path.join(OUT_DIR, fname);
    const voiceId = VOICES[voice];
    console.log(`[${voice}] "${phrase.slice(0, 50)}..."`);
    try {
      await generateMP3(phrase, voiceId, outPath);
      audioMap[phrase] = `/audio/${SLUG}/${fname}`;
    } catch (e) {
      console.error('  FAILED:', e.message);
    }
    // Rate limit
    await new Promise(r => setTimeout(r, 300));
  }

  // Generate listening audios
  for (const l of LISTENINGS) {
    const outPath = path.join(OUT_DIR, l.file);
    const voiceId = VOICES[l.voice];
    console.log(`\n[LISTENING] ${l.file}`);
    try {
      await generateMP3(l.text, voiceId, outPath);
    } catch (e) {
      console.error('  FAILED:', e.message);
    }
    await new Promise(r => setTimeout(r, 500));
  }

  // Write audioMap JSON
  const mapPath = path.join(ROOT, '_mark-b2-audiomap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMap, null, 2));
  console.log(`\naudioMap saved to ${mapPath}`);
  console.log(`Total: ${Object.keys(audioMap).length} entries`);

  // Generate the audioMap JS snippet to paste into the HTML
  let snippet = 'var audioMap = {\n';
  for (const [k, v] of Object.entries(audioMap)) {
    snippet += `  "${k.replace(/"/g, '\\"')}": "${v}",\n`;
  }
  snippet += '};\n';
  fs.writeFileSync(path.join(ROOT, '_mark-b2-audiomap-snippet.js'), snippet);
  console.log('JS snippet saved to _mark-b2-audiomap-snippet.js');
}

main().catch(e => { console.error(e); process.exit(1); });
