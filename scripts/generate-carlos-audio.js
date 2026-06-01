const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carlos-vinicius-vale-bassan');

// Carlos is male → Arthur for his lines, vocab words, student exercises
// Sarah Mitchell is female → Ellen for her lines
// General phrases → alternate Arthur/Ellen
const PHRASES = [
  // Vocabulary words (Arthur — male student)
  { text: "Lead", voice: ARTHUR },
  { text: "Assess", voice: ARTHUR },
  { text: "Oversee", voice: ARTHUR },
  { text: "Brief", voice: ARTHUR },
  { text: "Drive", voice: ARTHUR },
  { text: "Articulate", voice: ARTHUR },
  { text: "Leverage", voice: ARTHUR },
  { text: "Align", voice: ARTHUR },
  { text: "Pitch", voice: ARTHUR },
  // Vocab example sentences (Arthur — student's voice for practice)
  { text: "I lead the due diligence team for global transactions.", voice: ARTHUR },
  { text: "We need to assess the financial risks before the acquisition.", voice: ARTHUR },
  { text: "I oversee post-merger integration projects across Latin America.", voice: ARTHUR },
  { text: "I need to brief the CEO on the latest deal updates.", voice: ARTHUR },
  { text: "Our team drives value creation in every transaction.", voice: ARTHUR },
  { text: "An articulate consultant builds trust with C-level executives.", voice: ELLEN },
  { text: "We leverage data analytics to improve deal outcomes.", voice: ARTHUR },
  { text: "We need to align our approach with the client's vision.", voice: ELLEN },
  { text: "Carlos delivered a compelling pitch to the PE fund partners.", voice: ELLEN },
  // Additional vocab examples (IN CLASS — different from Pre-class, alternate)
  { text: "I lead the M&A advisory practice for the Americas region.", voice: ARTHUR },
  { text: "We assessed the target company and identified key risks.", voice: ELLEN },
  { text: "He oversees a team of twelve consultants across three offices.", voice: ARTHUR },
  { text: "I briefed the board on our acquisition strategy last quarter.", voice: ARTHUR },
  { text: "Our practice has driven over two billion dollars in deal value.", voice: ELLEN },
  // Speech card phrases (Arthur — student practicing)
  { text: "I am a Senior Strategy Executive at Accenture, based in Sao Paulo.", voice: ARTHUR },
  { text: "I have been working in M&A advisory for over ten years.", voice: ARTHUR },
  { text: "I currently oversee post-merger integration across the Americas.", voice: ARTHUR },
  // Survival phrases (Arthur — male student, alternate)
  { text: "Could you repeat that, please?", voice: ARTHUR },
  { text: "I am not sure I understand. Could you explain?", voice: ELLEN },
  { text: "Let me think about that for a moment.", voice: ARTHUR },
  { text: "That is a great question.", voice: ELLEN },
  { text: "In my experience, I would say...", voice: ARTHUR },
  // Fill-in / practice phrases (Arthur)
  { text: "I lead the due diligence process for cross-border deals.", voice: ARTHUR },
  { text: "We need to align our strategy with the client's goals.", voice: ARTHUR },
  { text: "He drove the integration and delivered results ahead of schedule.", voice: ELLEN },
  { text: "We leveraged our network to find the right acquisition target.", voice: ARTHUR },
  { text: "The pitch convinced the private equity partners to invest.", voice: ELLEN },
  // Dialogue — Sarah Mitchell = Ellen (female)
  { text: "Hi there! I am Sarah Mitchell, Managing Partner at Deloitte. What do you do?", voice: ELLEN },
  { text: "Impressive! How long have you been doing that?", voice: ELLEN },
  { text: "That sounds like a complex role. What is the biggest challenge you face?", voice: ELLEN },
  { text: "Absolutely. We should connect. I would love to hear more about your approach.", voice: ELLEN },
  // Dialogue — Carlos = Arthur (male)
  { text: "Nice to meet you, Sarah. I am Carlos Bassan, a Senior Strategy Executive at Accenture. I lead M and A advisory for the Americas.", voice: ARTHUR },
  { text: "I have been working in M and A advisory for over ten years. I currently oversee post-merger integration across three regions.", voice: ARTHUR },
  { text: "I would say it is aligning stakeholders across different countries. Each market has unique regulatory requirements.", voice: ARTHUR },
  { text: "Absolutely. Let me brief you on a recent deal we closed. I think you will find it very relevant.", voice: ARTHUR },
  // Listening 1 — conference self-introduction (Arthur — student's voice)
  { text: "Good morning, everyone. My name is Carlos Bassan. I am a Senior Strategy Executive at Accenture, based in Sao Paulo, Brazil. I specialize in mergers and acquisitions, specifically in due diligence and post-merger integration. Over the past fifteen years, I have worked with multinational companies across the Americas, helping them assess risks, drive value creation, and leverage technology in corporate transactions.", voice: ARTHUR, filename: "listening_1_conference_intro" },
  // Listening 2 — project update (Ellen — different speaker for variety)
  { text: "Hi team, I just wanted to briefly update you on the Johnson deal. We completed the initial assessment last week, and the preliminary findings look positive. The target company has strong fundamentals, but there are some regulatory risks we need to address. Next steps: Carlos will oversee the financial due diligence, and I will lead the technology assessment. We need to align on our final recommendation by Friday.", voice: ELLEN, filename: "listening_2_project_update" },
  // Ordering exercise
  { text: "Hi, I am Carlos Bassan. I am a Senior Strategy Executive at Accenture. I lead the M and A advisory practice for the Americas. My team assesses risks and oversees due diligence. I joined Accenture about two years ago. I would love to discuss how we could align on this opportunity.", voice: ARTHUR, filename: "order_l1_self_introduction" },
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

  console.log('Generating ' + unique.length + ' audio files for Carlos Vinicius Vale Bassan...');
  let ok = 0, skip = 0, fail = 0;

  for (const p of unique) {
    const fname = (p.filename || toFilename(p.text)) + '.mp3';
    const outPath = path.join(DIR, fname);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + fname);
      skip++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + fname + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        ok++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) {
        console.error('FAIL: ' + fname + ' — ' + e.message);
        fail++;
      }
    }
  }

  console.log('\nDone! OK: ' + ok + ' | Skip: ' + skip + ' | Fail: ' + fail);
}

main().catch(e => { console.error(e); process.exit(1); });
