const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

const PHRASES = [
  // Survival phrases (advice context — alternate voices)
  { text: "You should take care of yourself.", voice: ARTHUR, file: "aula5_surv_you_should.mp3" },
  { text: "You could try meditation.", voice: ELLEN, file: "aula5_surv_you_could.mp3" },
  { text: "It might help to go for a walk.", voice: ARTHUR, file: "aula5_surv_it_might.mp3" },
  { text: "I would recommend getting more sleep.", voice: ELLEN, file: "aula5_surv_recommend.mp3" },
  { text: "The best thing you could do is start small.", voice: ARTHUR, file: "aula5_surv_best_thing.mp3" },
];

async function generate(text, voiceId, filename) {
  const filepath = path.join(DIR, filename);
  if (fs.existsSync(filepath)) { console.log('SKIP (exists):', filename); return; }
  console.log('Generating:', filename);
  const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
    })
  });
  if (!res.ok) { console.error('FAIL:', filename, res.status, await res.text()); return; }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(filepath, buf);
  console.log('OK:', filename, (buf.length/1024).toFixed(1)+'KB');
}

(async () => {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });
  for (const p of PHRASES) {
    await generate(p.text, p.voice, p.file);
    await new Promise(r => setTimeout(r, 500));
  }
  console.log('Done! Generated', PHRASES.length, 'audio files for aula5 missing.');
})();
