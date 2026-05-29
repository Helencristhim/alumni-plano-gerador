const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

// Roberto = male → Arthur
// Airport agent (female) = Ellen
// Single words (1-2) → ALWAYS Arthur
// Phrases (3+) → ALTERNATE Arthur/Ellen
const PHRASES = [
  // Vocab words (1-2 words → Arthur)
  { text: "Luggage", voice: ARTHUR },
  { text: "Claim", voice: ARTHUR },
  { text: "Carousel", voice: ARTHUR },
  { text: "Missing", voice: ARTHUR },
  { text: "Report", voice: ARTHUR },
  { text: "Describe", voice: ARTHUR },
  { text: "Suitcase", voice: ARTHUR },
  { text: "Lost and Found", voice: ARTHUR },

  // Grammar in Context / narrative sentences (alternate)
  { text: "Roberto went to baggage claim.", voice: ARTHUR },
  { text: "Someone took his bag.", voice: ELLEN },
  { text: "He left it at check-in.", voice: ARTHUR },
  { text: "They found it.", voice: ELLEN },

  // Spot the error
  { text: "He went to the airport.", voice: ARTHUR },
  { text: "He goed to the airport.", voice: ELLEN },

  // Dialogue — Airport agent (female) = Ellen, Roberto (male) = Arthur
  { text: "Excuse me, my luggage is missing. I need to report a lost bag.", voice: ARTHUR },
  { text: "I am sorry to hear that. Can you describe your suitcase?", voice: ELLEN },
  { text: "It is a blue medium suitcase with a black handle.", voice: ARTHUR },
  { text: "What flight were you on?", voice: ELLEN },
  { text: "I was on flight AB4821 from Sao Paulo.", voice: ARTHUR },
  { text: "Let me check. We found a bag matching that description.", voice: ELLEN },
  { text: "Where did you find it?", voice: ARTHUR },
  { text: "Someone took the wrong bag by mistake. We brought it to Lost and Found.", voice: ELLEN },
  { text: "Thank you so much.", voice: ARTHUR },
  { text: "You are welcome. Here is your suitcase.", voice: ELLEN },

  // Survival / practice phrases (alternate)
  { text: "My luggage did not arrive.", voice: ARTHUR },
  { text: "I need to report a missing bag.", voice: ELLEN },
  { text: "Can you describe your suitcase?", voice: ARTHUR },
  { text: "Someone took my bag by mistake.", voice: ELLEN },
  { text: "They found it at Lost and Found.", voice: ARTHUR },

  // Fill-in / quiz phrases (alternate)
  { text: "I waited at the carousel but my bag did not come.", voice: ELLEN },
  { text: "We lost your bag. We will bring it to your hotel.", voice: ARTHUR },

  // Quick fire phrases (alternate)
  { text: "My bag didn't arrive.", voice: ELLEN },
  { text: "I need to report a lost bag.", voice: ARTHUR },
  { text: "When will it come?", voice: ELLEN },
  { text: "Can you bring it to my hotel?", voice: ARTHUR },

  // Production / speech phrases (alternate)
  { text: "My flight landed but my bag is missing.", voice: ELLEN },
  { text: "I went to baggage claim and waited.", voice: ARTHUR },
  { text: "The agent said they found it.", voice: ELLEN },
  { text: "They brought it to my hotel that night.", voice: ARTHUR },
  { text: "I lost my suitcase at the airport.", voice: ELLEN },
  { text: "He came to the counter and reported it.", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Roberto Pires — Aula 5...');
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
