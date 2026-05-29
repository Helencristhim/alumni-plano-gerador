const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'diogo-leal');

// Diogo is male → Arthur for his dialogue lines
// David is male → Arthur for his dialogue lines
// Single words (1-2 words) → ALWAYS Arthur
// Emergency phrases → alternate Ellen/Arthur starting with Ellen
// Vocab example sentences → alternate Arthur/Ellen
// Fill-in-blank phrases → alternate Arthur/Ellen
// Listening narrations → Ellen for full narration MP3s
const PHRASES = [
  // ===== Emergency phrases (alternate Ellen/Arthur starting with Ellen) =====
  { text: "Could you repeat that, please?", voice: ELLEN },
  { text: "I am not sure I understand. Could you explain?", voice: ARTHUR },
  { text: "Let me think about that for a moment.", voice: ELLEN },
  { text: "That is a great question.", voice: ARTHUR },
  { text: "In my experience, I would say...", voice: ELLEN },

  // ===== Vocab words (single words — ALWAYS Arthur) =====
  { text: "Manage", voice: ARTHUR },
  { text: "Responsible", voice: ARTHUR },
  { text: "Currently", voice: ARTHUR },
  { text: "Experience", voice: ARTHUR },
  { text: "Challenge", voice: ARTHUR },
  { text: "Stakeholder", voice: ARTHUR },
  { text: "Scope", voice: ARTHUR },
  { text: "Launch", voice: ARTHUR },

  // ===== Pre-class vocab example sentences (alternate Arthur/Ellen) =====
  { text: "I manage a team of fifteen engineers at Oracle.", voice: ARTHUR },
  { text: "I am responsible for projects across Latin America and the United States.", voice: ELLEN },
  { text: "I am currently launching a new app for pet tutors.", voice: ARTHUR },
  { text: "I have over fifteen years of experience in IT.", voice: ELLEN },
  { text: "My biggest challenge right now is communicating with executive stakeholders.", voice: ARTHUR },
  { text: "The stakeholders are expecting a progress update by Friday.", voice: ELLEN },
  { text: "The scope of this project covers five countries in Latin America.", voice: ARTHUR },
  { text: "We are planning to launch the app in the American market.", voice: ELLEN },

  // ===== Fill-in-blank data-phrase sentences =====
  { text: "I am responsible for managing IT projects at Oracle.", voice: ARTHUR },
  { text: "My biggest challenge right now is executive communication.", voice: ELLEN },
  { text: "I currently manage a team of fifteen engineers.", voice: ARTHUR },
  { text: "The scope of my work covers Latin America and the United States.", voice: ELLEN },

  // ===== Speech card phrases =====
  { text: "I am Diogo Leal. I manage IT projects at Oracle.", voice: ARTHUR },
  { text: "My biggest challenge right now is executive communication in English.", voice: ELLEN },

  // ===== Survival card phrases (alternate Arthur/Ellen) =====
  { text: "I am Diogo Leal. I work at Oracle.", voice: ARTHUR },
  { text: "I am responsible for IT projects across Latin America.", voice: ELLEN },
  { text: "I am currently launching a new app.", voice: ARTHUR },

  // ===== Dialogue — David (male) = Arthur =====
  { text: "Hi, I am David. I work in IT consulting. What about you?", voice: ARTHUR },
  { text: "Oracle! That sounds interesting. What are you responsible for?", voice: ARTHUR },
  { text: "That is a big scope. What is your biggest challenge right now?", voice: ARTHUR },
  { text: "I understand. How long have you been working in IT?", voice: ARTHUR },

  // ===== Dialogue — Diogo (male) = Arthur =====
  { text: "Nice to meet you, David. I am Diogo Leal. I manage IT projects at Oracle.", voice: ARTHUR },
  { text: "I am responsible for managing projects across Latin America and the United States.", voice: ARTHUR },
  { text: "My biggest challenge right now is communicating with executive stakeholders in English.", voice: ARTHUR },
  { text: "I have over fifteen years of experience. I am currently launching an app for pet tutors.", voice: ARTHUR },

  // ===== Grammar examples =====
  { text: "I work at Oracle.", voice: ARTHUR },
  { text: "I manage a team of engineers.", voice: ARTHUR },
  { text: "I live in Sao Paulo.", voice: ARTHUR },
  { text: "She manages the project budget.", voice: ELLEN },

  // ===== Listening narrations (Ellen — full MP3s) =====
  { text: "Hi everyone, my name is David Chen. I work at a consulting firm in San Francisco. I am responsible for cloud infrastructure projects across the West Coast. I have been in IT consulting for about twelve years now. My biggest challenge right now is managing remote teams across different time zones. I am currently working on a major migration project for a healthcare client. The scope is huge, but the experience has been incredible.", voice: ELLEN, filename: "listening_1_david_introduction" },
  { text: "Diogo Leal has been working in Information Technology for over fifteen years. He currently manages projects at Oracle, covering Latin America and the United States. His main client is AT and T. Diogo is responsible for coordinating with engineering teams across multiple countries. Recently, he launched his own application for pet tutors in the American market. Despite his technical expertise, his biggest challenge is communicating with executive stakeholders outside of technical vocabulary.", voice: ELLEN, filename: "listening_2_diogo_journey" },
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
  if (!API_KEY) { console.error('No API key. Set ELEVENLABS_API_KEY env variable.'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => {
    const k = p.text.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });
  const audioMap = {};

  console.log('Generating ' + unique.length + ' audio files for Diogo Leal...\n');
  for (const p of unique) {
    const fname = (p.filename || toFilename(p.text)) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch (e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
    }
    audioMap[p.text] = '/audio/diogo-leal/' + fname;
  }

  fs.writeFileSync(path.join(DIR, 'audioMap.json'), JSON.stringify(audioMap, null, 2));
  console.log('\nDone! Generated ' + unique.length + ' entries.');
  console.log('\n// Paste into HTML:');
  console.log('var audioMap = ' + JSON.stringify(audioMap, null, 2) + ';');
}

main().catch(e => { console.error(e); process.exit(1); });
