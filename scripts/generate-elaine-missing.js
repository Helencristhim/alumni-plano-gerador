const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'elaine-mieko-pinho');

// Missing phrases from HTML that don't have MP3s yet
// Alternating Arthur/Ellen for variety
const MISSING = [
  { text: "I need my passport to board the plane.", voice: "ellen" },
  { text: "My flight is at 9 AM.", voice: "arthur" },
  { text: "The check-in desk is on the left.", voice: "ellen" },
  { text: "I have a reservation for two nights.", voice: "arthur" },
  { text: "New York is my destination.", voice: "ellen" },
  { text: "The housekeeper cleaned my room.", voice: "arthur" },
  { text: "Call 911 in an emergency.", voice: "ellen" },
  { text: "Hi! Is this seat 14B? I am Sarah.", voice: "ellen" },
  { text: "Hello! Yes, I am in 14A. I am Elaine. Nice to meet you!", voice: "arthur" },
  { text: "Nice to meet you too! Where are you from?", voice: "ellen" },
  { text: "I am from Sao Paulo, Brazil. What about you?", voice: "arthur" },
  { text: "I am from London. Is New York your destination?", voice: "ellen" },
  { text: "Yes! I have a reservation at a hotel in Manhattan. I am very excited!", voice: "arthur" },
  { text: "That sounds wonderful! Is your luggage heavy?", voice: "ellen" },
  { text: "Yes, it is very heavy! I have too many clothes.", voice: "arthur" },
  { text: "My name is Elaine. I am from Sao Paulo.", voice: "arthur" },
  { text: "I have a reservation under Pinho.", voice: "ellen" },
  { text: "Excuse me, where is gate B12?", voice: "arthur" },
  { text: "Can you help me, please?", voice: "ellen" },
  { text: "This is an emergency. Please call 911.", voice: "arthur" },
];

function toFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 60);
}

async function generateAudio(phrase, voiceId, outputPath) {
  const resp = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: phrase, model_id: 'eleven_turbo_v2_5', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!resp.ok) throw new Error('ElevenLabs ' + resp.status + ': ' + (await resp.text()));
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  if (!API_KEY) { console.error('No API key'); process.exit(1); }
  const newMapEntries = {};

  for (const p of MISSING) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(OUTPUT_DIR, fname);
    const voiceId = p.voice === 'ellen' ? ELLEN_ID : ARTHUR_ID;

    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
    } else {
      try {
        const bytes = await generateAudio(p.text, voiceId, outPath);
        console.log('OK [' + p.voice + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch (err) {
        console.error('FAIL: ' + fname + ' — ' + err.message);
      }
    }
    newMapEntries[p.text] = '/audio/elaine-mieko-pinho/' + fname;
  }

  // Output audioMap additions
  console.log('\n// ADD to audioMap:');
  Object.entries(newMapEntries).forEach(([k, v]) => {
    console.log('  "' + k.replace(/"/g, '\\"') + '": "' + v + '",');
  });
}

main().catch(err => { console.error(err); process.exit(1); });
