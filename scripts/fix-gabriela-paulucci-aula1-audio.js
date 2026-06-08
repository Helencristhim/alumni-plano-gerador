const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const RILEY_ID = 'hA4zGnmTwX2NQiTRMt7o'; // Female neutral (replaces Ellen)
const ASH_ID = 'VU16byTywsWv5JpI8rbc';   // Male neutral (replaces Arthur)

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

const FIXES = [
  // 1. "Live" pronunciation — force /lɪv/ (verb "to live/reside") via contextual text
  // Using "to live" context to ensure verb pronunciation, then trim mentally
  // ElevenLabs reads context, so "Live. To live in a city." guides pronunciation
  { text: "Live.", outputName: "live.mp3", voice: "ash", note: "Pronunciation fix: /lɪv/ not /laɪv/" },

  // 2. "I am 33 years old." — regenerate with female voice (was Arthur, should be Riley)
  { text: "I am 33 years old.", outputName: "i_am_33_years_old.mp3", voice: "riley", note: "Voice fix: female for Gabriela" },

  // 3. New listening audio — Lucas introducing himself (personal info, matches lesson theme)
  { text: "Hi! My name is Lucas. I am 25 years old. I am from Rio de Janeiro. I live in São Paulo now. It is a very big city. I work at a hospital. I am a nurse.", outputName: "listening1_lucas_intro.mp3", voice: "ash", note: "New listening: personal intro replaces airport announcement" },
];

async function generateAudio(text, voiceId, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: {
      'xi-api-key': API_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_turbo_v2_5',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 },
    }),
  });

  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`ElevenLabs error (${resp.status}): ${err}`);
  }

  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  if (!API_KEY) {
    console.error('ELEVENLABS_API_KEY not set. Run: source ~/.zshrc');
    process.exit(1);
  }

  console.log(`\nFixing ${FIXES.length} audio files for Gabriela Paulucci Aula 1...\n`);

  for (const fix of FIXES) {
    const outputPath = path.join(OUTPUT_DIR, fix.outputName);
    const voiceId = fix.voice === 'riley' ? RILEY_ID : ASH_ID;
    const existsAlready = fs.existsSync(outputPath);

    console.log(`  ${fix.note}`);
    console.log(`    File: ${fix.outputName} (${existsAlready ? 'OVERWRITING' : 'NEW'})`);

    // Backup existing file before overwriting
    if (existsAlready) {
      const backupPath = outputPath.replace('.mp3', '_backup.mp3');
      fs.copyFileSync(outputPath, backupPath);
      console.log(`    Backup: ${path.basename(backupPath)}`);
    }

    try {
      const bytes = await generateAudio(fix.text, voiceId, outputPath);
      console.log(`    OK [${fix.voice}]: ${(bytes / 1024).toFixed(1)}KB\n`);
    } catch (err) {
      console.error(`    FAILED: ${err.message}\n`);
    }

    // Rate limit
    await new Promise(r => setTimeout(r, 600));
  }

  console.log('Done! Verify the audio files before deploying.');
}

main();
