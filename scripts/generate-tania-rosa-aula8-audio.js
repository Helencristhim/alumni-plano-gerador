const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tania-rosa-aula8');

// Voice rules:
// Single words (1-2 words) = ALWAYS Arthur
// Phrases (3+ words) = ALTERNATE Arthur/Ellen
// Dialogue: Pharmacist = Arthur, Tânia = Ellen
const PHRASES = [
  // ===== Vocab words (1-2 words -> Arthur) =====
  { text: "Emergency", voice: ARTHUR },
  { text: "Pharmacy", voice: ARTHUR },
  { text: "Medicine", voice: ARTHUR },
  { text: "Doctor", voice: ARTHUR },
  { text: "Pain", voice: ARTHUR },
  { text: "Symptom", voice: ARTHUR },
  { text: "Ambulance", voice: ARTHUR },
  { text: "Insurance", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "In an emergency, call 112 in Europe.", voice: ARTHUR },
  { text: "I need to find a pharmacy nearby.", voice: ELLEN },
  { text: "I need to buy some medicine for my headache.", voice: ARTHUR },
  { text: "I need to see a doctor, please.", voice: ELLEN },
  { text: "I have a pain in my stomach.", voice: ARTHUR },
  { text: "My symptoms are a headache and a sore throat.", voice: ELLEN },
  { text: "Could you call an ambulance, please?", voice: ARTHUR },
  { text: "I have travel insurance. Here is my card.", voice: ELLEN },

  // ===== Grammar: need to / have to examples (alternate) =====
  { text: "I need to see a doctor.", voice: ARTHUR },
  { text: "You have to take this medicine twice a day.", voice: ELLEN },
  { text: "She needs to rest for two days.", voice: ARTHUR },
  { text: "Do I have to go to the hospital?", voice: ELLEN },

  // ===== Dialogue — Pharmacist = Arthur, Tânia = Ellen =====
  { text: "Good morning. I need some help, please. I am not feeling well.", voice: ELLEN },
  { text: "Good morning! What are your symptoms?", voice: ARTHUR },
  { text: "I have a headache and a sore throat. I also feel very tired.", voice: ELLEN },
  { text: "How long have you had these symptoms?", voice: ARTHUR },
  { text: "Since yesterday morning. I think I need some medicine.", voice: ELLEN },
  { text: "I recommend this pain reliever for the headache. You need to take it twice a day.", voice: ARTHUR },
  { text: "Do I have to take it with food?", voice: ELLEN },
  { text: "Yes, you have to take it after meals. And for the sore throat, try these lozenges.", voice: ARTHUR },
  { text: "Thank you. Do I need to see a doctor?", voice: ELLEN },
  { text: "If you do not feel better in two days, you need to see a doctor. Here is the address of a clinic nearby.", voice: ARTHUR },

  // ===== Quiz / practice phrases (alternate) =====
  { text: "Excuse me, I need to find a pharmacy. Is there one nearby?", voice: ARTHUR },
  { text: "I have a headache and a sore throat.", voice: ELLEN },
  { text: "Do I need a prescription for this medicine?", voice: ARTHUR },
  { text: "How do I have to take this medicine?", voice: ELLEN },
  { text: "Could you call an ambulance, please? It is an emergency.", voice: ARTHUR },
  { text: "I have travel insurance. Here is my insurance card.", voice: ELLEN },

  // ===== Error correction pairs (alternate) =====
  { text: "I need see a doctor.", voice: ARTHUR },
  { text: "You have take medicine twice.", voice: ELLEN },
  { text: "You have to take medicine twice a day.", voice: ARTHUR },
  { text: "I have a pain in the head.", voice: ELLEN },
  { text: "I have a headache.", voice: ARTHUR },
  { text: "Do I have to going to the hospital?", voice: ELLEN },
  { text: "She need to rest.", voice: ARTHUR },
  { text: "She needs to rest.", voice: ELLEN },

  // ===== Survival / speech phrases (alternate) =====
  { text: "I am not feeling well. I need to see a doctor.", voice: ARTHUR },
  { text: "I have a headache, a sore throat, and I feel very tired.", voice: ELLEN },
  { text: "I need some medicine for my headache, please.", voice: ARTHUR },
  { text: "Do I need to see a doctor?", voice: ELLEN },
  { text: "How often do I have to take this medicine?", voice: ARTHUR },
  { text: "Help! Could you call an ambulance, please?", voice: ELLEN },
  { text: "I need some medicine, please.", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Tânia Rosa — Aula 8...');
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
