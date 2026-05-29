const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const missing = [
  { file: 'she_is_never_late_for_meetings.mp3', text: 'She is never late for meetings.', voice: ELLEN },
  { file: 'he_is_usually_in_the_office_by_8_am.mp3', text: 'He is usually in the office by 8 AM.', voice: ARTHUR },
  { file: 'he_is_sometimes_in_sao_paulo_v2.mp3', text: 'He is sometimes in São Paulo.', voice: ARTHUR },
];

const outDir = path.join(__dirname, '..', 'public', 'audio', 'maisa-de-oliveira-santos');

async function generate(item) {
  const url = `https://api.elevenlabs.io/v1/text-to-speech/${item.voice}`;
  const res = await fetch(url, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: item.text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
  });
  if (!res.ok) { console.error(`ERRO ${item.file}: ${res.status} ${await res.text()}`); return; }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(path.join(outDir, item.file), buf);
  console.log(`OK: ${item.file} (${buf.length} bytes)`);
}

(async () => {
  for (const item of missing) {
    await generate(item);
    await new Promise(r => setTimeout(r, 500));
  }
  console.log('Done!');
})();
