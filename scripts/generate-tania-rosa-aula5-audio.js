const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tania-rosa-aula5');

// Voice rules:
// Single words (1-2 words) = ALWAYS Arthur
// Phrases (3+ words) = ALTERNATE Arthur/Ellen
// Dialogue: Waiter = Arthur, Tania = Ellen
const PHRASES = [
  // ===== Vocab words (1-2 words -> Arthur) =====
  { text: "Menu", voice: ARTHUR },
  { text: "Order", voice: ARTHUR },
  { text: "Appetizer", voice: ARTHUR },
  { text: "Main Course", voice: ARTHUR },
  { text: "Dessert", voice: ARTHUR },
  { text: "Bill", voice: ARTHUR },
  { text: "Tip", voice: ARTHUR },
  { text: "Waiter", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "Could I see the menu, please?", voice: ARTHUR },
  { text: "Are you ready to order?", voice: ELLEN },
  { text: "I would like an appetizer to start.", voice: ARTHUR },
  { text: "For the main course, I would like the grilled fish.", voice: ELLEN },
  { text: "Could I see the dessert menu, please?", voice: ARTHUR },
  { text: "Could I have the bill, please?", voice: ELLEN },
  { text: "Is the tip included in the bill?", voice: ARTHUR },
  { text: "Excuse me, could I ask the waiter a question?", voice: ELLEN },

  // ===== Grammar: "could I have / I would like" phrases (alternate) =====
  { text: "Could I have the grilled fish, please?", voice: ARTHUR },
  { text: "Could I see the menu?", voice: ELLEN },
  { text: "Could we have a table for two?", voice: ARTHUR },
  { text: "Could you bring the bill, please?", voice: ELLEN },

  // ===== Dialogue — Waiter = Arthur, Tania = Ellen =====
  { text: "Good evening! Welcome to La Bella Vista. A table for one?", voice: ARTHUR },
  { text: "Good evening! Yes, a table for one, please. Could I sit near the window?", voice: ELLEN },
  { text: "Of course! Here is the menu. Would you like something to drink?", voice: ARTHUR },
  { text: "I would like a glass of sparkling water, please.", voice: ELLEN },
  { text: "Are you ready to order, or would you like a few more minutes?", voice: ARTHUR },
  { text: "I am ready. Could I have the tomato soup as an appetizer?", voice: ELLEN },
  { text: "Excellent choice! And for the main course?", voice: ARTHUR },
  { text: "I would like the grilled fish with vegetables, please.", voice: ELLEN },
  { text: "Perfect. Would you like to see the dessert menu later?", voice: ARTHUR },
  { text: "Yes, please. And could I have the bill after dessert? I am in no hurry.", voice: ELLEN },

  // ===== Quiz / practice phrases (alternate) =====
  { text: "Good evening! Could I have a table for one, please?", voice: ARTHUR },
  { text: "Yes, I would like the grilled fish, please.", voice: ELLEN },
  { text: "Excuse me, is the tip included?", voice: ARTHUR },
  { text: "I would like the fish, please.", voice: ELLEN },
  { text: "I would like an appetizer.", voice: ARTHUR },
  { text: "Could I have the menu?", voice: ELLEN },
  { text: "The waiter brings the dessert.", voice: ARTHUR },

  // ===== Additional speech / survival phrases (alternate) =====
  { text: "Good evening! Could I have a table for two, please?", voice: ELLEN },
  { text: "Excuse me, what is today's special?", voice: ARTHUR },
  { text: "Could I have the tomato soup as an appetizer and the grilled fish as the main course?", voice: ELLEN },
  { text: "I would like the grilled fish, please.", voice: ARTHUR },
  { text: "Thank you, the food was delicious!", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Tania Rosa — Aula 5...');
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
