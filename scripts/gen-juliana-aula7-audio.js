const fs = require('fs'), path = require('path');
const K = process.env.ELEVENLABS_API_KEY;
const G = '5vkxOzoz40FrElmLP4P7', J = 'rBqbBncz61jpuaOTI1GW';
const D = path.join(__dirname, '..', 'public', 'audio', 'juliana-marques');
const phrases = JSON.parse(fs.readFileSync('/tmp/aula7_phrases.json'));

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
  if (!K) { console.error('No key'); process.exit(1); }
  let g = 0, s = 0;
  for (let i = 0; i < phrases.length; i++) {
    const p = phrases[i];
    const o = path.join(D, p.file);
    if (fs.existsSync(o)) { s++; continue; }
    const voice = i % 2 === 0 ? G : J;
    try {
      const sz = await gen(p.text, voice, o);
      console.log('OK: ' + p.file + ' (' + Math.round(sz / 1024) + 'KB)');
      g++;
      await new Promise(r => setTimeout(r, 500));
    } catch (e) { console.error('ERR: ' + p.file + ' ' + e.message); }
  }
  console.log('Gen: ' + g + ' Skip: ' + s);
}
main();
