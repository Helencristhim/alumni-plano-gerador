const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-pelizaro');

const PHRASES = [
  { text: "He leads a remote team of twelve developers.", file: "he_leads_a_remote_team_of_twelve.mp3", voice: ELLEN },
  { text: "I need to report our progress to the board.", file: "i_need_to_report_our_progress_board.mp3", voice: ARTHUR },
];

async function generate(phrase) {
  const filepath = path.join(DIR, phrase.file);
  if (fs.existsSync(filepath)) { console.log(`SKIP ${phrase.file}`); return; }
  console.log(`Generating: ${phrase.text} → ${phrase.file}`);
  const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${phrase.voice}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: phrase.text, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
  });
  if (!res.ok) { console.error(`FAIL ${phrase.file}: ${res.status}`); return; }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(filepath, buf);
  console.log(`OK ${phrase.file} (${buf.length} bytes)`);
}

(async () => {
  for (const p of PHRASES) await generate(p);
  console.log('Done!');
})();
