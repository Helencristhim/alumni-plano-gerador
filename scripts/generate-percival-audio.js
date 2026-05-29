const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'percival-jr');

// Percival is male → Arthur for his lines
// Sarah Miller is female → Ellen for her lines
// Single words (1-2) → ALWAYS Arthur
// Phrases (3+) → ALTERNATE Arthur/Ellen
const PHRASES = [
  // Emergency phrases (alternate Arthur/Ellen)
  { text: "Could you repeat that, please?", voice: ARTHUR },
  { text: "I do not understand. Could you explain?", voice: ELLEN },
  { text: "Let me think for a moment.", voice: ARTHUR },
  { text: "Could I ask a question?", voice: ELLEN },
  { text: "My name is Percival. Nice to meet you.", voice: ARTHUR },

  // Vocab words (1-2 words → ALWAYS Arthur)
  { text: "Role", voice: ARTHUR },
  { text: "Responsible", voice: ARTHUR },
  { text: "Team", voice: ARTHUR },
  { text: "Company", voice: ARTHUR },
  { text: "Meeting", voice: ARTHUR },
  { text: "Travel", voice: ARTHUR },
  { text: "Goal", voice: ARTHUR },
  { text: "Manage", voice: ARTHUR },

  // Vocab example sentences (alternate — Percival context = Arthur for his own lines)
  { text: "My role is Director of Risk and Internal Audit.", voice: ARTHUR },
  { text: "I am responsible for the audit team.", voice: ELLEN },
  { text: "I manage a team of ten people.", voice: ARTHUR },
  { text: "I work at a large company in São Paulo.", voice: ELLEN },
  { text: "I have a meeting with the directors.", voice: ARTHUR },
  { text: "I travel to New York next month.", voice: ELLEN },
  { text: "My goal is to speak English fluently.", voice: ARTHUR },
  { text: "I manage risk and internal audit at my company.", voice: ELLEN },

  // Fill-in-the-blank phrases (alternate)
  { text: "I work at EGEA Saneamento in São Paulo.", voice: ARTHUR },
  { text: "He is responsible for the risk team.", voice: ELLEN },
  { text: "My goal is to improve my English.", voice: ARTHUR },
  { text: "She manages a team of ten people.", voice: ELLEN },
  { text: "I travel to conferences in the United States.", voice: ARTHUR },
  { text: "We have a meeting every Monday.", voice: ELLEN },

  // Speech/Pronunciation cards (Percival = Arthur)
  { text: "My name is Percival. I work at EGEA Saneamento.", voice: ARTHUR },
  { text: "I am responsible for risk and internal audit.", voice: ELLEN },
  { text: "My goal is to speak English with confidence.", voice: ARTHUR },

  // Survival Card (alternate)
  { text: "My name is Percival. I am the Director of Risk.", voice: ARTHUR },
  { text: "I am responsible for internal audit.", voice: ELLEN },

  // Dialogue — Sarah Miller = Ellen (female)
  { text: "Hi! I am Sarah Miller. I work as a risk consultant at Deloitte. Are you in the risk field too?", voice: ELLEN },
  { text: "That sounds interesting! What does your team do?", voice: ELLEN },
  { text: "How long have you been working in risk management?", voice: ELLEN },
  { text: "Are you attending the session this afternoon?", voice: ELLEN },

  // Dialogue — Percival = Arthur (male)
  { text: "Nice to meet you, Sarah! My name is Percival. I am the Director of Risk at EGEA Saneamento.", voice: ARTHUR },
  { text: "I manage a team of specialists. We are responsible for the company risk matrix and internal audit.", voice: ARTHUR },
  { text: "I have been in risk management for many years. I really enjoy it.", voice: ARTHUR },
  { text: "Yes! I am here because I want to learn about new practices. My goal is to improve risk management at my company.", voice: ARTHUR },

  // Listening 1 — Percival's conference self-introduction (Arthur — long)
  { text: "Good morning, everyone. My name is Percival Junior. I am the Director of Risk and Internal Audit at EGEA Saneamento in São Paulo, Brazil. I manage a team of specialists. We are responsible for the company risk matrix. I am here because I want to connect with risk professionals. My goal is to learn about new practices.", voice: ARTHUR },

  // Listening 2 — Q&A lines
  { text: "Thank you for your introduction, Percival. I have a question about your team.", voice: ELLEN },
  { text: "Of course. Please go ahead.", voice: ARTHUR },
  { text: "How many people are on your team, and what do they do?", voice: ELLEN },
  { text: "I manage a team of ten specialists. They are responsible for internal audit, risk assessment, and compliance.", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Percival JR...');
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + fname + ' — ' + e.message); }
    }
    audioMap[p.text] = '/audio/percival-jr/' + fname;
  }

  fs.writeFileSync(path.join(DIR, 'audioMap.json'), JSON.stringify(audioMap, null, 2));
  console.log('\nDone! Generated ' + Object.keys(audioMap).length + ' entries.');
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
