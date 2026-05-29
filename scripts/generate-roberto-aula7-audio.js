const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-pires');

// Roberto = male = Arthur
// Local woman Maria = Ellen
// Male passenger = Arthur
// Single words (1-2) = ALWAYS Arthur (student gender)
// General phrases = ALTERNATE Arthur/Ellen
const PHRASES = [
  // Vocab words (Arthur = student gender)
  { text: "Intersection", voice: ARTHUR },
  { text: "Block", voice: ARTHUR },
  { text: "Corner", voice: ARTHUR },
  { text: "Straight", voice: ARTHUR },
  { text: "Turn", voice: ARTHUR },
  { text: "Platform", voice: ARTHUR },
  { text: "Exit", voice: ARTHUR },

  // Vocab example sentences (alternate)
  { text: "Turn left at the intersection.", voice: ARTHUR },
  { text: "Walk two blocks to the station.", voice: ELLEN },
  { text: "The station is on the corner.", voice: ARTHUR },
  { text: "Go straight for three minutes.", voice: ELLEN },
  { text: "Turn right after the park.", voice: ARTHUR },
  { text: "The platform is downstairs.", voice: ELLEN },
  { text: "Where is the exit?", voice: ARTHUR },

  // Grammar examples (alternate)
  { text: "Go straight for two blocks.", voice: ELLEN },
  { text: "Turn left at the big intersection.", voice: ARTHUR },
  { text: "Take line 3 to Sagrada Familia.", voice: ELLEN },
  { text: "The metro runs every five minutes.", voice: ARTHUR },
  { text: "I am going to take the metro to the beach.", voice: ELLEN },
  { text: "Go straight.", voice: ARTHUR },
  { text: "Turn left.", voice: ELLEN },
  { text: "Take the metro.", voice: ARTHUR },

  // Common mistake phrases
  { text: "How do I get to the station?", voice: ARTHUR },
  { text: "Turn left at the corner.", voice: ELLEN },
  { text: "Where do I get off?", voice: ARTHUR },

  // Dialogue — Roberto (Arthur) + Maria/local woman (Ellen)
  { text: "Excuse me, could you tell me how to get to the Gothic Quarter?", voice: ARTHUR },
  { text: "Of course! Go straight for two blocks.", voice: ELLEN },
  { text: "Two blocks straight. And then?", voice: ARTHUR },
  { text: "Then turn left at the big intersection. You will see a church on the corner.", voice: ELLEN },
  { text: "Turn left at the intersection. Is it far from here?", voice: ARTHUR },
  { text: "No, about ten minutes on foot.", voice: ELLEN },
  { text: "And where is the nearest metro station?", voice: ARTHUR },
  { text: "Jaume I station is right on the corner. Take the exit on your left.", voice: ELLEN },

  // Wrong train dialogue — Roberto (Arthur) + Passenger male (Ellen for variety, but actually use Arthur for male)
  { text: "Excuse me, I think I am on the wrong train. I want to go to Barceloneta. Is this the right line?", voice: ARTHUR },
  { text: "No, this train goes to Trinitat Nova. You need to get off at the next stop and change to line 4.", voice: ELLEN },
  { text: "Which platform do I need?", voice: ARTHUR },
  { text: "When you get off, follow the signs for line 4. The platform is on the other side.", voice: ELLEN },
  { text: "Thank you! How many stops to Barceloneta?", voice: ARTHUR },
  { text: "Just three stops. You will see the beach from the exit.", voice: ELLEN },

  // Quick fire answers (alternate)
  { text: "Excuse me, could you tell me how to get to La Rambla?", voice: ARTHUR },
  { text: "Which line do I take to the beach?", voice: ELLEN },
  { text: "Where do I get off for the Sagrada Familia?", voice: ARTHUR },
  { text: "Is it far from here?", voice: ELLEN },
  { text: "How long does it take on foot?", voice: ARTHUR },
  { text: "Go straight, then turn right at the corner.", voice: ELLEN },

  // Survival card phrases (Arthur = student voice)
  { text: "Excuse me, could you tell me how to get to...?", voice: ARTHUR },
  { text: "How do I get to the metro station?", voice: ARTHUR },
  { text: "Which line do I take?", voice: ARTHUR },
  { text: "How long does it take?", voice: ARTHUR },

  // Oral drilling (alternate)
  { text: "Excuse me, could you tell me how to get to La Boqueria?", voice: ARTHUR },
  { text: "How do I get to the Sagrada Familia?", voice: ELLEN },
  { text: "Which line do I take to Barceloneta?", voice: ARTHUR },
  { text: "Where do I get off for the Gothic Quarter?", voice: ELLEN },

  // Additional phrases used in slides
  { text: "It is about a fifteen-minute walk.", voice: ELLEN },
  { text: "Take line 4 and get off at Barceloneta.", voice: ARTHUR },
  { text: "Go straight for two blocks and turn left at the intersection.", voice: ELLEN },
  { text: "The platform for line 3 is downstairs.", voice: ARTHUR },

  // Listening 1 — full narration (Ellen for narration)
  { text: "Roberto is now at his hotel in Eixample, Barcelona. He wants to visit the Gothic Quarter today. He leaves the hotel and walks to the nearest metro station. He asks a woman on the street for directions. She tells him to go straight for two blocks and turn left at the big intersection. Roberto thanks her and walks. At the metro, he asks which line goes to the Gothic Quarter. A man tells him to take line 4 to Jaume I. Roberto finds the platform, waits for the train, and gets on. He gets off at the right station and walks to the exit. He is now in the Gothic Quarter. He did it all in English.", voice: ELLEN },

  // Listening 2 — wrong train narration (Arthur for narration)
  { text: "Roberto gets on the metro at Passeig de Gracia. He wants to go to Barceloneta beach. After two stops, he realizes the station names look wrong. He asks a passenger next to him. The passenger says this train goes to Trinitat Nova, not Barceloneta. Roberto needs to get off at the next stop and change to line 4. He thanks the passenger and follows the signs.", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Roberto Pires — Aula 7...');
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

  console.log('\nDone! Generated ' + generated + ' new files, skipped ' + skipped + ' existing.');
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
