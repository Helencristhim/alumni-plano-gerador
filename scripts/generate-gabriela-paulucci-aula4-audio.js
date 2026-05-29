const fs = require('fs');
const path = require('path');
const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

const PHRASES = [
  { text: "Mother", voice: "arthur" },
  { text: "Father", voice: "arthur" },
  { text: "Brother", voice: "arthur" },
  { text: "Sister", voice: "arthur" },
  { text: "Friend", voice: "arthur" },
  { text: "Lives", voice: "arthur" },
  { text: "Works", voice: "arthur" },
  { text: "Speaks", voice: "arthur" },
  { text: "Family", voice: "arthur" },
  { text: "Together", voice: "arthur" },
  { text: "My mother lives in Jau.", voice: "ellen" },
  { text: "My father works at a hospital.", voice: "arthur" },
  { text: "My brother lives in Sao Paulo.", voice: "ellen" },
  { text: "My sister speaks English.", voice: "arthur" },
  { text: "My friend works at Itau.", voice: "ellen" },
  { text: "She lives in Jau.", voice: "arthur" },
  { text: "He works every day.", voice: "ellen" },
  { text: "They eat lunch together.", voice: "arthur" },
  { text: "My family is very important to me.", voice: "ellen" },
  { text: "We eat dinner together at night.", voice: "arthur" },
  { text: "He speaks Portuguese and English.", voice: "ellen" },
  { text: "She wakes up at 6 in the morning.", voice: "arthur" },
  { text: "They live in Brazil.", voice: "ellen" },
  { text: "My mother is 58 years old.", voice: "arthur" },
  { text: "Tell me about your family, Gabriela.", voice: "arthur" },
  { text: "Do you have brothers or sisters?", voice: "arthur" },
  { text: "I have one brother. He lives in Sao Paulo.", voice: "ellen" },
  { text: "Where does your mother live?", voice: "arthur" },
  { text: "My mother lives in Jau. She is 58 years old.", voice: "ellen" },
  { text: "And your father? What does he do?", voice: "arthur" },
  { text: "My father works at a hospital. He wakes up very early.", voice: "ellen" },
  { text: "Do you see your family often?", voice: "arthur" },
  { text: "We eat dinner together on Sundays.", voice: "ellen" },
  { text: "That is wonderful! Family is important.", voice: "arthur" },
  { text: "Yes! My family is very important to me.", voice: "ellen" },
];

function toFilename(text) {
  return 'aula4_' + text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 55);
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
  console.log(`Generating ${unique.length} audio files for Lesson 4...`);
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
