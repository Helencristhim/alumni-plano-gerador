const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'pricila-adamo');

// Voice rules:
// Single words (1-2 words) = ALWAYS Arthur
// Phrases (3+ words) = ALTERNATE Arthur/Ellen
// Dialogue: David = Arthur, Pricila = Ellen
const PHRASES = [
  // ===== Onboarding survival phrases (alternate) =====
  { text: "Could you repeat that, please?", voice: ARTHUR },
  { text: "I am not sure I understand. Could you explain?", voice: ELLEN },
  { text: "Let me think about that for a moment.", voice: ARTHUR },
  { text: "To be honest, I have always wanted to...", voice: ELLEN },
  { text: "I have been studying English for many years.", voice: ARTHUR },

  // ===== Vocab words (1-2 words -> Arthur) =====
  { text: "Experience", voice: ARTHUR },
  { text: "Journey", voice: ARTHUR },
  { text: "Fluent", voice: ARTHUR },
  { text: "Confident", voice: ARTHUR },
  { text: "Struggle", voice: ARTHUR },
  { text: "Routine", voice: ARTHUR },
  { text: "Abroad", voice: ARTHUR },
  { text: "Retire", voice: ARTHUR },
  { text: "Accomplish", voice: ARTHUR },
  { text: "Explore", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "I have had many experiences traveling abroad.", voice: ARTHUR },
  { text: "Learning English has been a long journey for me.", voice: ELLEN },
  { text: "I want to become fluent in English before my next trip.", voice: ARTHUR },
  { text: "I feel more confident when I practice every day.", voice: ELLEN },
  { text: "I sometimes struggle to find the right words in English.", voice: ARTHUR },
  { text: "I try to make English part of my daily routine.", voice: ELLEN },
  { text: "I have traveled abroad many times.", voice: ARTHUR },
  { text: "I am going to retire soon and travel the world.", voice: ELLEN },
  { text: "I want to accomplish my dream of speaking English fluently.", voice: ARTHUR },
  { text: "I love to explore new places and meet new people.", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "I have been studying English for...", voice: ARTHUR },
  { text: "I grew up in...", voice: ELLEN },
  { text: "I have always wanted to...", voice: ARTHUR },
  { text: "Right now, I am...", voice: ELLEN },
  { text: "To be honest, the thing is...", voice: ARTHUR },

  // ===== Grammar context sentences (alternate) =====
  { text: "Pricila is a dentist from Araras, Sao Paulo.", voice: ELLEN },
  { text: "She has worked as a dentist for over twenty-five years.", voice: ARTHUR },
  { text: "She has traveled to Canada, Malta, and many other countries.", voice: ELLEN },
  { text: "She lives in Araras and goes to Sao Paulo every two weeks.", voice: ARTHUR },
  { text: "She has always wanted to be fluent in English.", voice: ELLEN },

  // ===== Fill-in / practice phrases =====
  { text: "I have been studying English for over twenty years.", voice: ARTHUR },
  { text: "I grew up in Araras, a small city in Sao Paulo state.", voice: ELLEN },
  { text: "I have always wanted to visit Australia.", voice: ARTHUR },
  { text: "Right now, I am preparing for my retirement.", voice: ELLEN },
  { text: "To be honest, the thing is I get tired of studying.", voice: ARTHUR },

  // ===== Dialogue — David = Arthur, Pricila = Ellen =====
  { text: "Hi there! Are you flying to Sydney too?", voice: ARTHUR },
  { text: "Yes! This is going to be an amazing journey.", voice: ELLEN },
  { text: "What brings you to Australia?", voice: ARTHUR },
  { text: "I have always wanted to explore the country. I am a retired dentist from Brazil.", voice: ELLEN },
  { text: "That sounds wonderful! Have you been to Australia before?", voice: ARTHUR },
  { text: "No, this is my first time. I have traveled to many countries, but never to Australia.", voice: ELLEN },
  { text: "What do you want to accomplish on this trip?", voice: ARTHUR },
  { text: "I want to become more confident speaking English abroad. I have been studying for years.", voice: ELLEN },

  // ===== Self-introduction ordering phrases =====
  { text: "Let me introduce myself. I am Pricila Adamo.", voice: ELLEN },
  { text: "I am a dentist, but I am retiring soon.", voice: ARTHUR },
  { text: "I have been studying English since the year 2000.", voice: ELLEN },
  { text: "I have always been curious about the world.", voice: ARTHUR },
  { text: "I want to explore Australia next year.", voice: ELLEN },

  // ===== Pronunciation / speech phrases =====
  { text: "I want to accomplish my dream of speaking English fluently.", voice: ARTHUR },

  // ===== Listening 1: Pricila's story (Ellen, full paragraph) =====
  { text: "Hi, my name is Pricila Adamo. I am a dentist from Araras, a small city in Sao Paulo state, Brazil. I have been working as a dentist for over twenty-five years. I have treated patients from many countries, including foreigners who came to my clinic. I have traveled to Canada, where I had an amazing experience at a hospital. I also did an exchange program in Malta. I have been studying English since the year 2000, but to be honest, the thing is I sometimes struggle to organize my thoughts in English. Right now, I am preparing for my retirement. I want to explore Australia and feel confident speaking English abroad. My journey with English has been long, but I have never given up.", voice: ELLEN },

  // ===== Listening 2: David about Australia (Arthur, full paragraph) =====
  { text: "G'day! My name is David, and I am from Sydney, Australia. Sydney is a beautiful city with the famous Opera House and Harbour Bridge. If you love nature, you should visit the Great Barrier Reef. It is one of the most incredible places on Earth. Melbourne is another great city. It has amazing coffee, street art, and cultural events. If you are adventurous, you can explore the Outback. It is a vast, open landscape with unique wildlife. Australians are very friendly and relaxed. We love to have a barbecue and spend time at the beach. I think you will have an amazing journey in Australia.", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Pricila Adamo — Aula 1...');
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
