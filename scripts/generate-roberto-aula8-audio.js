const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

const PHRASES = [
  // Vocab words (Arthur = student gender)
  { text: "Damaged", voice: ARTHUR },
  { text: "Replacement", voice: ARTHUR },
  { text: "Inconvenience", voice: ARTHUR },

  // Vocab example sentences (alternate)
  { text: "My luggage is missing.", voice: ARTHUR },
  { text: "The flight was delayed by three hours.", voice: ELLEN },
  { text: "I need to report a problem.", voice: ARTHUR },
  { text: "I want to file a claim.", voice: ELLEN },
  { text: "My suitcase is damaged.", voice: ARTHUR },
  { text: "Can I get a replacement?", voice: ELLEN },
  { text: "I am sorry for the inconvenience.", voice: ARTHUR },

  // Grammar examples (alternate)
  { text: "I will call the airline right now.", voice: ARTHUR },
  { text: "I am going to talk to the manager.", voice: ELLEN },
  { text: "You should file a report.", voice: ARTHUR },
  { text: "You should call the airline.", voice: ELLEN },
  { text: "You should ask for a replacement.", voice: ARTHUR },

  // Complaint chunks
  { text: "I am not satisfied with this room.", voice: ARTHUR },
  { text: "What can you do about this?", voice: ELLEN },
  { text: "This is very inconvenient.", voice: ARTHUR },
  { text: "I agree.", voice: ARTHUR },
  { text: "I disagree.", voice: ARTHUR },
  { text: "It depends on the airline policy.", voice: ELLEN },

  // Dialogue — Roberto (Arthur) + Agent female (Ellen)
  { text: "Excuse me, my luggage did not arrive. I need to file a claim.", voice: ARTHUR },
  { text: "It is a large blue suitcase with my name tag on it.", voice: ARTHUR },
  { text: "Flight AB4821 from Sao Paulo. It arrived two hours late.", voice: ARTHUR },
  { text: "Let me check. Your bag was delayed, not lost. It should arrive tonight.", voice: ELLEN },
  { text: "Can you deliver it to my hotel?", voice: ARTHUR },
  { text: "Yes, we will send it to your hotel. Here is a reference number.", voice: ELLEN },

  // Hotel dialogue — Roberto (Arthur) + Receptionist (Ellen)
  { text: "The air conditioning is not working. I am not satisfied with this room.", voice: ARTHUR },
  { text: "I am sorry for the inconvenience. We will fix it right away.", voice: ELLEN },
  { text: "I would rather have a different room.", voice: ARTHUR },
  { text: "Let me check. We have a room on the fifth floor with a city view.", voice: ELLEN },
  { text: "That sounds good. What time is breakfast?", voice: ARTHUR },
  { text: "Breakfast is from 7 to 10. Here is your new key.", voice: ELLEN },

  // Missed connection dialogue
  { text: "My flight was delayed and I missed my connection. What should I do?", voice: ARTHUR },
  { text: "You should go to the rebooking desk. I will call them now.", voice: ELLEN },
  { text: "When is the next flight to Paris?", voice: ARTHUR },
  { text: "The next flight leaves at 8 PM. You will arrive in Paris by 10 PM.", voice: ELLEN },
  { text: "Will the airline pay for a hotel if I need to wait?", voice: ARTHUR },
  { text: "It depends on the policy. You should ask at the desk.", voice: ELLEN },

  // Quick fire / oral drilling (alternate)
  { text: "My luggage is missing. What should I do?", voice: ARTHUR },
  { text: "The air conditioning is damaged. I need a replacement room.", voice: ELLEN },
  { text: "I missed my connection. When is the next flight?", voice: ARTHUR },
  { text: "I am not satisfied with the service.", voice: ELLEN },
  { text: "I will file a report right now.", voice: ARTHUR },
  { text: "You should ask for a refund.", voice: ELLEN },
  { text: "My suitcase arrived damaged.", voice: ARTHUR },

  // Listening 1 — baggage narrative (Ellen)
  { text: "Roberto arrives at Barcelona airport after a long flight from Sao Paulo. He goes to baggage claim and waits. All the bags come out, but his blue suitcase is not there. He goes to the airline desk. The agent tells him his bag was delayed, not lost. It should arrive tonight. Roberto asks them to deliver it to his hotel. The agent gives him a reference number. Roberto is calm. He knows what to say.", voice: ELLEN },

  // Listening 2 — hotel problem narrative (Arthur)
  { text: "Roberto is at his hotel in Barcelona. He goes to his room on the third floor. The room is hot. He checks the air conditioning. It is not working. He calls the front desk. The receptionist says she is sorry and offers to fix it. Roberto says he would rather have a different room. She checks and finds a room on the fifth floor with a city view. Roberto takes it. He asks about breakfast. She says breakfast is from 7 to 10. Roberto is satisfied with the new room.", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Roberto Pires — Aula 8...');
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
