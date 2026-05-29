const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

const PHRASES = [
  // Review combined phrases (alternate voices)
  { text: "My name is Gabriela. I am 33 years old. I am from Jau.", voice: "ellen" },
  { text: "I live in Sao Paulo. I work at Itau.", voice: "arthur" },
  { text: "This is my phone. It is black.", voice: "ellen" },
  { text: "That is my bag. It is big.", voice: "arthur" },
  { text: "I wake up at 7. I eat breakfast at 8.", voice: "ellen" },
  { text: "I go to work at 9. I finish at 6.", voice: "arthur" },
  { text: "My mother lives in Jau. She is 58.", voice: "ellen" },
  { text: "My father works at a hospital.", voice: "arthur" },
  { text: "We eat dinner together on Sundays.", voice: "ellen" },
  { text: "She speaks English and Portuguese.", voice: "arthur" },

  // Dialogue prompts (Arthur = David)
  { text: "Tell me about yourself, Gabriela.", voice: "arthur" },
  { text: "Describe your daily routine.", voice: "arthur" },
  { text: "Who is important in your life?", voice: "arthur" },

  // Celebration
  { text: "I am proud of my English!", voice: "ellen" },
];

function toFilename(text) {
  return 'aula5_' + text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 55);
}

async function generateAudio(phrase, voiceId, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: phrase, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
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
  const unique = PHRASES.filter(p => { const k = p.text.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });
  console.log(`Generating ${unique.length} audio files for Lesson 5...`);
  for (const phrase of unique) {
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
