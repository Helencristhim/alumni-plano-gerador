const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const RACHEL = '21m00Tcm4TlvDq8ikWAM';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

const PHRASES = [
  // Survival phrases (protagonist = ellen)
  { text: "The place was absolutely stunning.", voice: ELLEN, file: "aula4_surv_place_stunning.mp3" },
  { text: "It was more beautiful than I expected.", voice: ELLEN, file: "aula4_surv_more_beautiful.mp3" },
  { text: "It was the most unforgettable experience of my life.", voice: ELLEN, file: "aula4_surv_most_unforgettable.mp3" },
  { text: "I would describe it as breathtaking.", voice: ELLEN, file: "aula4_surv_describe_breathtaking.mp3" },
  { text: "What I loved most about it was the scenery.", voice: ELLEN, file: "aula4_surv_loved_scenery.mp3" },
  // Dialogue — Lena (rachel) and Pricila (ellen)
  { text: "Hi! I could not help overhearing you speaking Portuguese. I am Lena, from Germany. I just came back from Greece!", voice: RACHEL, file: "aula4_d_lena_1.mp3" },
  { text: "Oh, how lovely! I am Pricila, from Brazil. I have always wanted to visit Greece. Was it stunning?", voice: ELLEN, file: "aula4_d_pricila_1.mp3" },
  { text: "It was the most breathtaking place I have ever visited. The islands were more beautiful than any photo. And the food was so authentic!", voice: RACHEL, file: "aula4_d_lena_2.mp3" },
  { text: "That sounds unforgettable! I traveled to Canada once. The scenery was more scenic than I expected. We stayed in a cozy hotel in a remote village.", voice: ELLEN, file: "aula4_d_pricila_2.mp3" },
  { text: "I love remote places! Greece was vibrant and crowded in Athens, but the islands were peaceful. What I loved most was the ancient architecture.", voice: RACHEL, file: "aula4_d_lena_3.mp3" },
  { text: "For me, Canada was more challenging than I imagined because of English. But the people were the friendliest I have ever met.", voice: ELLEN, file: "aula4_d_pricila_3.mp3" },
  { text: "I would describe Greece as the most authentic experience of my life. You should definitely go! It is more affordable than people think.", voice: RACHEL, file: "aula4_d_lena_4.mp3" },
  { text: "It is on my bucket list now! I would describe my dream trip to Australia as the most exciting adventure ahead of me.", voice: ELLEN, file: "aula4_d_pricila_4.mp3" },
  // Listening 2 — Sydney tour (narrator = arthur)
  { text: "Welcome to the Sydney Scenic Tour. Today we will explore one of the most stunning cities in the world. Sydney is more vibrant than most people expect. The harbor is breathtaking, especially at sunset. We will visit the ancient rocks area, one of the oldest neighborhoods in Australia. The streets are crowded with tourists, but the atmosphere is authentic and unforgettable. Our first stop is a cozy cafe near the Opera House, where you can enjoy the most scenic views of the harbor bridge. Later, we will drive along a remote coastal road that is more beautiful than any postcard. This tour will be the most unforgettable experience of your trip to Australia.", voice: ARTHUR, file: "aula4_listening_2_sydney_tour.mp3" },
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
  console.log('Done! Generated', PHRASES.length, 'audio files for aula4 missing.');
})();
