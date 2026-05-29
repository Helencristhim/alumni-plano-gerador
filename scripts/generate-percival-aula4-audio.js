const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'percival-jr-aula4');

const PHRASES = [
  // Emergency/survival (alternate)
  { text: "Could you repeat that, please?", voice: ARTHUR },
  { text: "I am not sure I understand.", voice: ELLEN },
  { text: "It depends on the situation.", voice: ARTHUR },
  { text: "At the moment, I am focused on compliance.", voice: ELLEN },
  { text: "We are still working on that.", voice: ARTHUR },

  // Vocab words (1-2 → Arthur)
  { text: "Risk matrix", voice: ARTHUR },
  { text: "Ongoing", voice: ARTHUR },
  { text: "Review", voice: ARTHUR },
  { text: "Action plan", voice: ARTHUR },
  { text: "Deadline", voice: ARTHUR },
  { text: "Stakeholder", voice: ARTHUR },
  { text: "Currently", voice: ARTHUR },
  { text: "Challenge", voice: ARTHUR },

  // Vocab examples (alternate)
  { text: "We are updating the risk matrix this month.", voice: ARTHUR },
  { text: "We have an ongoing review of the operations.", voice: ELLEN },
  { text: "My team is reviewing the internal controls.", voice: ARTHUR },
  { text: "We are developing an action plan.", voice: ELLEN },
  { text: "The deadline is next Friday.", voice: ARTHUR },
  { text: "I am meeting with the stakeholders today.", voice: ELLEN },
  { text: "I am currently leading a new project.", voice: ARTHUR },
  { text: "The biggest challenge is the tight deadline.", voice: ELLEN },

  // Additional professional phrases
  { text: "Right now, we are reviewing the risk matrix.", voice: ARTHUR },
  { text: "My team is conducting an internal audit this week.", voice: ELLEN },
  { text: "We are working on a new compliance check.", voice: ARTHUR },
  { text: "I am preparing a report for the executive board.", voice: ELLEN },
  { text: "We are not ignoring the issue. We are working on an action plan.", voice: ARTHUR },
  { text: "I am currently focused on risk assessment.", voice: ELLEN },

  // Dialogue — Amanda Ross = Ellen, Percival = Arthur
  { text: "Hi Percival! What are you working on at EGEA right now?", voice: ELLEN },
  { text: "Right now, I am leading an internal audit of the operations department.", voice: ARTHUR },
  { text: "That sounds important. What is your team doing?", voice: ELLEN },
  { text: "My team is reviewing the internal controls and updating the risk matrix.", voice: ARTHUR },
  { text: "Are you facing any challenges?", voice: ELLEN },
  { text: "Yes, we are dealing with a tight deadline. The board is expecting the report next month.", voice: ARTHUR },
  { text: "When will the audit be finished?", voice: ELLEN },
  { text: "It depends on the stakeholders. We are still waiting for some documents.", voice: ARTHUR },

  // Listening 1 — weekly update (Arthur, long)
  { text: "This week, I am reviewing the risk matrix for EGEA. My team is conducting an internal audit in the operations department. We are developing an action plan for the new compliance requirements. I am currently focused on meeting the deadline for the executive board report.", voice: ARTHUR },

  // Listening 2 — Q&A
  { text: "What are you focusing on this month?", voice: ELLEN },
  { text: "I am focusing on the annual risk review.", voice: ARTHUR },
  { text: "Is your team handling any big audits right now?", voice: ELLEN },
  { text: "Yes, we are conducting a full audit of the operations department.", voice: ARTHUR },
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
  console.log('Generating ' + unique.length + ' audio files for Percival JR — Aula 4...');
  for (const p of unique) {
    const fname = toFilename(p.text) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + fname); }
    else {
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
