const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tania-rosa-aula6');

// Voice rules:
// Single words (1-2 words) = ALWAYS Arthur
// Phrases (3+ words) = ALTERNATE Arthur/Ellen
// Dialogue: Shopkeeper = Arthur, Tania = Ellen
const PHRASES = [
  // ===== Vocab words (1-2 words -> Arthur) =====
  { text: "Price", voice: ARTHUR },
  { text: "Size", voice: ARTHUR },
  { text: "Souvenir", voice: ARTHUR },
  { text: "Cash", voice: ARTHUR },
  { text: "Credit Card", voice: ARTHUR },
  { text: "Discount", voice: ARTHUR },
  { text: "Receipt", voice: ARTHUR },
  { text: "Change", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "What is the price of this scarf?", voice: ARTHUR },
  { text: "Do you have this in a larger size?", voice: ELLEN },
  { text: "I would like to buy some souvenirs for my grandchildren.", voice: ARTHUR },
  { text: "Could I pay in cash?", voice: ELLEN },
  { text: "Do you accept credit cards?", voice: ARTHUR },
  { text: "Is there a discount if I buy two?", voice: ELLEN },
  { text: "Could I have the receipt, please?", voice: ARTHUR },
  { text: "Here is your change. Thank you!", voice: ELLEN },

  // ===== Grammar: "How much" / comparatives (alternate) =====
  { text: "How much is this scarf?", voice: ARTHUR },
  { text: "How much does the bag cost?", voice: ELLEN },
  { text: "This one is cheaper than that one.", voice: ARTHUR },
  { text: "The blue scarf is more expensive than the red one.", voice: ELLEN },

  // ===== Dialogue — Shopkeeper = Arthur, Tania = Ellen =====
  { text: "Good afternoon! I am looking for souvenirs for my family.", voice: ELLEN },
  { text: "Welcome! We have scarves, bags, and handmade jewelry. What are you looking for?", voice: ARTHUR },
  { text: "I love that blue scarf. How much is it?", voice: ELLEN },
  { text: "That one is thirty-five euros.", voice: ARTHUR },
  { text: "And the red one? Is it cheaper?", voice: ELLEN },
  { text: "The red one is twenty-eight euros. It is smaller, but very popular.", voice: ARTHUR },
  { text: "I would like both. Is there a discount if I buy two?", voice: ELLEN },
  { text: "Yes! If you buy two, the total is fifty-five euros instead of sixty-three.", voice: ARTHUR },
  { text: "That is a good deal! Could I pay with a credit card?", voice: ELLEN },
  { text: "Of course! Here is your receipt. Would you like a bag?", voice: ARTHUR },

  // ===== Quiz / practice phrases (alternate) =====
  { text: "Excuse me, how much is this bag?", voice: ARTHUR },
  { text: "Do you have this in a larger size, please?", voice: ELLEN },
  { text: "This scarf is cheaper than that one.", voice: ARTHUR },
  { text: "Could I pay with a credit card?", voice: ELLEN },

  // ===== Survival / speech phrases (alternate) =====
  { text: "How much is this?", voice: ARTHUR },
  { text: "Is there a discount?", voice: ELLEN },
  { text: "Could I pay with a credit card?", voice: ARTHUR },
  { text: "Could I have the receipt, please?", voice: ELLEN },
  { text: "How much does it cost?", voice: ARTHUR },
  { text: "This is cheaper than that.", voice: ELLEN },
  { text: "I would like to pay with a card.", voice: ARTHUR },
  { text: "Do you have this in a bigger size?", voice: ELLEN },
  { text: "Could I have the receipt?", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Tania Rosa — Aula 6...');
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
