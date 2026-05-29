const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'milton-sayegh');

const VOICE_ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const VOICE_ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

// 12 missing audio files identified by audit
const MISSING = [
  { text: "For over thirty years. But I'm working on improving my English for negotiations.", file: "for_over_thirty_years_but_im_working_on_improving_my_english.mp3" },
  { text: "I'd like to discuss a possible partnership.", file: "id_like_to_discuss_a_possible_partnership.mp3" },
  { text: "I'm from Sao Paulo, Brazil.", file: "im_from_sao_paulo_brazil.mp3" },
  { text: "I'm responsible for all export operations.", file: "im_responsible_for_all_export_operations.mp3" },
  { text: "I'm responsible for all operations.", file: "im_responsible_for_all_operations.mp3" },
  { text: "I'm responsible for the export operations of my company.", file: "im_responsible_for_the_export_operations_of_my_company.mp3" },
  { text: "I'm sorry, I didn't quite catch that.", file: "im_sorry_i_didnt_quite_catch_that.mp3" },
  { text: "I'm working on improving my English.", file: "im_working_on_improving_my_english.mp3" },
  { text: "It's a pleasure to meet you.", file: "its_a_pleasure_to_meet_you.mp3" },
  { text: "My name is Milton Sayegh. I'm in the jewelry business.", file: "my_name_is_milton_sayegh_im_in_the_jewelry_business.mp3" },
  { text: "That would be great. I'm responsible for all business decisions, so we can move quickly.", file: "that_would_be_great_im_responsible_for_all_business_decisions.mp3" },
  { text: "We specialize in...", file: "we_specialize_in.mp3" },
];

let ellenToggle = false;
function getVoice(text) {
  const words = text.replace(/[^a-zA-Z0-9' -]/g, '').trim().split(/\s+/).filter(w => w).length;
  if (words <= 2) return { id: VOICE_ARTHUR, name: 'Arthur' };
  ellenToggle = !ellenToggle;
  return ellenToggle ? { id: VOICE_ELLEN, name: 'Ellen' } : { id: VOICE_ARTHUR, name: 'Arthur' };
}

async function generateOne(text, voiceId, retries = 2) {
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;
  for (let attempt = 0; attempt <= retries; attempt++) {
    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Accept': 'audio/mpeg' },
        body: JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
      });
      if (res.status === 429) { console.log('  Rate limited, waiting 30s...'); await new Promise(r => setTimeout(r, 30000)); continue; }
      if (!res.ok) throw new Error(`HTTP ${res.status}: ${await res.text()}`);
      return Buffer.from(await res.arrayBuffer());
    } catch (e) { if (attempt === retries) throw e; console.log(`  Retry ${attempt + 1}...`); await new Promise(r => setTimeout(r, 2000)); }
  }
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  // Filter only truly missing
  const toGenerate = MISSING.filter(p => !fs.existsSync(path.join(OUTPUT_DIR, p.file)));
  console.log(`\n=== Milton Sayegh: ${toGenerate.length} missing audio files ===\n`);

  for (let i = 0; i < toGenerate.length; i++) {
    const p = toGenerate[i];
    const voice = getVoice(p.text);
    console.log(`[${i + 1}/${toGenerate.length}] ${voice.name}: "${p.text.substring(0, 50)}..."`);
    try {
      const buf = await generateOne(p.text, voice.id);
      fs.writeFileSync(path.join(OUTPUT_DIR, p.file), buf);
      console.log(`  OK (${(buf.length / 1024).toFixed(1)} KB)`);
    } catch (e) { console.error(`  FAILED: ${e.message}`); }
    await new Promise(r => setTimeout(r, 150));
  }
  console.log('\nDone!');
}

main();
