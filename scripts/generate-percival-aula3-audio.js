const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'percival-jr-aula3');

// Percival = male → Arthur
// Lisa Park = female → Ellen
// Single words (1-2) → ALWAYS Arthur
// Phrases (3+) → ALTERNATE Arthur/Ellen
const PHRASES = [
  // Emergency/survival (alternate)
  { text: "Could you repeat that, please?", voice: ARTHUR },
  { text: "I am not sure I understand.", voice: ELLEN },
  { text: "Could you speak more slowly?", voice: ARTHUR },
  { text: "Let me think for a moment.", voice: ELLEN },
  { text: "I wear many hats.", voice: ARTHUR },

  // Vocab words (1-2 words → Arthur)
  { text: "Risk", voice: ARTHUR },
  { text: "Audit", voice: ARTHUR },
  { text: "Compliance", voice: ARTHUR },
  { text: "Report", voice: ARTHUR },
  { text: "Oversee", voice: ARTHUR },
  { text: "Operations", voice: ARTHUR },
  { text: "Internal", voice: ARTHUR },
  { text: "Director", voice: ARTHUR },

  // Vocab example sentences (alternate)
  { text: "I work in risk management.", voice: ARTHUR },
  { text: "My team does internal audit.", voice: ELLEN },
  { text: "Compliance is very important in our company.", voice: ARTHUR },
  { text: "I report to the executive board.", voice: ELLEN },
  { text: "I oversee the audit process.", voice: ARTHUR },
  { text: "I manage risk operations.", voice: ELLEN },
  { text: "I am the Director of Internal Audit.", voice: ARTHUR },
  { text: "The director manages the risk team.", voice: ELLEN },

  // Additional professional phrases
  { text: "I lead a team of ten specialists.", voice: ARTHUR },
  { text: "My team handles risk assessment and compliance.", voice: ELLEN },
  { text: "I work closely with the executive board.", voice: ARTHUR },
  { text: "I oversee all internal audit activities.", voice: ELLEN },
  { text: "I am responsible for the company risk matrix.", voice: ARTHUR },
  { text: "I report to the executive board every month.", voice: ELLEN },

  // Speech cards / survival (Percival = Arthur)
  { text: "My name is Percival. I am the Director of Risk and Internal Audit at EGEA Saneamento.", voice: ARTHUR },
  { text: "I lead a team of specialists. We handle risk assessment, compliance, and internal audit.", voice: ELLEN },
  { text: "I report to the executive board and I work closely with operations.", voice: ARTHUR },

  // Dialogue — Lisa Park = Ellen (female)
  { text: "Hi! I am Lisa Park. I am a risk consultant at PwC. What do you do?", voice: ELLEN },
  { text: "That is interesting! What does your team do?", voice: ELLEN },
  { text: "Who do you report to?", voice: ELLEN },
  { text: "It sounds like you wear many hats! Do you enjoy it?", voice: ELLEN },

  // Dialogue — Percival = Arthur (male)
  { text: "Nice to meet you, Lisa! I am Percival, the Director of Risk and Internal Audit at EGEA Saneamento.", voice: ARTHUR },
  { text: "I lead a team of ten specialists. We oversee risk assessment and internal audit.", voice: ARTHUR },
  { text: "I report to the executive board. I work closely with the operations team.", voice: ARTHUR },
  { text: "Yes, I do! I really enjoy working with my team. We handle important projects for the company.", voice: ARTHUR },

  // Listening 1 — long professional intro (Arthur)
  { text: "Good morning, everyone. My name is Percival Junior. I am the Director of Risk and Internal Audit at EGEA Saneamento in São Paulo. I lead a team of ten specialists. My team handles risk assessment, compliance, and internal audit. I report to the executive board. I work closely with the operations team. I wear many hats, but I really enjoy my work.", voice: ARTHUR },

  // Listening 2 — Q&A about compliance
  { text: "Tell me more about compliance at your company.", voice: ELLEN },
  { text: "Compliance is very important at EGEA. We follow strict regulations because we work in sanitation.", voice: ARTHUR },
  { text: "How often do you report to the board?", voice: ELLEN },
  { text: "I report to the board every month. We present our risk matrix and audit findings.", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Percival JR — Aula 3...');
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
  }

  console.log('\nDone! Generated ' + unique.length + ' entries.');
}

main().catch(e => { console.error(e); process.exit(1); });
