const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'karina-macedo');

// Voice rules (Karina is FEMALE):
// - Single words = ELLEN (student gender)
// - Karina's exercise/survival phrases = ELLEN
// - Male investor dialogue lines = ARTHUR
// - General alternating phrases = alternate Arthur/Ellen

const PHRASES = [
  // ===== Aula 3 Vocab words (Karina is female = ELLEN) =====
  { text: "Offer", file: "offer.mp3", voice: ELLEN },
  { text: "Team", file: "team.mp3", voice: ELLEN },
  { text: "Service", file: "service.mp3", voice: ELLEN },
  { text: "Partner", file: "partner.mp3", voice: ELLEN },
  { text: "Quality", file: "quality.mp3", voice: ELLEN },
  { text: "Deliver", file: "deliver.mp3", voice: ELLEN },
  { text: "Experience", file: "experience.mp3", voice: ELLEN },

  // ===== Aula 3 Fill-in / Practice phrases (alternate Arthur/Ellen) =====
  { text: "We offer the best aircraft in Brazil.", file: "we_offer_the_best_aircraft_in_brazil.mp3", voice: ELLEN },
  { text: "My team has ten people.", file: "my_team_has_ten_people.mp3", voice: ARTHUR },
  { text: "We offer excellent service.", file: "we_offer_excellent_service.mp3", voice: ELLEN },
  { text: "We have partners in Europe.", file: "we_have_partners_in_europe.mp3", voice: ARTHUR },
  { text: "Our aircraft are high quality.", file: "our_aircraft_are_high_quality.mp3", voice: ELLEN },
  { text: "We deliver aircraft worldwide.", file: "we_deliver_aircraft_worldwide.mp3", voice: ARTHUR },
  { text: "I have ten years of experience.", file: "i_have_ten_years_of_experience.mp3", voice: ELLEN },
  { text: "Our company offers sales and delivery services.", file: "our_company_offers_sales_delivery.mp3", voice: ARTHUR },
  { text: "We have been in aviation for fifteen years.", file: "we_have_been_in_aviation_fifteen_years.mp3", voice: ELLEN },
  { text: "Our experience makes us different.", file: "our_experience_makes_us_different.mp3", voice: ARTHUR },

  // ===== Aula 3 Speech card phrases (Karina practicing = ELLEN) =====
  { text: "We deliver high quality aircraft worldwide.", file: "we_deliver_high_quality_aircraft_worldwide.mp3", voice: ELLEN },

  // ===== Aula 3 Survival card phrases (Karina = ELLEN) =====
  { text: "Our company offers.", file: "our_company_offers.mp3", voice: ELLEN },
  { text: "We have ten years of experience.", file: "we_have_ten_years_of_experience.mp3", voice: ELLEN },
  { text: "Our team is excellent.", file: "our_team_is_excellent.mp3", voice: ELLEN },
  { text: "We deliver worldwide.", file: "we_deliver_worldwide.mp3", voice: ELLEN },
  { text: "We have partners in many countries.", file: "we_have_partners_in_many_countries.mp3", voice: ELLEN },

  // ===== Aula 3 Dialogue — Investor (male = ARTHUR), Karina (female = ELLEN) =====
  { text: "Tell me about your company.", file: "dialogue3_investor_1.mp3", voice: ARTHUR },
  { text: "We are Aviation Business Group. We have been in aviation for fifteen years.", file: "dialogue3_karina_1.mp3", voice: ELLEN },
  { text: "That is impressive! How big is your team?", file: "dialogue3_investor_2.mp3", voice: ARTHUR },
  { text: "Our team has ten people. We offer sales, import, and export services.", file: "dialogue3_karina_2.mp3", voice: ELLEN },
  { text: "Do you have partners outside Brazil?", file: "dialogue3_investor_3.mp3", voice: ARTHUR },
  { text: "Yes! We have partners in Europe and the Middle East.", file: "dialogue3_karina_3.mp3", voice: ELLEN },
  { text: "What makes your company different?", file: "dialogue3_investor_4.mp3", voice: ARTHUR },
  { text: "Our experience and quality. We deliver high quality aircraft worldwide.", file: "dialogue3_karina_4.mp3", voice: ELLEN },

  // ===== Aula 3 Listening 1 — Karina presenting her company (ELLEN) =====
  { text: "Good morning, everyone. My name is Karina Macedo, and I am the director of Aviation Business Group. We are based in São Paulo, Brazil. Our company has been in aviation for fifteen years. We offer aircraft sales, import, export, and delivery services. Our team has ten experienced people. We have partners in Europe and the Middle East. We deliver high quality aircraft to clients worldwide. What makes us different? Our experience and our commitment to quality. Thank you.", file: "listening3_company_presentation.mp3", voice: ELLEN },

  // ===== Aula 3 Listening 2 — Investor asking questions (ARTHUR) =====
  { text: "Tell me more about your team. How many years of experience do you have? What kind of aircraft do you sell? Do you deliver to Asia? Can I visit your office in São Paulo?", file: "listening3_investor_questions.mp3", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Karina Macedo — Aula 3...');
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
      console.error('  FAIL: ' + p.file + ' -> ' + err.message);
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + unique.length);
}

main().catch(console.error);
