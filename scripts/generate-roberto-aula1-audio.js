const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

// Roberto = male → Arthur
// Flight attendant (female) = Ellen
// Single words (1-2) → ALWAYS Arthur
// Phrases (3+) → ALTERNATE Arthur/Ellen
const PHRASES = [
  // Vocab words (1-2 words → Arthur)
  { text: "Travel", voice: ARTHUR },
  { text: "Trip", voice: ARTHUR },
  { text: "Airport", voice: ARTHUR },
  { text: "Hotel", voice: ARTHUR },
  { text: "Restaurant", voice: ARTHUR },
  { text: "City", voice: ARTHUR },

  // Vocab example sentences (alternate)
  { text: "I want to travel to Barcelona this summer.", voice: ARTHUR },
  { text: "This trip will be amazing.", voice: ELLEN },
  { text: "I need to go to the airport early.", voice: ARTHUR },
  { text: "My hotel is near the city center.", voice: ELLEN },
  { text: "I want to find a good restaurant tonight.", voice: ARTHUR },
  { text: "Barcelona is a beautiful city.", voice: ELLEN },

  // Speech cards (Roberto = Arthur)
  { text: "Hi, I am Roberto. I am from Sao Paulo.", voice: ARTHUR },
  { text: "I am a businessman from Brazil.", voice: ELLEN },
  { text: "I want to travel to Barcelona and Paris.", voice: ARTHUR },
  { text: "I need a hotel near the city center.", voice: ELLEN },
  { text: "I like good restaurants.", voice: ARTHUR },

  // Grammar in Context sentences (alternate)
  { text: "Roberto lives in Sao Paulo.", voice: ELLEN },
  { text: "He works every day.", voice: ARTHUR },
  { text: "She does not like cold weather.", voice: ELLEN },
  { text: "Does he travel for business?", voice: ARTHUR },

  // Dialogue — Flight attendant (female) = Ellen, Roberto (male) = Arthur
  { text: "Hello! Welcome aboard. Where are you flying today?", voice: ELLEN },
  { text: "Hi! I am going to Barcelona. It is my first time.", voice: ARTHUR },
  { text: "That is wonderful! I love Barcelona. Do you travel often?", voice: ELLEN },
  { text: "Not really. I usually work in Sao Paulo. But I want to visit new cities.", voice: ARTHUR },
  { text: "What do you do?", voice: ELLEN },
  { text: "I am a businessman. I work with technology.", voice: ARTHUR },
  { text: "Nice! Do you like European food?", voice: ELLEN },
  { text: "Yes, I do. I want to find good restaurants in Barcelona.", voice: ARTHUR },
  { text: "You need to try the tapas! Does your wife travel with you?", voice: ELLEN },
  { text: "Yes, she does. We like to travel together.", voice: ARTHUR },

  // Quick fire questions (alternate voices for questions, Arthur for Roberto answers)
  { text: "You arrive at the airport. The officer asks: Where are you going?", voice: ELLEN },
  { text: "I am going to Barcelona.", voice: ARTHUR },
  { text: "At the hotel, they ask: Do you have a reservation?", voice: ELLEN },
  { text: "Yes, I do. My name is Roberto Pires.", voice: ARTHUR },
  { text: "A person asks: What do you do?", voice: ELLEN },
  { text: "I am a businessman from Sao Paulo.", voice: ARTHUR },
  { text: "Someone asks: Do you like this city?", voice: ELLEN },
  { text: "Yes, I do. Barcelona is a beautiful city.", voice: ARTHUR },
  { text: "A waiter asks: Do you want a table for two?", voice: ELLEN },
  { text: "Yes, please. We want a table near the window.", voice: ARTHUR },
  { text: "Your wife asks: Do you like the hotel?", voice: ELLEN },
  { text: "Yes, I do. The hotel is very nice.", voice: ARTHUR },

  // Survival card phrases (alternate)
  { text: "Hi, I am Roberto. I am from Sao Paulo, Brazil.", voice: ARTHUR },
  { text: "I am a businessman. I work with technology.", voice: ELLEN },
  { text: "I want to travel to Barcelona and Paris this August.", voice: ARTHUR },
  { text: "I need a good hotel near the city center.", voice: ELLEN },
  { text: "I like good restaurants and beautiful cities.", voice: ARTHUR },

  // Additional phrases
  { text: "Hi, I am Roberto. I am from São Paulo.", voice: ARTHUR },
  { text: "I need English for my trip this August.", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Roberto Pires — Aula 1...');
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
