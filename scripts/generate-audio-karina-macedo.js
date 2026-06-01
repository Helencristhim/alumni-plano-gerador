const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'karina-macedo');

// Voice rules:
// - Karina is FEMALE → her lines/exercises = ELLEN
// - Buyer is MALE → his lines = ARTHUR
// - Single words = ELLEN (student gender)
// - General phrases = ALTERNATE Arthur/Ellen

const PHRASES = [
  // ===== Emergency phrases (alternate) =====
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: ARTHUR },
  { text: "I do not understand. Could you explain?", file: "i_do_not_understand_could_you_explain.mp3", voice: ELLEN },
  { text: "How do you say this in English?", file: "how_do_you_say_this_in_english.mp3", voice: ARTHUR },
  { text: "Can you speak more slowly, please?", file: "can_you_speak_more_slowly_please.mp3", voice: ELLEN },
  { text: "I need a moment to think.", file: "i_need_a_moment_to_think.mp3", voice: ARTHUR },

  // ===== Vocab words (Karina is female → ELLEN) =====
  { text: "Aircraft", file: "aircraft.mp3", voice: ELLEN },
  { text: "Buy", file: "buy.mp3", voice: ELLEN },
  { text: "Sell", file: "sell.mp3", voice: ELLEN },
  { text: "Business", file: "business.mp3", voice: ELLEN },
  { text: "Company", file: "company.mp3", voice: ELLEN },
  { text: "Aviation", file: "aviation.mp3", voice: ELLEN },
  { text: "Export", file: "export.mp3", voice: ELLEN },

  // ===== Fill-in-the-blank sentences (alternate) =====
  { text: "My name is Karina Macedo.", file: "my_name_is_karina_macedo.mp3", voice: ELLEN },
  { text: "I work in the aviation business.", file: "i_work_in_the_aviation_business.mp3", voice: ELLEN },
  { text: "My company buys and sells aircraft.", file: "my_company_buys_and_sells_aircraft.mp3", voice: ARTHUR },
  { text: "We export aircraft to other countries.", file: "we_export_aircraft_to_other_countries.mp3", voice: ELLEN },
  { text: "I am from Sao Paulo, Brazil.", file: "i_am_from_sao_paulo_brazil.mp3", voice: ARTHUR },
  { text: "She is a businesswoman in aviation.", file: "she_is_a_businesswoman_in_aviation.mp3", voice: ELLEN },

  // ===== Speech practice (Karina = ELLEN) =====
  { text: "I buy and sell aircraft.", file: "i_buy_and_sell_aircraft.mp3", voice: ELLEN },
  { text: "Nice to meet you!", file: "nice_to_meet_you.mp3", voice: ELLEN },

  // ===== Survival card Lesson 1 (Karina = ELLEN) =====
  { text: "I work in aviation.", file: "i_work_in_aviation.mp3", voice: ELLEN },
  { text: "Could I have your business card?", file: "could_i_have_your_business_card.mp3", voice: ELLEN },

  // ===== Dialogue — Buyer (male = ARTHUR), Karina (female = ELLEN) =====
  { text: "Hi! Are you in the aviation business?", file: "dialogue_buyer_1.mp3", voice: ARTHUR },
  { text: "Yes! My name is Karina Macedo. I am from Sao Paulo.", file: "dialogue_karina_1.mp3", voice: ELLEN },
  { text: "Nice to meet you! What does your company do?", file: "dialogue_buyer_2.mp3", voice: ARTHUR },
  { text: "We buy and sell aircraft. We also export to many countries.", file: "dialogue_karina_2.mp3", voice: ELLEN },
  { text: "Interesting! How many aircraft do you sell per year?", file: "dialogue_buyer_3.mp3", voice: ARTHUR },
  { text: "We sell about ten aircraft per year.", file: "dialogue_karina_3.mp3", voice: ELLEN },
  { text: "That is impressive! Do you have a business card?", file: "dialogue_buyer_4.mp3", voice: ARTHUR },
  { text: "Yes! Here is my business card. Nice to meet you!", file: "dialogue_karina_4.mp3", voice: ELLEN },

  // ===== Numbers in Aviation (alternate) =====
  { text: "one aircraft", file: "one_aircraft.mp3", voice: ELLEN },
  { text: "two clients", file: "two_clients.mp3", voice: ARTHUR },
  { text: "three countries", file: "three_countries.mp3", voice: ELLEN },
  { text: "five fairs", file: "five_fairs.mp3", voice: ARTHUR },
  { text: "ten sales", file: "ten_sales.mp3", voice: ELLEN },

  // ===== Listening 1 — Karina full intro (ELLEN) =====
  { text: "Hello! My name is Karina Macedo. I am from Sao Paulo, Brazil. I work in the aviation business. My company buys and sells aircraft. We also export to many countries. Nice to meet you!", file: "listening1_full_introduction.mp3", voice: ELLEN },

  // ===== Listening 2 — Buyer questions (ARTHUR) =====
  { text: "Excuse me, I am looking for someone who sells aircraft. Do you work in aviation? What is the name of your company? Do you export to Europe?", file: "listening2_buyer_questions.mp3", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Karina Macedo...');
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
