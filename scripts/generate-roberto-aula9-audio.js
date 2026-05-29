const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

const PHRASES = [
  // Vocab words (Arthur = student gender)
  { text: "Crowded", voice: ARTHUR },
  { text: "Modern", voice: ARTHUR },
  { text: "Efficient", voice: ARTHUR },
  { text: "Elegant", voice: ARTHUR },
  { text: "Formal", voice: ARTHUR },
  { text: "Relaxed", voice: ARTHUR },

  // Comparative sentences (alternate)
  { text: "Paris is more expensive than Barcelona.", voice: ARTHUR },
  { text: "Barcelona is more relaxed than Paris.", voice: ELLEN },
  { text: "The metro in Paris is faster than the bus.", voice: ARTHUR },
  { text: "Paris is more elegant than Barcelona.", voice: ELLEN },
  { text: "The food in Barcelona is cheaper than in Paris.", voice: ARTHUR },
  { text: "The Eiffel Tower is the most visited monument in France.", voice: ELLEN },
  { text: "French waiters are more formal than Spanish waiters.", voice: ARTHUR },
  { text: "Barcelona is bigger than I expected.", voice: ELLEN },
  { text: "The Sagrada Familia is the most beautiful church in Spain.", voice: ARTHUR },

  // Expressions
  { text: "In my opinion, Barcelona has better food.", voice: ARTHUR },
  { text: "I would rather eat at a brasserie than a fast-food place.", voice: ELLEN },
  { text: "It is a piece of cake.", voice: ARTHUR },
  { text: "In my opinion...", voice: ARTHUR },
  { text: "I would rather...", voice: ARTHUR },

  // Short comparatives for slides
  { text: "Barcelona is cheaper.", voice: ARTHUR },
  { text: "Paris is more crowded.", voice: ELLEN },
  { text: "The metro is more efficient in Paris.", voice: ARTHUR },
  { text: "good, better, the best", voice: ELLEN },
  { text: "bad, worse, the worst", voice: ARTHUR },

  // Dialogue — Roberto (Arthur) + Sophie (Ellen)
  { text: "Where are you headed?", voice: ELLEN },
  { text: "I am going to Paris. I just spent a week in Barcelona.", voice: ARTHUR },
  { text: "Oh nice! How was Barcelona?", voice: ELLEN },
  { text: "It was amazing. The food is cheaper than in Paris, and the people are more relaxed.", voice: ARTHUR },
  { text: "I agree. Barcelona is more relaxed. But Paris is more elegant, in my opinion.", voice: ELLEN },
  { text: "What do you recommend in Paris?", voice: ARTHUR },
  { text: "You should visit Montmartre. It is the most charming neighborhood in Paris.", voice: ELLEN },
  { text: "I would rather explore on foot than take the metro everywhere.", voice: ARTHUR },
  { text: "That is the best way to see Paris. Walking is better than the metro for sightseeing.", voice: ELLEN },
  { text: "Thank you! Any restaurant recommendations?", voice: ARTHUR },
  { text: "Try a brasserie. The food is better than in tourist restaurants, and the prices are more reasonable.", voice: ELLEN },

  // Oral drilling / Quick fire
  { text: "In my opinion, Barcelona has the best food in Europe.", voice: ARTHUR },
  { text: "I would rather visit museums than go shopping.", voice: ELLEN },
  { text: "Paris is the most beautiful city I have ever seen.", voice: ARTHUR },
  { text: "The train is faster than the bus.", voice: ELLEN },
  { text: "This restaurant is better than the one near the hotel.", voice: ARTHUR },
  { text: "Navigating Paris will be a piece of cake after Barcelona.", voice: ELLEN },

  // Survival card
  { text: "Paris is more expensive than Barcelona, but the culture is richer.", voice: ARTHUR },
  { text: "The worst thing about travel is lost luggage.", voice: ELLEN },

  // Listening 1 — train conversation (Ellen narration)
  { text: "Roberto is on the train from Barcelona to Paris. He sits next to a French woman named Sophie. They start talking about the two cities. Roberto says Barcelona was amazing. The food was cheaper and the people were more relaxed. Sophie agrees but says Paris is more elegant. She recommends Montmartre as the most charming neighborhood. Roberto asks about restaurants. Sophie says brasseries have better food than tourist restaurants. Roberto is excited about Paris. He feels confident talking about both cities in English.", voice: ELLEN },

  // Listening 2 — Paris arrival (Arthur narration)
  { text: "Roberto arrives in Paris by train. He takes the metro to his hotel near the Eiffel Tower. The metro is faster and more efficient than in Barcelona. He checks into his hotel. The receptionist is more formal than in Barcelona. Roberto asks about restaurants nearby. The receptionist recommends a brasserie in the 7th arrondissement. She says it has the best steak in the neighborhood. Roberto thanks her and walks to the restaurant. Paris is more crowded than Barcelona, but Roberto feels ready. He orders in English without any problems.", voice: ARTHUR },
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
  console.log('Generating ' + unique.length + ' audio files for Roberto Pires — Aula 9...');
  let generated = 0, skipped = 0;
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
    }
  }
  console.log('\nDone! Generated ' + generated + ' new, skipped ' + skipped + ' existing.');
}

main().catch(e => { console.error(e); process.exit(1); });
