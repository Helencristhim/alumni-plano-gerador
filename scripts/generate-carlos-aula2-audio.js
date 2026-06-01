const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q'; // Male - Carlos's voice
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';  // Female - Rachel's voice
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carlos-vinicius-vale-bassan');

// RULE: Carlos = male = ARTHUR for ALL his lines (vocab, exercises, survival, speech cards)
// Ellen ONLY for female character dialogue lines
// Prefix aula2_ to avoid collision with aula1 files

const PHRASES = [
  // === VOCABULARY WORDS (Arthur - male student) ===
  { text: "Specialize", voice: ARTHUR, prefix: "aula2" },
  { text: "Handle", voice: ARTHUR, prefix: "aula2" },
  { text: "Deliver", voice: ARTHUR, prefix: "aula2" },
  { text: "Streamline", voice: ARTHUR, prefix: "aula2" },
  { text: "Navigate", voice: ARTHUR, prefix: "aula2" },
  { text: "Expertise", voice: ARTHUR, prefix: "aula2" },
  { text: "Outcome", voice: ARTHUR, prefix: "aula2" },
  { text: "Track record", voice: ARTHUR, prefix: "aula2" },

  // === PRE-CLASS VOCAB EXAMPLES (Arthur - student's practice sentences) ===
  { text: "I specialize in mergers and acquisitions for the Americas.", voice: ARTHUR, prefix: "aula2" },
  { text: "I handle complex transactions worth over one billion dollars.", voice: ARTHUR, prefix: "aula2" },
  { text: "Our team consistently delivers value for our clients.", voice: ARTHUR, prefix: "aula2" },
  { text: "We streamline the due diligence process using technology.", voice: ARTHUR, prefix: "aula2" },
  { text: "I navigate regulatory challenges across multiple countries.", voice: ARTHUR, prefix: "aula2" },
  { text: "My expertise is in technology-driven corporate transactions.", voice: ARTHUR, prefix: "aula2" },
  { text: "The outcome of the deal exceeded all expectations.", voice: ARTHUR, prefix: "aula2" },
  { text: "Carlos has a strong track record in post-merger integration.", voice: ARTHUR, prefix: "aula2" },

  // === IN CLASS VOCAB EXAMPLES (Arthur - different from Pre-class) ===
  { text: "She specializes in cross-border regulatory compliance.", voice: ARTHUR, prefix: "aula2" },
  { text: "Our team handled three major acquisitions this quarter.", voice: ARTHUR, prefix: "aula2" },
  { text: "The project delivered a twenty percent increase in efficiency.", voice: ARTHUR, prefix: "aula2" },
  { text: "We streamlined the approval process from six weeks to two.", voice: ARTHUR, prefix: "aula2" },
  { text: "He navigated the complex regulatory landscape successfully.", voice: ARTHUR, prefix: "aula2" },
  { text: "Her expertise in fintech made her the ideal consultant.", voice: ARTHUR, prefix: "aula2" },
  { text: "The outcome justified the investment completely.", voice: ARTHUR, prefix: "aula2" },
  { text: "His track record speaks for itself.", voice: ARTHUR, prefix: "aula2" },

  // === EXPRESSIONS (Arthur) ===
  { text: "Be responsible for", voice: ARTHUR, prefix: "aula2" },
  { text: "Have a proven track record", voice: ARTHUR, prefix: "aula2" },
  { text: "Make an impact", voice: ARTHUR, prefix: "aula2" },
  { text: "I am responsible for leading due diligence across the Americas.", voice: ARTHUR, prefix: "aula2" },
  { text: "We have a proven track record of delivering results on time.", voice: ARTHUR, prefix: "aula2" },
  { text: "I want to make an impact in every transaction I work on.", voice: ARTHUR, prefix: "aula2" },

  // === FILL-IN PHRASES (Arthur - student practice) ===
  { text: "I specialize in technology-driven M and A transactions.", voice: ARTHUR, prefix: "aula2" },
  { text: "Our team has delivered results in over twenty transactions.", voice: ARTHUR, prefix: "aula2" },
  { text: "I have navigated regulatory challenges in five countries.", voice: ARTHUR, prefix: "aula2" },
  { text: "The outcome was a thirty percent improvement in efficiency.", voice: ARTHUR, prefix: "aula2" },
  { text: "She has a proven track record in financial advisory.", voice: ARTHUR, prefix: "aula2" },

  // === SPEECH CARDS (Arthur - student practicing) ===
  { text: "I am Carlos Bassan. I specialize in M and A advisory at Accenture, focusing on the Americas.", voice: ARTHUR, prefix: "aula2" },
  { text: "My team has a proven track record of delivering value in complex transactions.", voice: ARTHUR, prefix: "aula2" },
  { text: "I navigate regulatory challenges and streamline due diligence using technology.", voice: ARTHUR, prefix: "aula2" },

  // === SURVIVAL CARD AULA 2 (Arthur - male student) ===
  { text: "I specialize in...", voice: ARTHUR, prefix: "aula2" },
  { text: "We have a proven track record in...", voice: ARTHUR, prefix: "aula2" },
  { text: "The outcome exceeded expectations.", voice: ARTHUR, prefix: "aula2" },
  { text: "Let me walk you through our approach.", voice: ARTHUR, prefix: "aula2" },
  { text: "What sets us apart is our expertise in...", voice: ARTHUR, prefix: "aula2" },

  // === DIALOGUE - Rachel = Ellen (female Senior Partner) ===
  { text: "Carlos, imagine you have sixty seconds in an elevator with a Fortune 500 CEO. Go.", voice: ELLEN, prefix: "aula2" },
  { text: "Good start. Now tell me what makes you different.", voice: ELLEN, prefix: "aula2" },
  { text: "Numbers are powerful. What about the how?", voice: ELLEN, prefix: "aula2" },
  { text: "And the outcome?", voice: ELLEN, prefix: "aula2" },

  // === DIALOGUE - Carlos = Arthur (male student) ===
  { text: "I am Carlos Bassan, a Senior Strategy Executive at Accenture. I specialize in M and A advisory for the Americas.", voice: ARTHUR, prefix: "aula2" },
  { text: "I have a proven track record in technology-driven deals. My team has delivered over two billion dollars in transaction value.", voice: ARTHUR, prefix: "aula2" },
  { text: "We streamline due diligence using technology, and I personally navigate the regulatory landscape across multiple markets.", voice: ARTHUR, prefix: "aula2" },
  { text: "Every deal I have handled has made a measurable impact on the client's bottom line. That is what I bring to the table.", voice: ARTHUR, prefix: "aula2" },

  // === LISTENING 1 - Perfect elevator pitch (Arthur) ===
  { text: "Hi, I am Carlos Bassan from Accenture. I specialize in mergers and acquisitions advisory, focusing on the Americas. My team handles complex, technology-driven transactions. We have a proven track record, having delivered over two billion dollars in deal value. What sets us apart is our expertise in navigating regulatory challenges across multiple markets. We streamline the entire due diligence process using cutting-edge technology, which means faster outcomes and better results for our clients. I would love to discuss how we could help your organization.", voice: ARTHUR, filename: "aula2_listening_1_perfect_pitch" },

  // === LISTENING 2 - Project update call (Ellen - different speaker) ===
  { text: "Good morning, everyone. Quick update on the Rodriguez acquisition. Carlos and his team have completed the technology assessment, and the outcome looks very positive. They streamlined the review process, finishing two weeks ahead of schedule. His expertise in Latin American markets really made an impact. The client has asked us to handle the next phase as well. Carlos will walk you through the details in our meeting on Friday.", voice: ELLEN, filename: "aula2_listening_2_team_update" },

  // === ORDERING ===
  { text: "I am Carlos Bassan from Accenture. I specialize in M and A advisory for the Americas. My team handles complex technology-driven transactions. We have a proven track record of delivering results. What sets us apart is our expertise in navigating regulatory challenges. I would love to discuss how we could help.", voice: ARTHUR, filename: "aula2_order_elevator_pitch" },
];

function toFilename(text, prefix) {
  const base = text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 50);
  return prefix ? prefix + '_' + base : base;
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
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => { const k = p.text.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });

  console.log('Generating ' + unique.length + ' audio files for Aula 2...');
  let ok = 0, skip = 0, fail = 0;
  const audioMapEntries = {};

  for (const p of unique) {
    const fname = (p.filename || toFilename(p.text, p.prefix)) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
      skip++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        ok++;
        await new Promise(r => setTimeout(r, 400));
      } catch(e) {
        console.error('FAIL: ' + fname + ' — ' + e.message);
        fail++;
      }
    }
    audioMapEntries[p.text] = '/audio/carlos-vinicius-vale-bassan/' + fname;
  }

  // Write audioMap JSON for easy copy
  const mapPath = path.join(DIR, 'aula2_audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMapEntries, null, 2));

  console.log('\nDone! OK: ' + ok + ' | Skip: ' + skip + ' | Fail: ' + fail);
  console.log('AudioMap saved to: ' + mapPath);

  // Output the audioMap entries for HTML insertion
  console.log('\n// === AUDIOMAP ENTRIES FOR AULA 2 ===');
  Object.entries(audioMapEntries).forEach(([k, v]) => {
    console.log('  "' + k.replace(/"/g, '\\"') + '": "' + v + '",');
  });
}

main().catch(e => { console.error(e); process.exit(1); });
