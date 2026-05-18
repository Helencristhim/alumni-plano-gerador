const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'tania-rosa');

// Tânia = female → Ellen for her lines
// David = male → Arthur for his lines
// Single words (1-2 words) → ALWAYS Arthur
// Phrases (3+ words) → ALTERNATE Arthur/Ellen
// Dialogue lines: data-voice from HTML
const PHRASES = [
  // ===== Vocab words (1-2 words → Arthur) =====
  { text: "Travel", voice: ARTHUR },
  { text: "Destination", voice: ARTHUR },
  { text: "Passport", voice: ARTHUR },
  { text: "Experience", voice: ARTHUR },
  { text: "Culture", voice: ARTHUR },
  { text: "Visit", voice: ARTHUR },
  { text: "Country", voice: ARTHUR },
  { text: "Language", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "I love to travel to new places.", voice: ARTHUR },
  { text: "My next destination is Portugal.", voice: ELLEN },
  { text: "Could I see your passport, please?", voice: ARTHUR },
  { text: "Living abroad is a great experience.", voice: ELLEN },
  { text: "I enjoy learning about different cultures.", voice: ARTHUR },
  { text: "I want to visit Japan next year.", voice: ELLEN },
  { text: "Brazil is a beautiful country.", voice: ARTHUR },
  { text: "English is an international language.", voice: ELLEN },

  // ===== Grammar in Context sentences (alternate) =====
  { text: "Tânia lives in Brazil.", voice: ELLEN },
  { text: "She travels to many countries.", voice: ARTHUR },
  { text: "Her family does not speak English at home.", voice: ELLEN },
  { text: "Does she enjoy visiting new places?", voice: ARTHUR },
  { text: "Yes, she does. She loves learning about cultures.", voice: ELLEN },

  // ===== Grammar Practice / Fill-in-the-blank (alternate) =====
  { text: "I usually travel with my family.", voice: ARTHUR },
  { text: "She does not speak French very well.", voice: ELLEN },
  { text: "Do you visit other countries often?", voice: ARTHUR },
  { text: "He enjoys learning new languages.", voice: ELLEN },
  { text: "We love experiencing different cultures.", voice: ARTHUR },
  { text: "Tânia Rosa travels to new destinations every year.", voice: ELLEN },

  // ===== Speech cards — Tânia = Ellen (female student) =====
  { text: "Hi, I am Tânia Rosa. Nice to meet you.", voice: ELLEN },
  { text: "I love to travel. I have been to many countries.", voice: ELLEN },
  { text: "My family and I visit new places together.", voice: ELLEN },
  { text: "I want to speak English with confidence.", voice: ELLEN },

  // ===== Additional speech phrases =====
  { text: "Hi, I am Tânia Rosa. I am from Brazil.", voice: ELLEN },
  { text: "I love traveling. I have been to many countries.", voice: ELLEN },
  { text: "Could you repeat that, please?", voice: ELLEN },
  { text: "I enjoy visiting new countries and cultures.", voice: ELLEN },
  { text: "I usually travel with my children and grandchildren.", voice: ELLEN },

  // ===== Dialogue — David (male) = Arthur, Tânia (female) = Ellen =====
  { text: "Hello! Are you traveling to Europe too?", voice: ARTHUR },
  { text: "Yes, I am! I am going to visit a few countries.", voice: ELLEN },
  { text: "That sounds exciting! Where are you from?", voice: ARTHUR },
  { text: "I am from Brazil. I love traveling to new destinations.", voice: ELLEN },
  { text: "Brazil! Do you travel often?", voice: ARTHUR },
  { text: "Yes, I do. I usually travel with my children and grandchildren.", voice: ELLEN },
  { text: "That is wonderful! What countries have you visited?", voice: ARTHUR },
  { text: "I have been to Portugal, Spain, and France. I love different cultures.", voice: ELLEN },
  { text: "Do you speak any other languages?", voice: ARTHUR },
  { text: "A little. I want to improve my English. It is important for traveling.", voice: ELLEN },

  // ===== Quick fire questions (alternate) =====
  { text: "My name is Tânia Rosa. Nice to meet you.", voice: ELLEN },
  { text: "I am from Brazil.", voice: ELLEN },
  { text: "Yes, I do. I love to travel.", voice: ELLEN },
  { text: "I enjoy visiting new countries and learning about cultures.", voice: ELLEN },
  { text: "No, I do not. I usually travel with my family.", voice: ELLEN },
  { text: "I want to communicate with people from different countries.", voice: ELLEN },

  // ===== Additional grammar/practice sentences =====
  { text: "She travels every year.", voice: ARTHUR },
  { text: "Does she like traveling?", voice: ELLEN },
  { text: "I do not speak English.", voice: ARTHUR },
  { text: "Does he visit other countries?", voice: ELLEN },
  { text: "I live in Brazil.", voice: ARTHUR },
  { text: "I play piano and I do crochet.", voice: ELLEN },
  { text: "Yes, I do. I love trying new food.", voice: ARTHUR },
  { text: "What do you do?", voice: ELLEN },

  // ===== Survival card phrases (mix both) =====
  { text: "I have been to many countries. I love visiting new places.", voice: ARTHUR },
  { text: "Do you travel with your family?", voice: ELLEN },
  { text: "I enjoy visiting new destinations and learning about cultures.", voice: ARTHUR },
  { text: "Could you repeat that, please? I am learning English.", voice: ELLEN },
  { text: "She does not stay home on vacation.", voice: ARTHUR },
  { text: "Does she enjoy different cultures?", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Tânia Rosa — Aula 1...');
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
