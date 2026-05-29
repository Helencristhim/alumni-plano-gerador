const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

const PHRASES = [
  // Vocab words (Arthur — single/short)
  { text: "This", voice: "arthur" },
  { text: "That", voice: "arthur" },
  { text: "Phone", voice: "arthur" },
  { text: "Bag", voice: "arthur" },
  { text: "Key", voice: "arthur" },
  { text: "Book", voice: "arthur" },
  { text: "Pen", voice: "arthur" },
  { text: "Color", voice: "arthur" },
  { text: "Big", voice: "arthur" },
  { text: "Small", voice: "arthur" },

  // Vocab example sentences (alternate)
  { text: "This is my phone.", voice: "ellen" },
  { text: "That is your bag.", voice: "arthur" },
  { text: "This is my key.", voice: "ellen" },
  { text: "That is a good book.", voice: "arthur" },
  { text: "I need a pen.", voice: "ellen" },
  { text: "What color is your phone?", voice: "arthur" },
  { text: "Sao Paulo is a big city.", voice: "ellen" },
  { text: "Jau is a small city.", voice: "arthur" },

  // Grammar + practice phrases
  { text: "This is a blue pen.", voice: "ellen" },
  { text: "That is a big city.", voice: "arthur" },
  { text: "What color is this?", voice: "ellen" },
  { text: "It is big.", voice: "arthur" },
  { text: "It is small.", voice: "ellen" },
  { text: "This is a small red book.", voice: "arthur" },
  { text: "That is a big bag.", voice: "ellen" },

  // Dialogue — David lines (Arthur)
  { text: "Good morning, Gabriela! How are you today?", voice: "arthur" },
  { text: "Do you remember your 5 sentences from Lesson 1?", voice: "arthur" },
  { text: "What is this?", voice: "arthur" },
  { text: "What is that?", voice: "arthur" },
  { text: "What color is your bag?", voice: "arthur" },
  { text: "Hi Gabriela! Look at your desk. What do you see?", voice: "arthur" },
  { text: "Good! And what is that over there?", voice: "arthur" },
  { text: "What else do you have on your desk?", voice: "arthur" },
  { text: "What color is the book?", voice: "arthur" },
  { text: "Excellent! And where is your key?", voice: "arthur" },

  // Dialogue — Gabriela lines (Ellen)
  { text: "This is my phone. It is black.", voice: "ellen" },
  { text: "That is my bag. It is big and brown.", voice: "ellen" },
  { text: "I have a pen and a book. This is a blue pen.", voice: "ellen" },
  { text: "The book is red. It is small.", voice: "ellen" },
  { text: "My key is here. This is my key.", voice: "ellen" },

  // Colors
  { text: "It is black.", voice: "arthur" },
  { text: "It is blue.", voice: "ellen" },
  { text: "It is red.", voice: "arthur" },
  { text: "It is green.", voice: "ellen" },
  { text: "It is white.", voice: "arthur" },
];

function toFilename(text) {
  return 'aula2_' + text
    .toLowerCase()
    .replace(/[^a-z0-9 ]/g, '')
    .replace(/ +/g, '_')
    .substring(0, 55);
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

  const seen = new Set();
  const uniquePhrases = PHRASES.filter(p => {
    const key = p.text.toLowerCase();
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });

  console.log(`Generating ${uniquePhrases.length} audio files for Lesson 2...`);

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
        await new Promise(r => setTimeout(r, 500));
      } catch (err) {
        console.error(`  FAIL: ${filename} — ${err.message}`);
      }
    }

    audioMapEntries[phrase.text] = `/audio/gabriela-paulucci/${filename}`;
  }

  const mapPath = path.join(OUTPUT_DIR, 'audioMap-aula2.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMapEntries, null, 2));

  console.log(`\nDone: ${generated} generated, ${skipped} skipped`);
  console.log(`audioMap saved to ${mapPath}`);
}

main().catch(err => { console.error(err); process.exit(1); });
