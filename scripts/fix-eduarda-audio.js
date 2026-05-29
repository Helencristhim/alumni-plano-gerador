const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const missing = [
  { file: 'aula3_ex_estimate.mp3', text: 'We estimate the deal value at approximately two hundred million dollars.', voice: ELLEN },
  { file: 'aula3_ex_quarter.mp3', text: 'Revenue in the third quarter exceeded our forecast.', voice: ARTHUR },
  { file: 'aula3_fill1.mp3', text: 'Revenue declined by eight percent in the third quarter.', voice: ELLEN },
  { file: 'aula3_fill2.mp3', text: 'We estimate the deal value at approximately two hundred million dollars.', voice: ARTHUR },
  { file: 'aula3_pron2.mp3', text: 'We estimate the deal value at approximately two hundred million dollars.', voice: ELLEN },
  { file: 'aula3_ex_margin.mp3', text: 'The operating margin improved from fifteen to twenty percent.', voice: ARTHUR },
  { file: 'aula4_ex_file_for_bankruptcy.mp3', text: 'The company has filed for bankruptcy under Chapter 11.', voice: ELLEN },
  { file: 'aula4_ex_conduct_due_diligence.mp3', text: 'We have conducted due diligence on the target company.', voice: ARTHUR },
  { file: 'aula4_fill4.mp3', text: 'Have you conducted due diligence yet?', voice: ELLEN },
  { file: 'aula4_fill5.mp3', text: 'The team has already submitted the proposal.', voice: ARTHUR },
  { file: 'aula4_dial3.mp3', text: 'Have you conducted due diligence yet?', voice: ELLEN },
];

const outDir = path.join(__dirname, '..', 'public', 'audio', 'eduarda-gabriel');

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
