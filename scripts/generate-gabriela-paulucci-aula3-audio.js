const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

const PHRASES = [
  // Vocab words (Arthur)
  { text: "Wake Up", voice: "arthur" },
  { text: "Eat", voice: "arthur" },
  { text: "Go", voice: "arthur" },
  { text: "Start", voice: "arthur" },
  { text: "Finish", voice: "arthur" },
  { text: "Morning", voice: "arthur" },
  { text: "Afternoon", voice: "arthur" },
  { text: "Night", voice: "arthur" },
  { text: "Breakfast", voice: "arthur" },
  { text: "Lunch", voice: "arthur" },

  // Sentences (alternate)
  { text: "I wake up at 7 in the morning.", voice: "ellen" },
  { text: "I eat breakfast at 8.", voice: "arthur" },
  { text: "I go to work at 9.", voice: "ellen" },
  { text: "I start work at 9 in the morning.", voice: "arthur" },
  { text: "I eat lunch at noon.", voice: "ellen" },
  { text: "I finish work at 6 in the afternoon.", voice: "arthur" },
  { text: "I go home at night.", voice: "ellen" },
  { text: "In the morning, I eat breakfast.", voice: "arthur" },
  { text: "In the afternoon, I work at Itau.", voice: "ellen" },
  { text: "At night, I go home.", voice: "arthur" },
  { text: "What time do you wake up?", voice: "ellen" },
  { text: "What do you eat for breakfast?", voice: "arthur" },
  { text: "I go to work by metro.", voice: "ellen" },
  { text: "I eat dinner at 8 at night.", voice: "arthur" },

  // Dialogue — David (Arthur)
  { text: "Good morning, Gabriela! Tell me about your day.", voice: "arthur" },
  { text: "What do you do first in the morning?", voice: "arthur" },
  { text: "What time do you go to work?", voice: "arthur" },
  { text: "What do you do at Itau?", voice: "arthur" },
  { text: "And what do you do at night?", voice: "arthur" },
  { text: "That sounds like a busy day!", voice: "arthur" },

  // Dialogue — Gabriela (Ellen)
  { text: "I wake up at 7. Then I eat breakfast.", voice: "ellen" },
  { text: "I go to work at 9. I take the metro.", voice: "ellen" },
  { text: "I start work at 9. I finish at 6.", voice: "ellen" },
  { text: "At night, I go home. I eat dinner at 8.", voice: "ellen" },
  { text: "Yes! I am very busy.", voice: "ellen" },
];

function toFilename(text) {
  return 'aula3_' + text
    .toLowerCase()
    .replace(/[^a-z0-9 ]/g, '')
    .replace(/ +/g, '_')
    .substring(0, 55);
}

async function generateAudio(phrase, voiceId, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: phrase,
      model_id: 'eleven_turbo_v2_5',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 },
    }),
  });
  if (!resp.ok) { const err = await resp.text(); throw new Error(`ElevenLabs error (${resp.status}): ${err}`); }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  if (!API_KEY) { console.error('ELEVENLABS_API_KEY not set'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  let generated = 0, skipped = 0;
  const seen = new Set();
  const uniquePhrases = PHRASES.filter(p => { const k = p.text.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });

  console.log(`Generating ${uniquePhrases.length} audio files for Lesson 3...`);

  for (const phrase of uniquePhrases) {
    const filename = toFilename(phrase.text) + '.mp3';
    const outputPath = path.join(OUTPUT_DIR, filename);
    const voiceId = phrase.voice === 'ellen' ? ELLEN_ID : ARTHUR_ID;

    if (fs.existsSync(outputPath)) { console.log(`  SKIP: ${filename}`); skipped++; }
    else {
      try {
        const bytes = await generateAudio(phrase.text, voiceId, outputPath);
        console.log(`  OK [${phrase.voice}]: ${filename} (${(bytes/1024).toFixed(1)}KB)`);
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (err) { console.error(`  FAIL: ${filename} — ${err.message}`); }
    }
  }

  console.log(`\nDone: ${generated} generated, ${skipped} skipped`);
}

main().catch(err => { console.error(err); process.exit(1); });
