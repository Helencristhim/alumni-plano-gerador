const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tania-rosa-aula4');

// Voice rules:
// Single words (1-2 words) = ALWAYS Arthur
// Phrases (3+ words) = ALTERNATE Arthur/Ellen
// Dialogue: Local = Arthur, Tânia = Ellen
const PHRASES = [
  // ===== Vocab words (1-2 words → Arthur) =====
  { text: "Direction", voice: ARTHUR },
  { text: "Street", voice: ARTHUR },
  { text: "Corner", voice: ARTHUR },
  { text: "Block", voice: ARTHUR },
  { text: "Subway", voice: ARTHUR },
  { text: "Map", voice: ARTHUR },
  { text: "Bridge", voice: ARTHUR },
  { text: "Sidewalk", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "Could you tell me the direction to the museum?", voice: ARTHUR },
  { text: "The restaurant is on Main Street.", voice: ELLEN },
  { text: "Turn right at the corner.", voice: ARTHUR },
  { text: "The pharmacy is two blocks from here.", voice: ELLEN },
  { text: "Could you tell me where the subway station is?", voice: ARTHUR },
  { text: "I need a map of the city.", voice: ELLEN },
  { text: "Walk across the bridge and turn left.", voice: ARTHUR },
  { text: "Stay on the sidewalk and go straight.", voice: ELLEN },

  // ===== Grammar: imperatives / prepositions (alternate) =====
  { text: "Go straight for two blocks.", voice: ARTHUR },
  { text: "Turn left at the corner.", voice: ELLEN },
  { text: "The museum is next to the café.", voice: ARTHUR },
  { text: "The bank is across from the bridge.", voice: ELLEN },

  // ===== Dialogue — Local = Arthur, Tânia = Ellen =====
  { text: "Excuse me, could you help me? I am looking for the Art Museum.", voice: ELLEN },
  { text: "Of course! The Art Museum is not far from here.", voice: ARTHUR },
  { text: "How do I get there?", voice: ELLEN },
  { text: "Go straight on this street for two blocks.", voice: ARTHUR },
  { text: "Two blocks. And then?", voice: ELLEN },
  { text: "Then turn left at the corner. You will see a big bridge.", voice: ARTHUR },
  { text: "Turn left at the corner, near the bridge. Got it.", voice: ELLEN },
  { text: "The museum is across from the bridge, next to a café.", voice: ARTHUR },
  { text: "Across from the bridge, next to a café. Is it far to walk?", voice: ELLEN },
  { text: "No, about ten minutes. You can also take the subway. The station is on the next block.", voice: ARTHUR },

  // ===== Speech / practice phrases (alternate) =====
  { text: "Excuse me, could you tell me where the subway station is?", voice: ARTHUR },
  { text: "Is the hotel two blocks from here?", voice: ELLEN },
  { text: "Could I have a map of the city, please?", voice: ARTHUR },
  { text: "The bank is next to the pharmacy, on Main Street.", voice: ELLEN },

  // ===== Spot the Error phrases (alternate) =====
  { text: "I turn to the left side.", voice: ARTHUR },
  { text: "Go to the left at the corner.", voice: ELLEN },
  { text: "The museum is in the corner.", voice: ARTHUR },
  { text: "The museum is on the corner.", voice: ELLEN },
  { text: "Walk straight for two block.", voice: ARTHUR },
  { text: "Walk straight for two blocks.", voice: ELLEN },
  { text: "Where is the subway is?", voice: ARTHUR },
  { text: "Where is the subway?", voice: ELLEN },
  { text: "The café is across the bridge.", voice: ARTHUR },
  { text: "The café is across from the bridge.", voice: ELLEN },

  // ===== Quiz / survival phrases (alternate) =====
  { text: "Go straight for two blocks, then turn right.", voice: ARTHUR },
  { text: "How far is the museum from here?", voice: ELLEN },
  { text: "The bank is next to the pharmacy.", voice: ARTHUR },
  { text: "Is it far to walk? Can I walk there?", voice: ELLEN },
  { text: "Excuse me, could you help me?", voice: ARTHUR },
  { text: "How do I get to the Art Museum?", voice: ELLEN },
  { text: "Turn left at the corner and go straight.", voice: ARTHUR },
  { text: "Is it far to walk?", voice: ELLEN },
  { text: "Could you tell me where the subway station is?", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Tânia Rosa — Aula 4...');
  let generated = 0;
  let skipped = 0;
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
      skipped++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total entries: ' + unique.length);
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
