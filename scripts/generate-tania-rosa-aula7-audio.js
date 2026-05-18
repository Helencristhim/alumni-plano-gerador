const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tania-rosa-aula7');

// Voice rules:
// Single words (1-2 words) = ALWAYS Arthur
// Phrases (3+ words) = ALTERNATE Arthur/Ellen
// Dialogue: Marco = Arthur, Tânia = Ellen
const PHRASES = [
  // ===== Vocab words (1-2 words -> Arthur) =====
  { text: "Tradition", voice: ARTHUR },
  { text: "Festival", voice: ARTHUR },
  { text: "Monument", voice: ARTHUR },
  { text: "Local", voice: ARTHUR },
  { text: "Custom", voice: ARTHUR },
  { text: "Heritage", voice: ARTHUR },
  { text: "Landmark", voice: ARTHUR },
  { text: "Diversity", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "Every country has its own traditions.", voice: ARTHUR },
  { text: "I have been to a music festival in Spain.", voice: ELLEN },
  { text: "The Eiffel Tower is a famous monument.", voice: ARTHUR },
  { text: "The locals were very friendly and helpful.", voice: ELLEN },
  { text: "It is a custom to tip the waiter in the United States.", voice: ARTHUR },
  { text: "Brazil has a rich cultural heritage.", voice: ELLEN },
  { text: "The Colosseum is a landmark in Rome.", voice: ARTHUR },
  { text: "I love the cultural diversity of big cities.", voice: ELLEN },

  // ===== Grammar: Present Perfect examples (alternate) =====
  { text: "I have been to Portugal, Spain, and France.", voice: ARTHUR },
  { text: "Have you ever visited Japan?", voice: ELLEN },
  { text: "She has never been to Asia.", voice: ARTHUR },
  { text: "We have traveled to many countries.", voice: ELLEN },

  // ===== Dialogue — Marco = Arthur, Tânia = Ellen =====
  { text: "You are Brazilian, right? I love Brazil! Have you ever been to Italy?", voice: ARTHUR },
  { text: "Yes, I have! I have been to Rome and Florence. The monuments are incredible.", voice: ELLEN },
  { text: "What did you like most about Italy?", voice: ARTHUR },
  { text: "I loved the traditions and the food. Every region has different customs.", voice: ELLEN },
  { text: "That is true! Have you visited any festivals in your travels?", voice: ARTHUR },
  { text: "Yes, I have been to a music festival in Spain. It was an amazing experience.", voice: ELLEN },
  { text: "Spain is wonderful! I have never been to South America. What is Brazil like?", voice: ARTHUR },
  { text: "Brazil has incredible diversity — different cultures, languages, and traditions in every region.", voice: ELLEN },
  { text: "That sounds fascinating! What landmarks should I visit?", voice: ARTHUR },
  { text: "You should visit Rio de Janeiro, the Amazon, and Salvador. Brazil has a very rich heritage.", voice: ELLEN },

  // ===== Quiz / practice phrases (alternate) =====
  { text: "Yes, I have. I have been to Portugal, Spain, and France.", voice: ARTHUR },
  { text: "Have you ever visited Brazil?", voice: ELLEN },
  { text: "I have never been to Asia, but I would love to go.", voice: ARTHUR },
  { text: "In Brazil, we have a tradition of celebrating Carnival every year.", voice: ELLEN },

  // ===== Survival / speech phrases (alternate) =====
  { text: "I loved the local traditions and the cultural diversity.", voice: ARTHUR },
  { text: "You should visit the Eiffel Tower. It is a famous landmark in Paris.", voice: ELLEN },
  { text: "I have been to Portugal.", voice: ARTHUR },
  { text: "I love learning about different traditions and cultures.", voice: ELLEN },
  { text: "Brazil has a very rich cultural heritage.", voice: ARTHUR },
  { text: "You should visit Rio de Janeiro. It is a famous landmark.", voice: ELLEN },
  { text: "I have been to a music festival in Spain. It was amazing.", voice: ARTHUR },
  { text: "Brazil has incredible diversity — different cultures and traditions.", voice: ELLEN },
  { text: "I have never been to Asia, but I would love to visit.", voice: ARTHUR },
  { text: "You should visit Rio de Janeiro. It is beautiful.", voice: ELLEN },

  // ===== Error correction pairs (alternate) =====
  { text: "I have been in Portugal.", voice: ARTHUR },
  { text: "Did you ever visit Japan?", voice: ELLEN },
  { text: "She have been to many countries.", voice: ARTHUR },
  { text: "She has been to many countries.", voice: ELLEN },
  { text: "I never have been to Asia.", voice: ARTHUR },
  { text: "I have never been to Asia.", voice: ELLEN },
  { text: "The locals was very friendly.", voice: ARTHUR },
  { text: "The locals were very friendly.", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Tânia Rosa — Aula 7...');
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
