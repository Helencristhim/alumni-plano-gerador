const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

// Luiz is male → Arthur for his character lines
// Mark is male → Arthur for his lines too
// Voice alternation: alternate Arthur/Ellen for variety per rules
// Single words → Arthur
// Phrases alternate Arthur/Ellen throughout material

const PHRASES = [
  // === SURVIVAL / WELCOME (alternate) ===
  { text: "Could you repeat that, please?", voice: ARTHUR },
  { text: "I am not sure I understand. Could you explain?", voice: ELLEN },
  { text: "Let me think about that for a moment.", voice: ARTHUR },
  { text: "That is a great question.", voice: ELLEN },
  { text: "In my experience, I would say...", voice: ARTHUR },

  // === VOCAB WORDS (Arthur — short) ===
  { text: "Defend", voice: ARTHUR },
  { text: "Currently", voice: ARTHUR },
  { text: "Court", voice: ARTHUR },
  { text: "Trial", voice: ARTHUR },
  { text: "Commute", voice: ARTHUR },
  { text: "Challenge", voice: ARTHUR },
  { text: "Experience", voice: ARTHUR },
  { text: "Pursue", voice: ARTHUR },

  // === VOCAB EXAMPLE PHRASES (alternate) ===
  { text: "I defend people in criminal cases.", voice: ELLEN },
  { text: "I am currently working at the Criminal Court.", voice: ARTHUR },
  { text: "The court was in session all morning.", voice: ELLEN },
  { text: "The trial lasted three days.", voice: ARTHUR },
  { text: "I commute between Sao Paulo and Rio de Janeiro every week.", voice: ELLEN },
  { text: "My main challenge is speaking English at conferences.", voice: ARTHUR },
  { text: "I have twenty years of experience in law.", voice: ELLEN },
  { text: "I want to pursue a masters degree in the future.", voice: ARTHUR },

  // === FILL-IN PHRASES (alternate) ===
  { text: "I am a public defender. I defend people in court.", voice: ELLEN },
  { text: "I currently work at the Criminal Court in Sao Paulo.", voice: ARTHUR },
  { text: "My biggest challenge is understanding spoken English.", voice: ELLEN },
  { text: "I commute between two cities every week.", voice: ARTHUR },
  { text: "I have a lot of experience in criminal law.", voice: ELLEN },
  { text: "I want to pursue better English skills.", voice: ARTHUR },

  // === PRONUNCIATION PHRASES ===
  { text: "I am Luiz Bressane. I am a public defender in Sao Paulo.", voice: ARTHUR },
  { text: "I currently work at the Criminal Court in Barra Funda.", voice: ELLEN },

  // === DIALOGUE — Mark (Gartner) = Arthur, Luiz lines = Ellen for alternation ===
  { text: "Hi, I am Mark from Gartner. What do you do?", voice: ARTHUR },
  { text: "Hi, I am Luiz. I am a public defender in Sao Paulo, Brazil.", voice: ELLEN },
  { text: "Interesting! What exactly does a public defender do?", voice: ARTHUR },
  { text: "I defend people in criminal cases. I currently work at the Criminal Court.", voice: ELLEN },
  { text: "How long have you been doing that?", voice: ARTHUR },
  { text: "I have been working in law for over twenty years.", voice: ELLEN },
  { text: "Do you travel for work?", voice: ARTHUR },
  { text: "Yes, I commute between Sao Paulo and Rio de Janeiro every week.", voice: ELLEN },
  { text: "That sounds challenging. What brings you to this conference?", voice: ARTHUR },
  { text: "I want to pursue better English. That is my main challenge right now.", voice: ELLEN },

  // === SURVIVAL IC PHRASES ===
  { text: "I am Luiz Bressane. I am a public defender.", voice: ARTHUR },
  { text: "I commute between Sao Paulo and Rio de Janeiro.", voice: ELLEN },
  { text: "I have over twenty years of experience in law.", voice: ARTHUR },

  // === GRAMMAR EXAMPLES ===
  { text: "Luiz works at the Criminal Court.", voice: ARTHUR },
  { text: "He defends people in criminal cases.", voice: ELLEN },
  { text: "He commutes between two cities.", voice: ARTHUR },
  { text: "He has been working in law for twenty years.", voice: ELLEN },

  // === LISTENING 1 (long passage) ===
  { text: "Good morning, everyone. My name is Luiz Bressane. I am a public defender in Sao Paulo, Brazil. I currently work at the Criminal Court in Barra Funda. I defend people in criminal cases, including jury trials. I have been working in law for over twenty years. My main challenge right now is improving my English for international conferences.", voice: ARTHUR },

  // === ORDER EXERCISE ===
  { text: "My name is Luiz Bressane. I am a public defender in Sao Paulo. I currently work at the Criminal Court. I defend people in criminal cases. I commute between Sao Paulo and Rio de Janeiro every week.", voice: ARTHUR, filename: "order_l1_self_introduction" },
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
  const audioMap = {};

  console.log('Generating ' + unique.length + ' audio files for Luiz Bressane...');
  for (const p of unique) {
    const fname = (p.filename || toFilename(p.text)) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' -- ' + e.message); }
    }
    audioMap[p.text] = '/audio/luiz-bressane/' + fname;
  }

  fs.writeFileSync(path.join(DIR, 'audioMap.json'), JSON.stringify(audioMap, null, 2));
  console.log('\nDone! Generated ' + unique.length + ' unique audio files.');
  console.log('audioMap saved to: ' + path.join(DIR, 'audioMap.json'));
}

main().catch(e => { console.error(e); process.exit(1); });
