const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q'; // Male, neutral American
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';  // Female, calm American

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'elaine-mieko-pinho');

// Rule: 1-2 words = Arthur, 3+ words = alternate Arthur/Ellen
// Dialogues: Sarah = Ellen, announcements = Ellen, Elaine lines = Arthur

const PHRASES = [
  // Vocab words (Arthur — single/short)
  { text: "Passport", voice: "arthur" },
  { text: "Luggage", voice: "arthur" },
  { text: "Flight", voice: "arthur" },
  { text: "Check-in", voice: "arthur" },
  { text: "Reservation", voice: "arthur" },
  { text: "Destination", voice: "arthur" },
  { text: "Housekeeper", voice: "arthur" },
  { text: "Emergency", voice: "arthur" },

  // Vocab example sentences (alternate Arthur/Ellen)
  { text: "Don't forget your passport!", voice: "ellen" },
  { text: "My luggage is very heavy.", voice: "arthur" },
  { text: "The flight is at 9 AM.", voice: "ellen" },
  { text: "Where is the check-in counter?", voice: "arthur" },
  { text: "I have a reservation for tonight.", voice: "ellen" },
  { text: "My destination is New York.", voice: "arthur" },
  { text: "The housekeeper left extra towels.", voice: "ellen" },
  { text: "In case of emergency, call 911.", voice: "arthur" },

  // Pronunciation stress patterns
  { text: "Passport. PAS-sport.", voice: "arthur" },
  { text: "Luggage. LUG-gage.", voice: "ellen" },
  { text: "Reservation. Re-ser-VA-tion.", voice: "arthur" },
  { text: "Destination. Des-ti-NA-tion.", voice: "ellen" },
  { text: "Emergency. E-MER-gen-cy.", voice: "arthur" },

  // Dialogue — Sarah lines (Ellen)
  { text: "Hi there! Are you waiting for a flight too?", voice: "ellen" },
  { text: "Nice to meet you! What is your destination?", voice: "ellen" },
  { text: "Is your luggage heavy?", voice: "ellen" },
  { text: "Do you have your passport ready?", voice: "ellen" },

  // Dialogue — Elaine lines (Arthur)
  { text: "Yes! My name is Elaine. I am from Brazil.", voice: "arthur" },
  { text: "My destination is New York. I have a reservation at a hotel.", voice: "arthur" },
  { text: "Yes! My luggage is very heavy!", voice: "arthur" },
  { text: "Yes, my passport is in my bag!", voice: "arthur" },

  // Airport announcement (Ellen — formal)
  { text: "Attention passengers. Flight AA 2024 to New York JFK is now boarding at Gate B12. Please have your boarding pass and passport ready.", voice: "ellen" },

  // Survival card phrases (alternate)
  { text: "My name is Elaine Pinho.", voice: "arthur" },
  { text: "I am from Sao Paulo, Brazil.", voice: "ellen" },
  { text: "I am 61 years old.", voice: "arthur" },
  { text: "I have a reservation at the hotel.", voice: "ellen" },
  { text: "Excuse me, where is the check-in?", voice: "arthur" },

  // Grammar examples
  { text: "I am Elaine.", voice: "arthur" },
  { text: "She is from Brazil.", voice: "ellen" },
  { text: "We are travelers.", voice: "arthur" },
  { text: "You are my teacher.", voice: "ellen" },
  { text: "I am 61 years old.", voice: "arthur" },

  // Quick challenge answers
  { text: "Excuse me, where is the check-in?", voice: "ellen" },
  { text: "My luggage is very heavy.", voice: "arthur" },

  // Hotel check-in dialogue
  { text: "Good evening. Welcome to The Manhattan Grand. May I have your name?", voice: "ellen" },
  { text: "Good evening. My name is Elaine Pinho. I have a reservation.", voice: "arthur" },
  { text: "Of course. Could you spell your last name, please?", voice: "ellen" },
  { text: "Yes. P-I-N-H-O. Pinho.", voice: "arthur" },
  { text: "Thank you, Ms. Pinho. You are in room 1204, on the twelfth floor.", voice: "ellen" },
  { text: "Thank you. What time is breakfast?", voice: "arthur" },
  { text: "Breakfast is from 7 to 10 AM in the restaurant on the second floor.", voice: "ellen" },
  { text: "Perfect. Thank you very much.", voice: "arthur" },
];

function toFilename(text) {
  return text
    .toLowerCase()
    .replace(/[^a-z0-9 ]/g, '')
    .replace(/ +/g, '_')
    .substring(0, 60);
}

async function generateAudio(phrase, voiceId, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: {
      'xi-api-key': API_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: phrase,
      model_id: 'eleven_turbo_v2_5',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 },
    }),
  });

  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`ElevenLabs error (${resp.status}): ${err}`);
  }

  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  if (!API_KEY) {
    console.error('ELEVENLABS_API_KEY not set');
    process.exit(1);
  }

  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  const audioMap = {};
  let generated = 0;
  let skipped = 0;

  // Deduplicate
  const seen = new Set();
  const uniquePhrases = PHRASES.filter(p => {
    const key = p.text.toLowerCase();
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });

  console.log(`Generating ${uniquePhrases.length} audio files...`);

  for (const phrase of uniquePhrases) {
    const filename = toFilename(phrase.text) + '.mp3';
    const outputPath = path.join(OUTPUT_DIR, filename);
    const voiceId = phrase.voice === 'ellen' ? ELLEN_ID : ARTHUR_ID;

    if (fs.existsSync(outputPath)) {
      console.log(`  SKIP (exists): ${filename}`);
      skipped++;
    } else {
      try {
        const bytes = await generateAudio(phrase.text, voiceId, outputPath);
        console.log(`  OK [${phrase.voice}]: ${filename} (${(bytes/1024).toFixed(1)}KB)`);
        generated++;
        // Rate limit: 2 per second
        await new Promise(r => setTimeout(r, 500));
      } catch (err) {
        console.error(`  FAIL: ${filename} — ${err.message}`);
      }
    }

    audioMap[phrase.text] = `/audio/elaine-mieko-pinho/${filename}`;
  }

  // Write audioMap JSON for reference
  const mapPath = path.join(OUTPUT_DIR, 'audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMap, null, 2));

  console.log(`\nDone: ${generated} generated, ${skipped} skipped`);
  console.log(`audioMap saved to ${mapPath}`);

  // Output JS-ready audioMap
  console.log('\n// Paste into HTML:');
  console.log('var audioMap = ' + JSON.stringify(audioMap, null, 2) + ';');
}

main().catch(err => { console.error(err); process.exit(1); });
