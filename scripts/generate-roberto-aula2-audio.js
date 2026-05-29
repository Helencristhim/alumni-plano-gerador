const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

// Roberto = male → Arthur
// Airport staff (female) = Ellen
// Single words (1-2) → ALWAYS Arthur
// Phrases (3+) → ALTERNATE Arthur/Ellen
const PHRASES = [
  // Vocab words (1-2 words → Arthur)
  { text: "Excuse me", voice: ARTHUR },
  { text: "Help", voice: ARTHUR },
  { text: "Understand", voice: ARTHUR },
  { text: "Repeat", voice: ARTHUR },
  { text: "Slowly", voice: ARTHUR },
  { text: "Speak", voice: ARTHUR },

  // Vocab example sentences (alternate)
  { text: "Excuse me, can you help me?", voice: ARTHUR },
  { text: "I do not understand.", voice: ELLEN },
  { text: "Can you repeat that, please?", voice: ARTHUR },
  { text: "Can you speak more slowly?", voice: ELLEN },
  { text: "Do you speak English?", voice: ARTHUR },
  { text: "Excuse me, where is the exit?", voice: ELLEN },

  // Fill-in / practice sentences (alternate)
  { text: "Can you help me, please?", voice: ARTHUR },
  { text: "I do not understand this sign.", voice: ELLEN },
  { text: "I do not understand. Can you repeat that?", voice: ARTHUR },

  // Speech cards (alternate)
  { text: "Excuse me, can you help me? I do not understand this sign.", voice: ELLEN },

  // Dialogue — Airport staff (female) = Ellen, Roberto (male) = Arthur
  { text: "Of course! What do you need?", voice: ELLEN },
  { text: "Can you repeat that slowly, please?", voice: ARTHUR },
  { text: "Sure. The exit is on the left, near the taxi stand.", voice: ELLEN },
  { text: "Thank you! Do you speak English?", voice: ARTHUR },
  { text: "Yes, I do. You are welcome!", voice: ELLEN },

  // Quick fire / quiz phrases (alternate)
  { text: "Can you help me?", voice: ARTHUR },
  { text: "Do you understand?", voice: ELLEN },
  { text: "Can you repeat that?", voice: ARTHUR },
  { text: "Do you speak Spanish?", voice: ELLEN },
  { text: "Can you speak slowly?", voice: ARTHUR },
  { text: "Do you have a map?", voice: ELLEN },
];

function toFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 60);
}

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => { const k = p.text.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });

  console.log('Generating ' + unique.length + ' audio files for Roberto Pires — Aula 2...');
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
    }
  }

  console.log('\nDone! Generated ' + unique.length + ' entries.');
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
