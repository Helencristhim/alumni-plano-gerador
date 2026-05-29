const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

// Roberto = male → Arthur
// Check-in agent (female) = Ellen
// Single words (1-2) → ALWAYS Arthur
// Phrases (3+) → ALTERNATE Arthur/Ellen
const PHRASES = [
  // Vocab words (1-2 words → Arthur)
  { text: "Boarding pass", voice: ARTHUR },
  { text: "Gate", voice: ARTHUR },
  { text: "Check-in", voice: ARTHUR },
  { text: "Security", voice: ARTHUR },
  { text: "Passport", voice: ARTHUR },
  { text: "Delay", voice: ARTHUR },
  { text: "Announcement", voice: ARTHUR },
  { text: "Departure", voice: ARTHUR },

  // Vocab example sentences (alternate)
  { text: "Can I see your boarding pass, please?", voice: ARTHUR },
  { text: "My flight leaves from gate B7.", voice: ELLEN },
  { text: "I need to check in for my flight.", voice: ARTHUR },
  { text: "Please go through security.", voice: ELLEN },
  { text: "Do you have your passport ready?", voice: ARTHUR },
  { text: "There is a thirty-minute delay on flight AB4821.", voice: ELLEN },
  { text: "Attention please. Flight AB4821 is now boarding at gate B7.", voice: ARTHUR },
  { text: "The departure time is ten thirty AM.", voice: ELLEN },

  // Grammar in Context / narrative sentences (alternate)
  { text: "Roberto checked in at the counter.", voice: ARTHUR },
  { text: "He showed his passport.", voice: ELLEN },
  { text: "He waited at gate B7.", voice: ARTHUR },
  { text: "The agent asked: Window or aisle?", voice: ELLEN },
  { text: "He walked through security.", voice: ARTHUR },

  // Spot the error
  { text: "He check in yesterday", voice: ELLEN },
  { text: "He checked in yesterday.", voice: ARTHUR },

  // Dialogue — Check-in agent (female) = Ellen, Roberto (male) = Arthur
  { text: "Good morning, sir. May I see your passport and boarding pass?", voice: ELLEN },
  { text: "Of course. Here they are.", voice: ARTHUR },
  { text: "Are you checking any bags today?", voice: ELLEN },
  { text: "Yes, one suitcase. And I have a carry-on.", voice: ARTHUR },
  { text: "Window or aisle?", voice: ELLEN },
  { text: "Window, please.", voice: ARTHUR },
  { text: "Here is your boarding pass. Gate B7. Boarding starts at nine forty-five.", voice: ELLEN },
  { text: "Thank you. Where is security?", voice: ARTHUR },
  { text: "Straight ahead, then turn left.", voice: ELLEN },
  { text: "Thank you!", voice: ARTHUR },

  // Quick fire / practice phrases (alternate)
  { text: "I checked in online.", voice: ELLEN },
  { text: "Where is the departure board?", voice: ARTHUR },
  { text: "Excuse me, where is gate B7?", voice: ELLEN },
  { text: "I waited in line for twenty minutes.", voice: ARTHUR },
  { text: "The flight departed on time.", voice: ELLEN },
  { text: "I showed my passport at the counter.", voice: ARTHUR },
  { text: "They announced a gate change.", voice: ELLEN },

  // Survival / production phrases (alternate)
  { text: "Roberto checked in and showed his passport.", voice: ARTHUR },
  { text: "He asked about the gate and walked to security.", voice: ELLEN },
  { text: "She checked the reservation and printed the boarding pass.", voice: ARTHUR },
  { text: "They waited at the gate for thirty minutes.", voice: ELLEN },
  { text: "The pilot announced the delay.", voice: ARTHUR },
  { text: "We walked to gate B7 after security.", voice: ELLEN },
];

function toFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 60);
}

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

  const seen = new Set();
  const unique = PHRASES.filter(p => { const k = p.text.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });

  console.log('Generating ' + unique.length + ' audio files for Roberto Pires — Aula 4...');
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
    }
  }

  console.log('\nDone! Generated ' + unique.length + ' entries.');
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
