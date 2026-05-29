const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'luiz-bressane');

// Voice assignment rules:
// - Single words (1-2 words) = ALWAYS Arthur
// - Phrases (3+ words) = ALTERNATE Arthur/Ellen, starting with Ellen
// - Dialogue: Mark context = Arthur, Luiz context = Ellen
// - [order-l1] = Arthur

const PHRASES = [
  // === DISCUSSION PHRASES (3+ words — alternate starting Ellen) ===
  { text: "Could you elaborate on that point?", voice: ELLEN },
  { text: "I see what you mean, but I would argue that...", voice: ARTHUR },
  { text: "If I understand correctly, you are saying that...", voice: ELLEN },
  { text: "That raises an interesting question about...", voice: ARTHUR },
  { text: "Let me put it another way.", voice: ELLEN },

  // === VOCAB WORDS (1-2 words — ALWAYS Arthur) ===
  { text: "Acquittal", voice: ARTHUR },
  { text: "Burden of proof", voice: ARTHUR },
  { text: "Cross-examination", voice: ARTHUR },
  { text: "Due process", voice: ARTHUR },
  { text: "Jurisdiction", voice: ARTHUR },
  { text: "Litigation", voice: ARTHUR },
  { text: "Overturn", voice: ARTHUR },
  { text: "Plea bargain", voice: ARTHUR },
  { text: "Precedent", voice: ARTHUR },
  { text: "Ruling", voice: ARTHUR },
  { text: "Testimony", voice: ARTHUR },
  { text: "Verdict", voice: ARTHUR },
  { text: "Advocate", voice: ARTHUR },

  // === VOCAB EXAMPLE SENTENCES (3+ words — alternate starting Ellen) ===
  { text: "The jury returned a verdict of acquittal after deliberating for three hours.", voice: ELLEN },
  { text: "The burden of proof lies with the prosecution in criminal cases.", voice: ARTHUR },
  { text: "During cross-examination, the defense attorney challenged the witness.", voice: ELLEN },
  { text: "Every defendant has a right to due process under the constitution.", voice: ARTHUR },
  { text: "The court ruled that it did not have jurisdiction over the case.", voice: ELLEN },
  { text: "Complex litigation can take years to resolve in the federal courts.", voice: ARTHUR },
  { text: "The appeals court decided to overturn the original ruling.", voice: ELLEN },
  { text: "The defendant accepted a plea bargain to avoid a lengthy trial.", voice: ARTHUR },
  { text: "This case will set an important precedent for future rulings.", voice: ELLEN },
  { text: "The judge issued a ruling that surprised both parties.", voice: ARTHUR },
  { text: "The witness gave compelling testimony during the hearing.", voice: ELLEN },
  { text: "The verdict was announced after five days of deliberation.", voice: ARTHUR },
  { text: "As a public defender, I advocate for those who cannot afford representation.", voice: ELLEN },

  // === GRAMMAR PRACTICE SENTENCES (3+ words — alternate starting Arthur) ===
  { text: "I have been working as a public defender for over twenty years.", voice: ARTHUR },
  { text: "The defense has been preparing cross-examination questions all week.", voice: ELLEN },
  { text: "The prosecution has presented its testimony, and now it is the defense's turn.", voice: ARTHUR },
  { text: "We have been reviewing the precedent for this type of case since Monday.", voice: ELLEN },
  { text: "The court has already issued its ruling on the matter.", voice: ARTHUR },
  { text: "I have handled over three hundred cases involving due process violations.", voice: ELLEN },
  { text: "The jury has been deliberating since yesterday morning.", voice: ARTHUR },
  { text: "She has testified in court before, but never in a homicide case.", voice: ELLEN },
  { text: "The appeals court has overturned three verdicts this month.", voice: ARTHUR },
  { text: "They have been negotiating a plea bargain for the past two weeks.", voice: ELLEN },
  { text: "I have advocated for defendants' rights throughout my entire career.", voice: ARTHUR },
  { text: "The prosecution has not yet met the burden of proof.", voice: ELLEN },
  { text: "I have been working on this case for three months.", voice: ARTHUR },
  { text: "The defense has filed a motion to overturn the ruling.", voice: ELLEN },
  { text: "We have reviewed the testimony, but we have not found any inconsistencies.", voice: ARTHUR },
  { text: "The judge has been considering the jurisdiction issue for weeks.", voice: ELLEN },

  // === DIALOGUE — Mark (male, American attorney) = Arthur, Luiz (male, Brazilian defender) = Ellen ===
  { text: "Good afternoon. Welcome to the International Legal Symposium.", voice: ARTHUR },
  { text: "I am Mark Thompson, a criminal defense attorney from Washington, D.C.", voice: ARTHUR },
  { text: "Nice to meet you. I am Luiz Bressane, a public defender from Sao Paulo.", voice: ELLEN },
  { text: "How long have you been practicing criminal law?", voice: ARTHUR },
  { text: "I have been working in criminal defense for over twenty years now.", voice: ELLEN },
  { text: "That is impressive. Have you handled many jury trials?", voice: ARTHUR },
  { text: "Yes, I have handled hundreds of cases, including complex homicide trials.", voice: ELLEN },
  { text: "In the United States, we have been seeing a shift toward plea bargains.", voice: ARTHUR },
  { text: "That is interesting. In Brazil, we have been debating plea bargains as well.", voice: ELLEN },
  { text: "Have you ever had a case where the verdict was overturned on appeal?", voice: ARTHUR },
  { text: "Yes, I have. The appeals court overturned a ruling last year due to a due process violation.", voice: ELLEN },
  { text: "That must have been a significant precedent.", voice: ARTHUR },
  { text: "It was. It has changed how we approach cross-examination in similar cases.", voice: ELLEN },
  { text: "I have been meaning to ask — how does the burden of proof work in Brazilian courts?", voice: ARTHUR },
  { text: "It works similarly. The prosecution bears the burden of proof beyond a reasonable doubt.", voice: ELLEN },
  { text: "This has been a fascinating conversation. I have learned a great deal.", voice: ARTHUR },
  { text: "Likewise. I have been wanting to connect with American attorneys for some time.", voice: ELLEN },

  // === LISTENING 1 — Luiz symposium speech (long passage, Arthur) ===
  { text: "My name is Luiz Bressane. I have been working as a public defender in Sao Paulo for over twenty years. Throughout my career, I have handled hundreds of criminal cases, including complex homicide trials before jury courts. Recently, I have been focusing on cases involving due process violations and precedent-setting rulings. I have also been advocating for reforms in the plea bargain system in Brazil. The burden of proof in Brazilian criminal courts works similarly to the American system. I have been attending international legal symposiums to exchange ideas with colleagues from around the world.", voice: ARTHUR, filename: "listening1_luiz_symposium_speech" },

  // === LISTENING 2 — Sarah Chen prosecutor (long passage, Ellen) ===
  { text: "I am Sarah Chen, a federal prosecutor based in New York. I have been working in white-collar crime for the past fifteen years. Over the course of my career, I have prosecuted cases involving corporate fraud, insider trading, and money laundering. One thing I have noticed is that cross-examination techniques have evolved significantly. We have been using more technology in the courtroom, including digital evidence presentation. The burden of proof remains the cornerstone of our justice system. I have recently been involved in a landmark case that has set a new precedent for how we handle digital testimony. The verdict in that case has changed how prosecutors approach similar litigation.", voice: ELLEN, filename: "listening2_sarah_chen_prosecutor" },

  // === IN CLASS PRACTICE SENTENCES (alternate) ===
  { text: "The defense attorney has been preparing the cross-examination all week.", voice: ARTHUR },
  { text: "The prosecution has already presented its closing argument.", voice: ELLEN },
  { text: "I have worked on this type of case before.", voice: ARTHUR },
  { text: "They have been negotiating a settlement since last month.", voice: ELLEN },

  // === SURVIVAL IC PHRASES (alternate) ===
  { text: "I have been practicing law for over twenty years.", voice: ARTHUR },
  { text: "The prosecution has not met the burden of proof in this case.", voice: ELLEN },
  { text: "We have been reviewing the testimony for inconsistencies.", voice: ARTHUR },
  { text: "The court has set an important precedent with this ruling.", voice: ELLEN },
  { text: "I would argue that the evidence does not support the verdict.", voice: ARTHUR },

  // === ORDER EXERCISE ===
  { text: "[order-l1]", voice: ARTHUR, filename: "order_l1_symposium_intro" },
];

function toFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 60);
}

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
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

  console.log('Generating ' + unique.length + ' audio files for Luiz Bressane B2...');
  let generated = 0;
  let skipped = 0;
  let failed = 0;

  for (const p of unique) {
    const fname = (p.filename || toFilename(p.text)) + '.mp3';
    const outPath = path.join(DIR, fname);
    const voiceName = p.voice === ELLEN ? 'Ellen' : 'Arthur';
    const truncated = p.text.length > 50 ? p.text.substring(0, 50) + '...' : p.text;

    if (fs.existsSync(outPath)) {
      console.log('SKIP [' + voiceName + ']: "' + truncated + '" → ' + fname);
      skipped++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK   [' + voiceName + ']: "' + truncated + '" → ' + fname + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) {
        console.error('FAIL [' + voiceName + ']: "' + truncated + '" → ' + e.message);
        failed++;
      }
    }
    audioMap[p.text] = '/audio/luiz-bressane/' + fname;
  }

  fs.writeFileSync(path.join(DIR, 'audioMap-b2.json'), JSON.stringify(audioMap, null, 2));
  console.log('\n--- Summary ---');
  console.log('Total:     ' + unique.length);
  console.log('Generated: ' + generated);
  console.log('Skipped:   ' + skipped);
  console.log('Failed:    ' + failed);
  console.log('audioMap saved to: ' + path.join(DIR, 'audioMap-b2.json'));
}

main().catch(e => { console.error(e); process.exit(1); });
