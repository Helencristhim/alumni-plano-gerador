const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carlos-vinicius-vale-bassan');

// Carlos = male = ARTHUR for ALL his lines
// Amanda Torres = female = ELLEN for her dialogue lines

const PHRASES = [
  // === VOCAB WORDS (Arthur) ===
  { text: "Network", voice: ARTHUR, prefix: "aula3" },
  { text: "Connect", voice: ARTHUR, prefix: "aula3" },
  { text: "Approach", voice: ARTHUR, prefix: "aula3" },
  { text: "Engage", voice: ARTHUR, prefix: "aula3" },
  { text: "Mention", voice: ARTHUR, prefix: "aula3" },
  { text: "Relate", voice: ARTHUR, prefix: "aula3" },
  { text: "Insight", voice: ARTHUR, prefix: "aula3" },
  { text: "Agenda", voice: ARTHUR, prefix: "aula3" },

  // === PRE-CLASS VOCAB EXAMPLES (Arthur) ===
  { text: "I always network at industry conferences.", voice: ARTHUR, prefix: "aula3" },
  { text: "I would love to connect with you after the presentation.", voice: ARTHUR, prefix: "aula3" },
  { text: "He approached me during the coffee break to discuss the deal.", voice: ARTHUR, prefix: "aula3" },
  { text: "She knows how to engage people in meaningful conversations.", voice: ARTHUR, prefix: "aula3" },
  { text: "He mentioned that the project deadline was moved to Friday.", voice: ARTHUR, prefix: "aula3" },
  { text: "I can relate to the challenges of working across time zones.", voice: ARTHUR, prefix: "aula3" },
  { text: "Her insight on the Latin American market was very valuable.", voice: ARTHUR, prefix: "aula3" },
  { text: "What is on the agenda for today's meeting?", voice: ARTHUR, prefix: "aula3" },

  // === IN CLASS VOCAB EXAMPLES (Arthur - different from Pre-class) ===
  { text: "Networking is essential for building long-term business relationships.", voice: ARTHUR, prefix: "aula3" },
  { text: "We connected over our shared interest in technology-driven M and A.", voice: ARTHUR, prefix: "aula3" },
  { text: "The best time to approach someone is during a coffee break.", voice: ARTHUR, prefix: "aula3" },
  { text: "Carlos engages his clients by asking thoughtful questions.", voice: ARTHUR, prefix: "aula3" },
  { text: "She mentioned that the acquisition was on track.", voice: ARTHUR, prefix: "aula3" },
  { text: "I can really relate to your experience with cross-border deals.", voice: ARTHUR, prefix: "aula3" },
  { text: "That is a great insight. I had not thought of it that way.", voice: ARTHUR, prefix: "aula3" },
  { text: "Let me check the agenda before we start.", voice: ARTHUR, prefix: "aula3" },

  // === EXPRESSIONS (Arthur) ===
  { text: "Break the ice", voice: ARTHUR, prefix: "aula3" },
  { text: "Common ground", voice: ARTHUR, prefix: "aula3" },
  { text: "Touch base", voice: ARTHUR, prefix: "aula3" },
  { text: "A good question can break the ice at any networking event.", voice: ARTHUR, prefix: "aula3" },
  { text: "Finding common ground makes conversations feel natural.", voice: ARTHUR, prefix: "aula3" },
  { text: "Let me touch base with you next week about the proposal.", voice: ARTHUR, prefix: "aula3" },

  // === FILL-IN PHRASES (Arthur) ===
  { text: "I love to network at conferences because I always meet interesting people.", voice: ARTHUR, prefix: "aula3" },
  { text: "Could you mention this to the team before the meeting?", voice: ARTHUR, prefix: "aula3" },
  { text: "We need to find common ground before we can move forward.", voice: ARTHUR, prefix: "aula3" },
  { text: "She approached the CEO and introduced herself confidently.", voice: ARTHUR, prefix: "aula3" },
  { text: "His insight helped us understand the regulatory landscape.", voice: ARTHUR, prefix: "aula3" },

  // === SPEECH CARDS (Arthur) ===
  { text: "Hi, I am Carlos from Accenture. What brings you to the conference?", voice: ARTHUR, prefix: "aula3" },
  { text: "That is really interesting. I can relate to that challenge. We face something similar in M and A.", voice: ARTHUR, prefix: "aula3" },
  { text: "It was great connecting with you. Let me touch base next week.", voice: ARTHUR, prefix: "aula3" },

  // === SURVIVAL CARD AULA 3 (Arthur) ===
  { text: "What brings you to this event?", voice: ARTHUR, prefix: "aula3" },
  { text: "How did you get into that field?", voice: ARTHUR, prefix: "aula3" },
  { text: "That is really interesting. Tell me more.", voice: ARTHUR, prefix: "aula3" },
  { text: "We should definitely connect.", voice: ARTHUR, prefix: "aula3" },
  { text: "It was great talking to you.", voice: ARTHUR, prefix: "aula3" },

  // === DIALOGUE - Amanda Torres = Ellen (female VP) ===
  { text: "Hi! I do not think we have met. I am Amanda Torres, VP of Corporate Development at NovaTech. And you?", voice: ELLEN, prefix: "aula3" },
  { text: "M and A advisory, that sounds fascinating. What kind of deals do you usually work on?", voice: ELLEN, prefix: "aula3" },
  { text: "I can relate to that. We are actually looking at expanding into Brazil. It is such a complex market.", voice: ELLEN, prefix: "aula3" },
  { text: "That is a great insight. I had not thought about using technology to speed up due diligence. How does that work exactly?", voice: ELLEN, prefix: "aula3" },

  // === DIALOGUE - Carlos = Arthur ===
  { text: "Hi Amanda, great to meet you. I am Carlos Bassan from Accenture. I specialize in M and A advisory for the Americas.", voice: ARTHUR, prefix: "aula3" },
  { text: "Mostly technology-driven acquisitions. My team handles everything from due diligence to post-merger integration.", voice: ARTHUR, prefix: "aula3" },
  { text: "Absolutely. Brazil has unique regulatory challenges, but that is exactly where my team's expertise comes in. We help companies navigate that landscape.", voice: ARTHUR, prefix: "aula3" },
  { text: "We use data analytics to streamline the entire process. It cuts the timeline significantly. I would love to walk you through it. Could we touch base next week?", voice: ARTHUR, prefix: "aula3" },

  // === LISTENING 1 - Networking at conference (Arthur) ===
  { text: "Excuse me, do you mind if I join you? I noticed your badge says NovaTech. I have been following your company's growth in the fintech space. I am Carlos Bassan from Accenture. We specialize in M and A advisory for the Americas. What brings you to the summit today? I am curious about your perspective on cross-border acquisitions in Latin America. We have been seeing a lot of activity in that space recently.", voice: ARTHUR, filename: "aula3_listening_1_networking" },

  // === LISTENING 2 - Overheard conversation at event (Ellen) ===
  { text: "So I was at this conference in Miami last month, and I approached someone from Accenture. We started talking about M and A trends in Latin America, and it turns out we had so much common ground. He mentioned that his team uses technology to streamline due diligence, which I found really insightful. We connected on LinkedIn right away, and now we are exploring a potential partnership. You never know who you will meet at these events.", voice: ELLEN, filename: "aula3_listening_2_overheard" },

  // === ORDERING ===
  { text: "Hi, I do not think we have met. I am Carlos from Accenture. What brings you to the conference? That is really interesting. I can relate to that challenge. We should definitely connect. It was great talking to you.", voice: ARTHUR, filename: "aula3_order_small_talk" },
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

  console.log('Generating ' + unique.length + ' audio files for Aula 3...');
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

  // Add listening + order keys
  audioMapEntries['[aula3-listening-1]'] = '/audio/carlos-vinicius-vale-bassan/aula3_listening_1_networking.mp3';
  audioMapEntries['[aula3-listening-2]'] = '/audio/carlos-vinicius-vale-bassan/aula3_listening_2_overheard.mp3';
  audioMapEntries['[order-l3]'] = '/audio/carlos-vinicius-vale-bassan/aula3_order_small_talk.mp3';

  fs.writeFileSync(path.join(DIR, 'aula3_audioMap.json'), JSON.stringify(audioMapEntries, null, 2));
  console.log('\nDone! OK: ' + ok + ' | Skip: ' + skip + ' | Fail: ' + fail);
}

main().catch(e => { console.error(e); process.exit(1); });
