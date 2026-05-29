const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

const PHRASES = [
  { text: "Stunning", voice: ARTHUR, file: "aula4_stunning.mp3" },
  { text: "Breathtaking", voice: ARTHUR, file: "aula4_breathtaking.mp3" },
  { text: "Cozy", voice: ARTHUR, file: "aula4_cozy.mp3" },
  { text: "Crowded", voice: ARTHUR, file: "aula4_crowded.mp3" },
  { text: "Remote", voice: ARTHUR, file: "aula4_remote.mp3" },
  { text: "Vibrant", voice: ARTHUR, file: "aula4_vibrant.mp3" },
  { text: "Scenic", voice: ARTHUR, file: "aula4_scenic.mp3" },
  { text: "Ancient", voice: ARTHUR, file: "aula4_ancient.mp3" },
  { text: "Authentic", voice: ARTHUR, file: "aula4_authentic.mp3" },
  { text: "Unforgettable", voice: ARTHUR, file: "aula4_unforgettable.mp3" },
  { text: "The view from the mountain was absolutely stunning.", voice: ARTHUR, file: "aula4_stunning_sentence.mp3" },
  { text: "The sunset over the ocean was breathtaking.", voice: ELLEN, file: "aula4_breathtaking_sentence.mp3" },
  { text: "We stayed in a cozy little hotel near the beach.", voice: ARTHUR, file: "aula4_cozy_sentence.mp3" },
  { text: "The market was very crowded, but the atmosphere was amazing.", voice: ELLEN, file: "aula4_crowded_sentence.mp3" },
  { text: "The village was so remote that there was no internet.", voice: ARTHUR, file: "aula4_remote_sentence.mp3" },
  { text: "The city was vibrant, full of music and color.", voice: ELLEN, file: "aula4_vibrant_sentence.mp3" },
  { text: "We drove along the most scenic road I have ever seen.", voice: ARTHUR, file: "aula4_scenic_sentence.mp3" },
  { text: "We visited ancient temples that were over a thousand years old.", voice: ELLEN, file: "aula4_ancient_sentence.mp3" },
  { text: "The food was authentic and completely different from what we have at home.", voice: ARTHUR, file: "aula4_authentic_sentence.mp3" },
  { text: "That trip was the most unforgettable experience of my life.", voice: ELLEN, file: "aula4_unforgettable_sentence.mp3" },
  { text: "The place was...", voice: ARTHUR, file: "aula4_expr_place_was.mp3" },
  { text: "It was more... than I expected.", voice: ELLEN, file: "aula4_expr_more_than.mp3" },
  { text: "It was the most... place I have ever visited.", voice: ARTHUR, file: "aula4_expr_the_most.mp3" },
  { text: "What I loved most about it was...", voice: ELLEN, file: "aula4_expr_loved_most.mp3" },
  { text: "I would describe it as...", voice: ARTHUR, file: "aula4_expr_describe_as.mp3" },
  // Dialogue: James (tour guide) = Arthur, Pricila = Ellen
  { text: "Welcome aboard the Sydney Scenic Tour! My name is James, and I will be your guide today.", voice: ARTHUR, file: "aula4_dialogue_james_1.mp3" },
  { text: "This is stunning! The harbour is even more beautiful than in the photos.", voice: ELLEN, file: "aula4_dialogue_pricila_1.mp3" },
  { text: "On your left, you can see the Opera House. It is the most iconic building in Australia.", voice: ARTHUR, file: "aula4_dialogue_james_2.mp3" },
  { text: "It is breathtaking! I would describe it as the most elegant building I have ever seen.", voice: ELLEN, file: "aula4_dialogue_pricila_2.mp3" },
  { text: "Now we are entering The Rocks, one of the oldest and most vibrant neighborhoods in Sydney.", voice: ARTHUR, file: "aula4_dialogue_james_3.mp3" },
  { text: "It reminds me of the ancient neighborhoods I visited in Malta. But this is more colorful and more crowded.", voice: ELLEN, file: "aula4_dialogue_pricila_3.mp3" },
  { text: "If you want authentic Australian food, I recommend the market here. It is cozy and full of local flavors.", voice: ARTHUR, file: "aula4_dialogue_james_4.mp3" },
  { text: "This is already the most unforgettable day of my trip! What I love most about Sydney is how vibrant it feels.", voice: ELLEN, file: "aula4_dialogue_pricila_4.mp3" },
  // Listening 1: Pricila describes Canada trip (Ellen)
  { text: "Let me tell you about the most unforgettable trip of my life. In the year 2000, I traveled to Canada with my family. The scenery was absolutely stunning. We drove along the most scenic roads, surrounded by mountains and forests. The colors in autumn were more vibrant than anything I had seen before. We stayed in a cozy little cabin near a remote lake. There was no internet, no noise, just nature. The village nearby had authentic Canadian restaurants where we tried local food. It was more delicious than I expected. The most breathtaking moment was when we saw Niagara Falls. I remember thinking: this is the most beautiful place I have ever visited. Even though some tourist areas were crowded, the experience was unforgettable.", voice: ELLEN, file: "aula4_listening_1_canada_trip.mp3" },
  // Listening 2: James describes Australian highlights (Arthur)
  { text: "Australia is one of the most stunning countries on Earth. Sydney is a vibrant city with breathtaking views of the harbour. The Opera House is more impressive in person than in any photo. If you want something more remote, visit the Outback. It is the most ancient landscape you will ever see. The Great Barrier Reef is the most scenic natural wonder in the world. The water is crystal clear and the coral is more colorful than you can imagine. For authentic Australian food, try a local barbecue. Australians call it a barbie. Melbourne has the coziest cafes and the most vibrant street art scene in the country. And if you think Sydney is crowded, wait until you see the beaches in summer. Every trip to Australia is unforgettable.", voice: ARTHUR, file: "aula4_listening_2_australia_highlights.mp3" },
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
  console.log('Generating ' + PHRASES.length + ' audio files for Pricila Adamo — Aula 4...');
  let generated = 0, skipped = 0;
  for (const p of PHRASES) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }
  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + PHRASES.length);
}

main().catch(e => { console.error(e); process.exit(1); });
