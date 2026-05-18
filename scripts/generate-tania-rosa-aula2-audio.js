const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tania-rosa-aula2');

// Voice rules:
// Single words (1-2 words) = ALWAYS Arthur
// Phrases (3+ words) = ALTERNATE Arthur/Ellen
// Dialogue: Agent = Arthur, Tânia = Ellen
const PHRASES = [
  // ===== Vocab words (1-2 words → Arthur) =====
  { text: "Flight", voice: ARTHUR },
  { text: "Boarding Pass", voice: ARTHUR },
  { text: "Gate", voice: ARTHUR },
  { text: "Luggage", voice: ARTHUR },
  { text: "Check-in", voice: ARTHUR },
  { text: "Terminal", voice: ARTHUR },
  { text: "Departure", voice: ARTHUR },
  { text: "Arrival", voice: ARTHUR },
  { text: "Travel", voice: ARTHUR },
  { text: "Destination", voice: ARTHUR },
  { text: "Passport", voice: ARTHUR },
  { text: "Country", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "My flight to London departs at 10 AM.", voice: ARTHUR },
  { text: "Could I see your boarding pass, please?", voice: ELLEN },
  { text: "Your gate is B12.", voice: ARTHUR },
  { text: "I need to check my luggage.", voice: ELLEN },
  { text: "Could I check in for my flight, please?", voice: ARTHUR },
  { text: "The international terminal is on the left.", voice: ELLEN },
  { text: "The departure time is 3:30 PM.", voice: ARTHUR },
  { text: "The arrival time in Paris is 8 PM.", voice: ELLEN },

  // ===== Context / narrative sentences (alternate) =====
  { text: "Tânia is at the airport. She is checking in for her flight to Paris.", voice: ELLEN },
  { text: "She could not find her gate at first, but an agent helped her.", voice: ARTHUR },

  // ===== Grammar practice / polite requests (alternate) =====
  { text: "Could I have a window seat, please?", voice: ELLEN },
  { text: "Can you help me with my luggage?", voice: ARTHUR },
  { text: "The agent asks: Can I see your boarding pass?", voice: ELLEN },
  { text: "Her departure time is 3:30 PM from gate B7.", voice: ARTHUR },

  // ===== Speech / practice phrases (alternate) =====
  { text: "I could not find my gate.", voice: ELLEN },
  { text: "Could you tell me where Terminal B is?", voice: ARTHUR },
  { text: "Could you help me with my luggage, please?", voice: ELLEN },
  { text: "Could you tell me the departure time, please?", voice: ARTHUR },
  { text: "Where is gate B7?", voice: ELLEN },

  // ===== Dialogue — Agent = Arthur, Tânia = Ellen =====
  { text: "Good morning! Welcome to International Airlines. Could I see your passport, please?", voice: ARTHUR },
  { text: "Good morning! Here is my passport. I am flying to Paris.", voice: ELLEN },
  { text: "Thank you, Mrs. Rosa. Could I see your booking confirmation?", voice: ARTHUR },
  { text: "Yes, here it is. Could I have a window seat, please?", voice: ELLEN },
  { text: "Of course! I have seat 14A for you. Are you checking any luggage today?", voice: ARTHUR },
  { text: "Yes, I have one suitcase. How much luggage can I take?", voice: ELLEN },
  { text: "You can check one bag up to 23 kilos. Could I see your luggage?", voice: ARTHUR },
  { text: "Here it is. Could you tell me where my gate is?", voice: ELLEN },
  { text: "Your gate is B7. Departure is at 3:30 PM. Here is your boarding pass.", voice: ARTHUR },
  { text: "Thank you very much! Could you tell me where Terminal B is?", voice: ELLEN },

  // ===== Additional practice phrases (alternate) =====
  { text: "Here is my passport.", voice: ARTHUR },
  { text: "Excuse me, could you tell me where gate B7 is?", voice: ELLEN },
  { text: "Yes, please. I am looking for Terminal B.", voice: ARTHUR },
  { text: "Good morning! I am checking in for my flight to Paris.", voice: ELLEN },
  { text: "Could I have an aisle seat, please?", voice: ARTHUR },
  { text: "Excuse me, could you tell me where Terminal B is?", voice: ELLEN },
  { text: "I am flying to Paris. My flight departs at 3:30 PM.", voice: ARTHUR },
  { text: "How much luggage can I take, please?", voice: ELLEN },
  { text: "Thank you! Could you tell me where gate B7 is?", voice: ARTHUR },

  // ===== Short practice phrases (alternate) =====
  { text: "I want a window seat.", voice: ELLEN },
  { text: "Where is the gate?", voice: ARTHUR },
  { text: "Can I see your passport?", voice: ELLEN },
  { text: "She could not find her luggage.", voice: ARTHUR },
  { text: "The flight departs at 3 PM.", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Tânia Rosa — Aula 2...');
  let generated = 0;
  let skipped = 0;
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
      skipped++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total entries: ' + unique.length);
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
