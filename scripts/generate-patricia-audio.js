const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'patricia-ruffo');

// Patricia is female → Ellen for her lines
// Dr. Lee is male → Arthur for his lines
// Single words → Arthur
// Phrases alternate Arthur/Ellen
const PHRASES = [
  // Emergency phrases (alternate)
  { text: "Could you repeat that, please?", voice: ELLEN },
  { text: "I am not sure I understand. Could you explain?", voice: ARTHUR },
  { text: "Let me think about that for a moment.", voice: ELLEN },
  { text: "That is a great question.", voice: ARTHUR },
  { text: "In my experience, I would say...", voice: ELLEN },
  // Vocab words (Arthur — short)
  { text: "Introduce", voice: ARTHUR },
  { text: "Collaborate", voice: ARTHUR },
  { text: "Responsible", voice: ARTHUR },
  { text: "Currently", voice: ARTHUR },
  { text: "Clinical Research", voice: ARTHUR },
  { text: "Functional Ingredients", voice: ARTHUR },
  { text: "Glycemic Control", voice: ARTHUR },
  { text: "Trial", voice: ARTHUR },
  // Vocab example sentences (alternate, Patricia = Ellen)
  { text: "Let me introduce myself. I am Patricia Ruffo.", voice: ELLEN },
  { text: "I am a clinical nutritionist at Abbott.", voice: ELLEN },
  { text: "I have been working in clinical research for over twenty years.", voice: ELLEN },
  { text: "I am currently focused on glycemic control.", voice: ELLEN },
  { text: "I would love to discuss this further.", voice: ELLEN },
  // Dialogue — Dr. Lee = Arthur (male)
  { text: "Hi! I am Dr. Lee from Seoul National University. Are you presenting today?", voice: ARTHUR },
  { text: "Nice to meet you! What is your presentation about?", voice: ARTHUR },
  { text: "That sounds fascinating! How long have you been in clinical research?", voice: ARTHUR },
  { text: "Impressive! I would love to hear more. Are you free after your presentation?", voice: ARTHUR },
  // Dialogue — Patricia = Ellen (female)
  { text: "Yes! Let me introduce myself. I am Patricia Ruffo, a clinical nutritionist at Abbott.", voice: ELLEN },
  { text: "I am currently working on glycemic control with functional ingredients. Our latest trial has shown very promising results.", voice: ELLEN },
  { text: "I have been in clinical research for over twenty years. I collaborate with several universities in Brazil.", voice: ELLEN },
  { text: "Absolutely! I am responsible for the afternoon session, but I am free after four. Let us connect!", voice: ELLEN },
  // Survival card / pronunciation (Patricia = Ellen)
  { text: "Let me introduce myself. I am Patricia Ruffo from Abbott.", voice: ELLEN },
  { text: "I am currently working on glycemic control research.", voice: ELLEN },
  { text: "I have been collaborating with universities for over ten years.", voice: ELLEN },
  { text: "Our latest trial has shown very promising results.", voice: ELLEN },
  // Listening — conference announcement (Ellen formal)
  { text: "Good afternoon, everyone. My name is Patricia Ruffo. I am a clinical nutritionist at Abbott, based in Sao Paulo, Brazil. I am currently working on glycemic control with functional ingredients. I have been collaborating with universities for over ten years, and our latest trial has shown very promising results.", voice: ELLEN },
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
  if (!API_KEY) { console.error('No API key'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => { const k = p.text.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });
  const audioMap = {};

  console.log('Generating ' + unique.length + ' audio files...');
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
    audioMap[p.text] = '/audio/patricia-ruffo/' + fname;
  }

  fs.writeFileSync(path.join(DIR, 'audioMap.json'), JSON.stringify(audioMap, null, 2));
  console.log('\n// Paste into HTML:');
  console.log('var audioMap = ' + JSON.stringify(audioMap, null, 2) + ';');
}

main().catch(e => { console.error(e); process.exit(1); });
