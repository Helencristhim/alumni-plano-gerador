const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const RILEY_ID = 'hA4zGnmTwX2NQiTRMt7o'; // Female (Sandra)
const ASH_ID = 'VU16byTywsWv5JpI8rbc';   // Male (alternation + male chars)

const AUDIO_DIR = path.join(__dirname, 'public', 'audio', 'sandra-hayasaki');

// Extract audioMap from professor file
const html = fs.readFileSync(path.join(__dirname, 'public', 'professor', 'sandra-hayasaki.html'), 'utf8');
const match = html.match(/var audioMap = \{([\s\S]*?)\};/);
if (!match) { console.error('No audioMap found'); process.exit(1); }
const block = '{' + match[1] + '}';
const map = eval('(' + block + ')');
const entries = Object.entries(map);

// Voice assignment: Sandra's exercises = Riley, male character = Ash, alternate for general
// Dialogue lines by Mark (male teacher) = Ash
const ashPhrases = [
  'Good morning! Welcome to your English class.',
  'My name is Mark. What is your name?',
  'Nice to meet you, Sandra! Where are you from?',
  'What is your hobby, Sandra?',
  'Job', 'English', 'Goal',  // alternating vocab
  'I am fine, thank you.',
  'He is a good teacher.',
  'She is from Japan.',
  '[order-l1]'
];

function getVoice(text, index) {
  if (ashPhrases.some(p => text === p)) return ASH_ID;
  // For single words (vocab), alternate
  if (text.split(' ').length <= 2 && index % 2 === 1) return ASH_ID;
  return RILEY_ID;
}

async function generateAudio(text, filePath, voiceId) {
  const fullPath = path.join(AUDIO_DIR, path.basename(filePath));
  if (fs.existsSync(fullPath)) {
    console.log(`SKIP (exists): ${path.basename(filePath)}`);
    return true;
  }

  const url = `https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`;
  try {
    const res = await fetch(url, {
      method: 'POST',
      headers: {
        'xi-api-key': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg'
      },
      body: JSON.stringify({
        text: text.replace(/\[order-l1\]/, 'Good morning, everyone. Let me introduce myself. My name is Sandra. I am from Brazil. I study English every week. My goal is to speak English well.'),
        model_id: 'eleven_turbo_v2_5',
        voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0, use_speaker_boost: true }
      })
    });

    if (!res.ok) {
      const err = await res.text();
      console.error(`FAIL: ${path.basename(filePath)} - ${res.status} ${err.substring(0,100)}`);
      return false;
    }

    const buffer = Buffer.from(await res.arrayBuffer());
    fs.writeFileSync(fullPath, buffer);
    console.log(`OK: ${path.basename(filePath)} (${(buffer.length/1024).toFixed(1)}KB)`);
    return true;
  } catch(e) {
    console.error(`ERROR: ${path.basename(filePath)} - ${e.message}`);
    return false;
  }
}

async function main() {
  console.log(`Generating ${entries.length} audio files...`);
  console.log(`Output: ${AUDIO_DIR}`);

  let ok = 0, fail = 0;

  // Process in batches of 5 to respect rate limits
  for (let i = 0; i < entries.length; i += 5) {
    const batch = entries.slice(i, i + 5);
    const results = await Promise.all(
      batch.map(([text, filePath], batchIdx) => {
        const voiceId = getVoice(text, i + batchIdx);
        return generateAudio(text, filePath, voiceId);
      })
    );
    results.forEach(r => r ? ok++ : fail++);

    // Small delay between batches
    if (i + 5 < entries.length) await new Promise(r => setTimeout(r, 500));
  }

  console.log(`\nDone: ${ok} OK, ${fail} failed, ${entries.length} total`);
}

main();
