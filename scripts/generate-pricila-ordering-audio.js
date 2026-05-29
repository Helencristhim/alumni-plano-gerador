const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

// Each ordering audio = the CORRECT sequence read as a continuous paragraph
const PHRASES = [
  {
    text: "She grew up in Araras, Sao Paulo. She graduated from dental school in 1995. She opened her own dental clinic in Araras. She traveled to Canada and overcame her fear of speaking English. Now she is preparing for retirement — her next chapter.",
    voice: ELLEN,
    file: "order_l2_life_chapters.mp3"
  },
  {
    text: "I am going to retire next year. Freedom is my priority. My goal is to change my lifestyle and find a new purpose. I am planning to visit the places on my bucket list. I am going to explore Australia and embrace new adventures. I believe this will be the best chapter of my life.",
    voice: ARTHUR,
    file: "order_l3_retirement_plans.mp3"
  },
  {
    text: "We arrived at a stunning beach town on the first day. We checked into a cozy little hotel near the vibrant market. The scenic views along the coast were more breathtaking than any photo. We ate authentic food and explored ancient ruins. It was the most unforgettable trip of my life.",
    voice: ELLEN,
    file: "order_l4_travel_description.mp3"
  },
  {
    text: "It might help to drink more water. You could try walking thirty minutes a day. You should see a doctor about those symptoms.",
    voice: ARTHUR,
    file: "order_l5_wellness_advice.mp3"
  },
];

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
  console.log('Generating ' + PHRASES.length + ' ordering audio files...');
  for (const p of PHRASES) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); continue; }
    try {
      const bytes = await gen(p.text, p.voice, outPath);
      console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes/1024).toFixed(1) + 'KB)');
      await new Promise(r => setTimeout(r, 500));
    } catch(e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
  }
  console.log('Done!');
}

main().catch(e => { console.error(e); process.exit(1); });
