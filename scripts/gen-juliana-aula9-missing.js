const fs = require('fs'), path = require('path');
const K = process.env.ELEVENLABS_API_KEY;
const G = '5vkxOzoz40FrElmLP4P7'; // Female Spanish voice (same as other Juliana scripts)
const D = path.join(__dirname, '..', 'public', 'audio', 'juliana-marques');

async function gen(t, v, o) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + v, {
    method: 'POST', headers: { 'xi-api-key': K, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: t, model_id: 'eleven_multilingual_v2', voice_settings: { stability: .5, similarity_boost: .75, style: 0, use_speaker_boost: true } })
  });
  if (!r.ok) throw new Error(r.status);
  const b = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(o, b);
  return b.length;
}

async function main() {
  if (!K) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  const file = 'aula9_yo_vengo_reunion_importante.mp3';
  const out = path.join(D, file);
  if (fs.existsSync(out)) { console.log('Already exists: ' + file); return; }
  try {
    const sz = await gen('Yo vengo de una reunión importante.', G, out);
    console.log('OK: ' + file + ' (' + Math.round(sz / 1024) + 'KB)');
  } catch (e) { console.error('ERR: ' + file + ' ' + e.message); }
}
main();
