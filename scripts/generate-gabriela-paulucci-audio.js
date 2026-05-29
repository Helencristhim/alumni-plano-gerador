const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

// Rule: 1-2 words = Arthur, 3+ words = alternate Arthur/Ellen
// Dialogue: David = Arthur, Gabriela = Ellen

const PHRASES = [
  // Vocab words (Arthur — single/short)
  { text: "Name", voice: "arthur" },
  { text: "Age", voice: "arthur" },
  { text: "City", voice: "arthur" },
  { text: "Work", voice: "arthur" },
  { text: "Country", voice: "arthur" },
  { text: "Live", voice: "arthur" },
  { text: "From", voice: "arthur" },
  { text: "Years Old", voice: "arthur" },

  // Vocab example sentences (alternate Arthur/Ellen)
  { text: "My name is Gabriela.", voice: "ellen" },
  { text: "I am 33 years old.", voice: "arthur" },
  { text: "I am from Jau.", voice: "ellen" },
  { text: "I live in Sao Paulo.", voice: "arthur" },
  { text: "I work at Itau.", voice: "ellen" },

  // Questions (alternate)
  { text: "What is your name?", voice: "arthur" },
  { text: "My name is Gabriela Paulucci.", voice: "ellen" },
  { text: "Where are you from?", voice: "arthur" },
  { text: "I am from Brazil. I am from a small city called Jau.", voice: "ellen" },
  { text: "Where do you live?", voice: "arthur" },
  { text: "I live in Sao Paulo. It is a big city.", voice: "ellen" },
  { text: "How old are you?", voice: "arthur" },
  { text: "I am 33 years old", voice: "ellen" },
  { text: "Where do you work?", voice: "arthur" },
  { text: "I work at Itau in Sao Paulo.", voice: "ellen" },

  // Greetings
  { text: "Nice to meet you.", voice: "arthur" },
  { text: "Nice to meet you too.", voice: "ellen" },

  // Grammar examples
  { text: "I am Gabriela.", voice: "ellen" },
  { text: "She is from Brazil.", voice: "arthur" },
  { text: "He is a teacher.", voice: "ellen" },
  { text: "We are students.", voice: "arthur" },
  { text: "They are from Sao Paulo.", voice: "ellen" },
  { text: "You are my teacher.", voice: "arthur" },
  { text: "It is a big city.", voice: "ellen" },

  // Extended sentences
  { text: "I am from Jau, but I live in Sao Paulo.", voice: "arthur" },
  { text: "Hi, my name is Gabriela. I am 33 years old.", voice: "ellen" },
  { text: "I am from Jau, a small city in Sao Paulo state.", voice: "arthur" },
  { text: "I live in Sao Paulo now. It is a very big city.", voice: "ellen" },
  { text: "I work at Itau. It is a big bank in Brazil.", voice: "arthur" },
  { text: "I want to learn English for travel.", voice: "ellen" },

  // Dialogue — David lines (Arthur)
  { text: "Hello! My name is David. I am your new English teacher.", voice: "arthur" },
  { text: "Nice to meet you too, Gabriela! Where are you from?", voice: "arthur" },
  { text: "Sao Paulo is a very big city! Where do you work?", voice: "arthur" },
  { text: "Great! How old are you, Gabriela?", voice: "arthur" },
  { text: "Wonderful! Welcome to our English class!", voice: "arthur" },

  // Dialogue — Gabriela lines (Ellen)
  { text: "Hi David! My name is Gabriela. Nice to meet you.", voice: "ellen" },
  { text: "I am from Jau. It is a small city. But I live in Sao Paulo now.", voice: "ellen" },
  { text: "I work at Itau. It is a big bank.", voice: "ellen" },
  { text: "Thank you, David!", voice: "ellen" },

  // Listening — Airport announcement (Ellen — formal)
  { text: "Attention please. This is an announcement for all passengers. Flight 2024 to New York is now boarding at Gate 5. Please have your passport ready.", voice: "ellen" },

  // Extra phrases
  { text: "Here is my passport.", voice: "arthur" },
  { text: "Excuse me, where is Gate 5?", voice: "ellen" },
  { text: "I am a passenger on Flight 2024.", voice: "arthur" },
  { text: "My destination is New York.", voice: "ellen" },
  { text: "I am Brazilian.", voice: "arthur" },
  { text: "Sao Paulo is in Brazil.", voice: "ellen" },
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

  const audioMapEntries = {};
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

    audioMapEntries[phrase.text] = `/audio/gabriela-paulucci/${filename}`;
  }

  // Write audioMap JSON for reference
  const mapPath = path.join(OUTPUT_DIR, 'audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMapEntries, null, 2));

  console.log(`\nDone: ${generated} generated, ${skipped} skipped`);
  console.log(`audioMap saved to ${mapPath}`);

  // Output JS-ready audioMap
  console.log('\n// Paste into HTML:');
  console.log('var audioMap = ' + JSON.stringify(audioMapEntries, null, 2) + ';');
}

main().catch(err => { console.error(err); process.exit(1); });
