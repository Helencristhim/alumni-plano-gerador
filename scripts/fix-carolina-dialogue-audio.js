const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carolina-paludetto-rodrigues');

const PHRASES = [
  { text: "Hi! I am Alex. I am a new exchange student. What is your name?", file: "dialogue_alex_1.mp3", voice: ARTHUR },
  { text: "Hi Alex! My name is Carolina. Nice to meet you! Where are you from?", file: "dialogue_carolina_1.mp3", voice: ELLEN },
  { text: "I am from Canada. So, what do you like to do? Any hobbies?", file: "dialogue_alex_2.mp3", voice: ARTHUR },
  { text: "I play handball twice a week. And I love writing creative stories!", file: "dialogue_carolina_2.mp3", voice: ELLEN },
  { text: "Cool! Are you good at English?", file: "dialogue_alex_3.mp3", voice: ARTHUR },
  { text: "I struggle with grammar, but I want to improve. My goal is to feel more confident speaking.", file: "dialogue_carolina_3.mp3", voice: ELLEN },
  { text: "That is a great goal! I can help you practice if you want.", file: "dialogue_alex_4.mp3", voice: ARTHUR },
  { text: "Yes, I would love that! Thanks, Alex!", file: "dialogue_carolina_4.mp3", voice: ELLEN },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  for (const p of PHRASES) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); continue; }
    try {
      const size = await gen(p.text, p.voice, outPath);
      console.log('OK: ' + p.file + ' (' + Math.round(size/1024) + ' KB)');
      await new Promise(r => setTimeout(r, 500));
    } catch(e) { console.error('FAIL: ' + p.file + ' - ' + e.message); }
  }
  console.log('Done!');
}
main();
