const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'patricia-ruffo');
const PREFIX = 'aula5_';

// Áudios a regenerar:
// 1. Slide 5: trocar voz para ELLEN (alternância) — volume diferente pois voz diferente dos demais
// 2. Slide 16: networking audio FALTANTE — gerar com ELLEN (Patricia é mulher)
// 3. Slide 26: survival phrases 2 e 4 — trocar para ELLEN (alternância)
const PHRASES = [
  // Slide 5 — vocab cards com volume alto (regenerar com ELLEN para alternância)
  { text: "The keynote speaker presented groundbreaking research.", voice: ELLEN },
  { text: "The team reached a consensus on the new methodology.", voice: ELLEN },

  // Slide 16 — networking listening FALTANTE
  { text: "Dr. Ruffo, I really enjoyed your keynote. Your findings on glycemic control were fascinating. I have been working on a similar project in Tokyo. Dr. Nakamura mentioned that your methodology was very innovative. I was wondering if you would be open to a collaboration. If we combined our data, we would have the largest sample in this field. Could you elaborate on how you selected your control group? I would argue that a multi-center approach could strengthen the results. My recommendation is that we set up a meeting next month to discuss the details.", voice: ARTHUR },

  // Slide 26 — survival phrases 2 e 4 (regenerar com ELLEN para alternância)
  { text: "Based on the evidence, my recommendation is to continue the current approach.", voice: ELLEN },
  { text: "If we had more funding, we would replicate the study at a larger symposium.", voice: ELLEN },
];

function toFilename(text) {
  var clean = text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_');
  return (PREFIX + clean).substring(0, 60);
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

  console.log('Regenerating ' + PHRASES.length + ' audio files for Aula 5 fixes...');
  for (const p of PHRASES) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    const voiceName = p.voice === ELLEN ? 'Ellen' : 'Arthur';
    try {
      const size = await gen(p.text, p.voice, outPath);
      console.log('[OK] ' + voiceName + ' | ' + fname + ' (' + size + ' bytes)');
    } catch (e) {
      console.error('[FAIL] ' + fname + ': ' + e.message);
    }
  }
  console.log('Done! Networking audio filename for data-src:');
  console.log('/audio/patricia-ruffo/' + toFilename("Dr. Ruffo, I really enjoyed your keynote. Your findings on glycemic control were fascinating. I have been working on a similar project in Tokyo. Dr. Nakamura mentioned that your methodology was very innovative. I was wondering if you would be open to a collaboration. If we combined our data, we would have the largest sample in this field. Could you elaborate on how you selected your control group? I would argue that a multi-center approach could strengthen the results. My recommendation is that we set up a meeting next month to discuss the details.") + '.mp3');
}

main();
