const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'percival-jr-aula2');

// Percival = male → Arthur
// Receptionist/Officer = female → Ellen
// Single words (1-2) → ALWAYS Arthur
// Phrases (3+) → ALTERNATE Arthur/Ellen
const PHRASES = [
  // Survival / emergency (alternate)
  { text: "I have a reservation under the name Percival.", voice: ARTHUR },
  { text: "I am here on vacation.", voice: ELLEN },
  { text: "Could you help me with my luggage?", voice: ARTHUR },
  { text: "Where is the elevator?", voice: ELLEN },
  { text: "I am going to stay for ten days.", voice: ARTHUR },

  // Vocab words (1-2 words → Arthur)
  { text: "Passport", voice: ARTHUR },
  { text: "Customs", voice: ARTHUR },
  { text: "Declaration", voice: ARTHUR },
  { text: "Carry-on", voice: ARTHUR },
  { text: "Boarding pass", voice: ARTHUR },
  { text: "Reservation", voice: ARTHUR },
  { text: "Front desk", voice: ARTHUR },
  { text: "Room key", voice: ARTHUR },
  { text: "Luggage", voice: ARTHUR },
  { text: "Floor", voice: ARTHUR },

  // Vocab example sentences (alternate)
  { text: "Could I see your passport, please?", voice: ELLEN },
  { text: "We went through customs at JFK.", voice: ARTHUR },
  { text: "I have nothing to declare.", voice: ELLEN },
  { text: "My carry-on is in the overhead bin.", voice: ARTHUR },
  { text: "Here is my boarding pass.", voice: ELLEN },
  { text: "Could you call the front desk?", voice: ARTHUR },
  { text: "Here is your room key.", voice: ELLEN },
  { text: "Could you help me with my luggage, please?", voice: ARTHUR },
  { text: "My room is on the tenth floor.", voice: ELLEN },

  // Fill-in phrases (alternate)
  { text: "I arrived at JFK Airport yesterday.", voice: ARTHUR },
  { text: "He went through customs without problems.", voice: ELLEN },
  { text: "I am going to stay for ten days in New York.", voice: ARTHUR },

  // Speech cards
  { text: "My name is Percival. I work at EGEA Saneamento.", voice: ARTHUR },

  // Immigration dialogue — Officer = Ellen, Percival = Arthur
  { text: "Good morning. Passport, please.", voice: ELLEN },
  { text: "Here you go.", voice: ARTHUR },
  { text: "What is the purpose of your visit?", voice: ELLEN },
  { text: "I am here on vacation with my wife.", voice: ARTHUR },
  { text: "How long are you going to stay?", voice: ELLEN },
  { text: "We are going to stay for ten days.", voice: ARTHUR },
  { text: "Where are you staying?", voice: ELLEN },
  { text: "At the Marriott Hotel in Manhattan.", voice: ARTHUR },
  { text: "Enjoy your trip.", voice: ELLEN },
  { text: "Thank you!", voice: ARTHUR },

  // Hotel dialogue — Receptionist = Ellen, Percival = Arthur
  { text: "Good evening! Welcome to the Marriott. How can I help you?", voice: ELLEN },
  { text: "Let me check. Yes, a king room for ten nights. Could I see your passport?", voice: ELLEN },
  { text: "Of course. Here it is.", voice: ARTHUR },
  { text: "Thank you. Your room is on the fifteenth floor. Here is your room key.", voice: ELLEN },
  { text: "Thank you. Could you help me with my luggage?", voice: ARTHUR },
  { text: "Of course! The elevator is on your left. Is there anything else?", voice: ELLEN },
  { text: "Yes. Could you recommend a good restaurant nearby?", voice: ARTHUR },

  // Concierge dialogue (Listening 2)
  { text: "Excuse me, could you help me? I am looking for a good Italian restaurant near the hotel.", voice: ARTHUR },
  { text: "Of course, sir. There is an excellent Italian restaurant two blocks from here. It is called Carbone.", voice: ELLEN },
  { text: "How do I get there?", voice: ARTHUR },
  { text: "Go right out of the hotel, walk two blocks, and it is on your left.", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Percival JR — Aula 2...');
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
