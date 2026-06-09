const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

const missing = [
  { text: "Does she need a visa?", voice: ARTHUR, file: "does_she_need_a_visa.mp3" },
  { text: "The officer stamps your passport.", voice: ARTHUR, file: "the_officer_stamps_your_passport.mp3" },
  { text: "I am a Brazilian citizen.", voice: ELLEN, file: "i_am_a_brazilian_citizen.mp3" },
  { text: "Good afternoon. Passport, please. What is the purpose of your visit?", voice: ARTHUR, file: "good_afternoon_passport_please.mp3" },
  { text: "Ten days. I return on the twenty-fifth.", voice: ELLEN, file: "ten_days_i_return_on_the_twenty_fifth.mp3" },
  { text: "Do you have a hotel reservation?", voice: ARTHUR, file: "do_you_have_a_hotel_reservation.mp3" },
  { text: "Yes, I do. Here is my reservation.", voice: ELLEN, file: "yes_i_do_here_is_my_reservation.mp3" },
  { text: "Do you have anything to declare at customs?", voice: ARTHUR, file: "do_you_have_anything_to_declare_customs.mp3" },
  { text: "No, I do not. Just personal items. Thank you!", voice: ELLEN, file: "no_i_do_not_just_personal_items.mp3" },
];

function gen(text, voiceId) {
  return new Promise((resolve, reject) => {
    const d = JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const o = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voiceId}`, method: 'POST', headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(d) } };
    const req = https.request(o, (res) => {
      if (res.statusCode !== 200) { let b = ''; res.on('data', x => b += x); res.on('end', () => reject(new Error(`${res.statusCode}: ${b}`))); return; }
      const c = []; res.on('data', x => c.push(x)); res.on('end', () => resolve(Buffer.concat(c)));
    }); req.on('error', reject); req.write(d); req.end();
  });
}

async function main() {
  const dir = path.join(BASE_DIR, 'audio/marlene-landucci');
  for (const { text, voice, file } of missing) {
    const fp = path.join(dir, file);
    if (fs.existsSync(fp)) { console.log(`SKIP: ${file}`); continue; }
    console.log(`GEN: ${text.substring(0,50)}...`);
    try { fs.writeFileSync(fp, await gen(text, voice)); await new Promise(r => setTimeout(r, 500)); }
    catch (e) { console.error(`ERR: ${e.message}`); }
  }
  console.log('\nAudioMap entries to add:');
  for (const { text, file } of missing) console.log('  "' + text + '": "/audio/marlene-landucci/' + file + '",');
}
main();
