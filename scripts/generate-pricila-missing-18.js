const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

// 18 missing audio files for Pricila Adamo
// Voice assignment follows original aula1 script + alternation rules
const PHRASES = [
  // Vocab example sentences (from aula1 script — alternating)
  { text: "I want to become fluent in English before my next trip.", voice: ARTHUR, file: "i_want_to_become_fluent_in_english_before_my_next.mp3" },
  { text: "I sometimes struggle to find the right words in English.", voice: ARTHUR, file: "i_sometimes_struggle_to_find_the_right_words.mp3" },
  { text: "I want to accomplish my dream of speaking English fluently.", voice: ARTHUR, file: "i_want_to_accomplish_my_dream_of_speaking_english.mp3" },

  // Fill-in / practice phrase
  { text: "I grew up in Araras, a small city in Sao Paulo state.", voice: ELLEN, file: "i_grew_up_in_araras_a_small_city_in_sao_paulo.mp3" },

  // Grammar context sentences (about Pricila — 3rd person, alternating)
  { text: "She has worked as a dentist for over twenty-five years.", voice: ARTHUR, file: "she_has_worked_as_a_dentist_for_over_twenty_five.mp3" },
  { text: "She has traveled to Canada, Malta, and many other countries.", voice: ELLEN, file: "she_has_traveled_to_canada_malta_and_many_other.mp3" },
  { text: "She lives in Araras and goes to Sao Paulo every two weeks.", voice: ARTHUR, file: "she_lives_in_araras_and_goes_to_sao_paulo.mp3" },

  // Dialogue — David = Arthur
  { text: "That sounds wonderful! Have you been to Australia before?", voice: ARTHUR, file: "that_sounds_wonderful_have_you_been_to_australia.mp3" },

  // Error sentences for Spot the Error (alternating)
  { text: "I have study English for many years.", voice: ELLEN, file: "error_i_have_study_english.mp3" },
  { text: "She retire last year from her clinic.", voice: ARTHUR, file: "error_she_retire_last_year.mp3" },
  { text: "I am live in Araras since 2000.", voice: ELLEN, file: "error_i_am_live_in_araras.mp3" },
  { text: "He has went to Australia twice.", voice: ARTHUR, file: "error_he_has_went_to_australia.mp3" },

  // Expressions (short phrases, alternating)
  { text: "I have been studying English for...", voice: ARTHUR, file: "expression_i_have_been_studying.mp3" },
  { text: "I grew up in...", voice: ELLEN, file: "expression_i_grew_up_in.mp3" },
  { text: "I have always wanted to...", voice: ARTHUR, file: "expression_i_have_always_wanted_to.mp3" },
  { text: "Right now, I am...", voice: ELLEN, file: "expression_right_now_i_am.mp3" },
  { text: "To be honest, the thing is...", voice: ARTHUR, file: "expression_to_be_honest.mp3" },

  // Ordering audio (self-introduction — Ellen as Pricila)
  { text: "Let me introduce myself. I am Pricila Adamo. I am a dentist, but I am retiring soon. I have been studying English since the year 2000. I have always been curious about the world. I want to explore Australia next year.", voice: ELLEN, file: "order_l1_self_introduction.mp3" },
];

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

  console.log('Generating ' + PHRASES.length + ' missing audio files for Pricila Adamo...\n');
  let generated = 0;
  let skipped = 0;

  for (const p of PHRASES) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('SKIP (exists): ' + p.file);
      skipped++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped);
}

main().catch(e => { console.error(e); process.exit(1); });
