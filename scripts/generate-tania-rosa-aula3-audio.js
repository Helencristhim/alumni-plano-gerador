const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tania-rosa-aula3');

// Voice rules:
// Single words (1-2 words) = ALWAYS Arthur
// Phrases (3+ words) = ALTERNATE Arthur/Ellen
// Dialogue: Receptionist = Arthur, Tânia = Ellen
const PHRASES = [
  // ===== Vocab words (1-2 words → Arthur) =====
  { text: "Reservation", voice: ARTHUR },
  { text: "Room", voice: ARTHUR },
  { text: "Key", voice: ARTHUR },
  { text: "Checkout", voice: ARTHUR },
  { text: "Receptionist", voice: ARTHUR },
  { text: "Elevator", voice: ARTHUR },
  { text: "Breakfast", voice: ARTHUR },
  { text: "Floor", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "I have a reservation under the name Rosa.", voice: ARTHUR },
  { text: "Could I have a room with a view, please?", voice: ELLEN },
  { text: "Here is your room key. You are in room 405.", voice: ARTHUR },
  { text: "Checkout is at 11 AM.", voice: ELLEN },
  { text: "The receptionist was very helpful.", voice: ARTHUR },
  { text: "The elevator is on your right.", voice: ELLEN },
  { text: "Would you like breakfast included?", voice: ARTHUR },
  { text: "Your room is on the fourth floor.", voice: ELLEN },

  // ===== Grammar: would like sentences (alternate) =====
  { text: "I would like a room with a view, please.", voice: ARTHUR },
  { text: "I would not like a room near the elevator.", voice: ELLEN },
  { text: "Yes, I would.", voice: ARTHUR },
  { text: "No, thank you.", voice: ELLEN },

  // ===== Context / narrative sentences (alternate) =====
  { text: "Tânia arrives at the Grand Palace Hotel after a long flight. She goes to the reception desk.", voice: ELLEN },
  { text: "She tells the receptionist she has a reservation. He checks the system and finds her booking.", voice: ARTHUR },

  // ===== Dialogue — Receptionist = Arthur, Tânia = Ellen =====
  { text: "Good evening! Welcome to the Grand Palace Hotel. How can I help you?", voice: ARTHUR },
  { text: "Good evening! I have a reservation under the name Tânia Rosa.", voice: ELLEN },
  { text: "Let me check. Yes, Mrs. Rosa! A double room for three nights. Is that correct?", voice: ARTHUR },
  { text: "Yes, that is correct. I would like a room with a view, if possible.", voice: ELLEN },
  { text: "Of course! Room 405 on the fourth floor has a lovely city view. Would you like breakfast included?", voice: ARTHUR },
  { text: "Yes, I would. What time is breakfast served?", voice: ELLEN },
  { text: "Breakfast is from 7 to 10 AM in the restaurant on the first floor.", voice: ARTHUR },
  { text: "That sounds perfect. What time is checkout?", voice: ELLEN },
  { text: "Checkout is at 11 AM. Here is your room key. The elevator is on your right.", voice: ARTHUR },
  { text: "Thank you very much! Could you also recommend a good restaurant nearby?", voice: ELLEN },

  // ===== Speech / practice phrases (alternate) =====
  { text: "Yes, I would. Thank you.", voice: ARTHUR },
  { text: "What time is checkout, please?", voice: ELLEN },
  { text: "Excuse me, where is the elevator?", voice: ARTHUR },
  { text: "Could you recommend a good restaurant nearby?", voice: ELLEN },
  { text: "I would like a room on a high floor, please.", voice: ARTHUR },
  { text: "What time is breakfast served?", voice: ELLEN },
  { text: "Could you tell me the Wi-Fi password, please?", voice: ARTHUR },
  { text: "Thank you! What time is checkout?", voice: ELLEN },

  // ===== Spot the Error phrases (alternate) =====
  { text: "I want a room with view.", voice: ARTHUR },
  { text: "What time is the checkout?", voice: ELLEN },
  { text: "What time is checkout?", voice: ARTHUR },
  { text: "The receptionist give me the key.", voice: ELLEN },
  { text: "The receptionist gave me the key.", voice: ARTHUR },
  { text: "Would you likes breakfast?", voice: ELLEN },
  { text: "Would you like breakfast?", voice: ARTHUR },
  { text: "My room is in fourth floor.", voice: ELLEN },
  { text: "My room is on the fourth floor.", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Tânia Rosa — Aula 3...');
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
