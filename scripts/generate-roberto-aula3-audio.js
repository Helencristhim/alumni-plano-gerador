const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

// Roberto = male → Arthur
// Vendor/shopkeeper (female) = Ellen
// Single words (1-2) → ALWAYS Arthur
// Phrases (3+) → ALTERNATE Arthur/Ellen
const PHRASES = [
  // Vocab words (1-2 words → Arthur)
  { text: "Price", voice: ARTHUR },
  { text: "Euro", voice: ARTHUR },
  { text: "Receipt", voice: ARTHUR },
  { text: "Cash", voice: ARTHUR },
  { text: "Card", voice: ARTHUR },
  { text: "Expensive", voice: ARTHUR },
  { text: "Cheap", voice: ARTHUR },
  { text: "Change", voice: ARTHUR },

  // Vocab example sentences (alternate)
  { text: "How much does this cost?", voice: ARTHUR },
  { text: "I want to pay in euros.", voice: ELLEN },
  { text: "Do you accept credit cards?", voice: ARTHUR },
  { text: "Can I have the receipt, please?", voice: ELLEN },
  { text: "That is too expensive.", voice: ARTHUR },
  { text: "No, thank you. I will think about it.", voice: ELLEN },
  { text: "I will take it!", voice: ARTHUR },

  // Grammar in Context sentences (alternate)
  { text: "How much is this scarf?", voice: ELLEN },
  { text: "It is twenty-five euros.", voice: ARTHUR },
  { text: "This one is only five euros.", voice: ELLEN },
  { text: "I will pay cash.", voice: ARTHUR },

  // Fill-in / practice sentences (alternate)
  { text: "It costs ten euros.", voice: ELLEN },
  { text: "The price is fifteen euros.", voice: ARTHUR },
  { text: "Do you have something cheaper?", voice: ELLEN },
  { text: "Here is your change.", voice: ARTHUR },
  { text: "I need the receipt for my company.", voice: ELLEN },

  // Numbers (1-2 words → Arthur)
  { text: "Thirteen", voice: ARTHUR },
  { text: "Thirty", voice: ARTHUR },
  { text: "Fourteen", voice: ARTHUR },
  { text: "Forty", voice: ARTHUR },
  { text: "Fifteen", voice: ARTHUR },
  { text: "Fifty", voice: ARTHUR },

  // Dialogue 1 — Market vendor (female) = Ellen, Roberto (male) = Arthur
  { text: "Good morning! What can I get for you?", voice: ELLEN },
  { text: "How much are the olives?", voice: ARTHUR },
  { text: "The small box is three euros. The large box is five euros.", voice: ELLEN },
  { text: "I will take the large box, please.", voice: ARTHUR },
  { text: "Anything else?", voice: ELLEN },
  { text: "How much is that cheese?", voice: ARTHUR },
  { text: "That is eighteen euros.", voice: ELLEN },
  { text: "That is too expensive. Do you have something cheaper?", voice: ARTHUR },
  { text: "This one is twelve euros. Very good quality.", voice: ELLEN },
  { text: "OK, I will take it. Do you accept credit cards?", voice: ARTHUR },
  { text: "Sorry, only cash.", voice: ELLEN },
  { text: "No problem. Here you go. Can I have the receipt, please?", voice: ARTHUR },
  { text: "Of course! Here is your receipt. Thank you!", voice: ELLEN },
  { text: "Thank you! Have a good day.", voice: ARTHUR },

  // Dialogue 2 — Souvenir shop (shopkeeper=Ellen, Roberto=Arthur)
  { text: "Excuse me, how much is this magnet?", voice: ARTHUR },
  { text: "That is seven euros.", voice: ELLEN },
  { text: "And the t-shirt?", voice: ARTHUR },
  { text: "The t-shirt is twenty euros.", voice: ELLEN },
  { text: "That is a bit expensive. Do you have a cheaper one?", voice: ARTHUR },
  { text: "This one is fifteen euros.", voice: ELLEN },
  { text: "I will take the magnet and the cheaper t-shirt.", voice: ARTHUR },
  { text: "That is twenty-two euros total.", voice: ELLEN },
  { text: "Can I pay with my card?", voice: ARTHUR },
  { text: "Yes, we accept cards.", voice: ELLEN },

  // Quick fire / survival phrases (alternate)
  { text: "How much is this?", voice: ARTHUR },
  { text: "Can I have the receipt?", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Roberto Pires — Aula 3...');
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
