const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'karina-macedo');

// Voice rules (Karina is FEMALE):
// - Single words = ELLEN (student gender)
// - Karina's exercise phrases = ELLEN
// - Male buyer dialogue lines = ARTHUR
// - General alternating phrases = alternate Arthur/Ellen

const PHRASES = [
  // ===== Aula 2 Vocab words (Karina is female → ELLEN) =====
  { text: "Price", file: "price.mp3", voice: ELLEN },
  { text: "Number", file: "number.mp3", voice: ELLEN },
  { text: "Million", file: "million.mp3", voice: ELLEN },
  { text: "Thousand", file: "thousand.mp3", voice: ELLEN },
  { text: "Cost", file: "cost.mp3", voice: ELLEN },
  { text: "Expensive", file: "expensive.mp3", voice: ELLEN },
  { text: "Client", file: "client.mp3", voice: ELLEN },

  // ===== Aula 2 Fill-in / Practice phrases (alternate Arthur/Ellen) =====
  { text: "How much does this aircraft cost?", file: "how_much_does_this_aircraft_cost.mp3", voice: ELLEN },
  { text: "It costs five million dollars.", file: "it_costs_five_million_dollars.mp3", voice: ARTHUR },
  { text: "The price is two million.", file: "the_price_is_two_million.mp3", voice: ELLEN },

  // ===== Aula 2 Survival card phrases (Karina = ELLEN) =====
  { text: "How much does it cost?", file: "how_much_does_it_cost.mp3", voice: ELLEN },
  { text: "The price is five million dollars.", file: "the_price_is_five_million_dollars.mp3", voice: ELLEN },
  { text: "That is too expensive.", file: "that_is_too_expensive.mp3", voice: ELLEN },
  { text: "We can offer a discount.", file: "we_can_offer_a_discount.mp3", voice: ELLEN },
  { text: "The final price is four million dollars.", file: "the_final_price_is_four_million_dollars.mp3", voice: ELLEN },

  // ===== Aula 2 Dialogue — Buyer (male = ARTHUR), Karina (female = ELLEN) =====
  { text: "Good morning. I am looking for an aircraft for my company.", file: "dialogue2_buyer_1.mp3", voice: ARTHUR },
  { text: "Welcome! How many seats do you need?", file: "dialogue2_karina_1.mp3", voice: ELLEN },
  { text: "About eight seats. How much does an eight-seat aircraft cost?", file: "dialogue2_buyer_2.mp3", voice: ARTHUR },
  { text: "An eight-seat aircraft costs five million dollars.", file: "dialogue2_karina_2.mp3", voice: ELLEN },
  { text: "That is expensive. Do you have anything cheaper?", file: "dialogue2_buyer_3.mp3", voice: ARTHUR },
  { text: "We have a six-seat aircraft. The price is three million dollars.", file: "dialogue2_karina_3.mp3", voice: ELLEN },
  { text: "That sounds good. Can you offer a discount?", file: "dialogue2_buyer_4.mp3", voice: ARTHUR },
  { text: "Yes! The final price is two million eight hundred thousand dollars.", file: "dialogue2_karina_4.mp3", voice: ELLEN },

  // ===== Aula 2 Listening 1 — Karina presenting prices (ELLEN) =====
  { text: "Good morning. Let me show you our aircraft options. The first aircraft has four seats. The price is two million dollars. The second aircraft has eight seats. It costs five million dollars. And our best aircraft has twelve seats. It is very fast. The price is ten million dollars. We can discuss discounts for large orders.", file: "listening2_karina_prices.mp3", voice: ELLEN },

  // ===== Aula 2 Listening 2 — Buyer asking price questions (ARTHUR) =====
  { text: "How much does this aircraft cost? Is the price negotiable? Can you give me the price in euros? I would like to see the price list. How many aircraft are available?", file: "listening2_buyer_price_questions.mp3", voice: ARTHUR },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    }),
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
  const unique = PHRASES.filter(p => {
    const k = p.file.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' audio files for Karina Macedo — Aula 2...');
  let generated = 0;
  let skipped = 0;

  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('  SKIP (exists): ' + p.file);
      skipped++;
      continue;
    }
    try {
      const size = await gen(p.text, p.voice, outPath);
      generated++;
      console.log('  OK (' + (size / 1024).toFixed(1) + 'KB): ' + p.file + ' [' + (p.voice === ARTHUR ? 'Arthur' : 'Ellen') + ']');
      // Rate limit: ~2 requests/second
      await new Promise(resolve => setTimeout(resolve, 500));
    } catch (err) {
      console.error('  FAIL: ' + p.file + ' → ' + err.message);
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + unique.length);
}

main().catch(console.error);
