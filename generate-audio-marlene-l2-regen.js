const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY env variable'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';
const AUDIO_DIR = path.join(BASE_DIR, 'audio/marlene-landucci');

// =============================================================
// Audios para RE-GERAR (sobrescrever) — problemas reportados
// =============================================================
// Stage 1.1 vocab words: ruído, rápido, cortado, voz errada
// Marlene = aluna feminina → palavras soltas = Ellen
// Stage 1.5 fill-in-the-blank: alternância de vozes correta
//   1. I wake up... (I) → Ellen (aluna)
//   2. She always... (She) → Arthur (alternância)
//   3. We usually... (We) → Ellen
//   4. He sometimes... (He) → Arthur
//   5. They never... (They) → Ellen
//   6. My schedule... (My/I) → Arthur (alternância)
// =============================================================

const audioEntries = [
  // Stage 1.1 - Vocab words com problemas (TODOS re-gerar com Ellen = voz da aluna)
  { text: "Wake up", file: "wake_up.mp3", voice: ELLEN },           // ruído no final
  { text: "Breakfast", file: "breakfast.mp3", voice: ELLEN },        // rápido
  { text: "Exercise", file: "exercise.mp3", voice: ELLEN },          // rápido e cortado
  { text: "Usually", file: "usually.mp3", voice: ELLEN },            // voz errada
  { text: "Always", file: "always.mp3", voice: ELLEN },              // rápido e cortado
  { text: "Sometimes", file: "sometimes.mp3", voice: ELLEN },        // muito rápido

  // Stage 1.5 - Fill-in-the-blank (corrigir alternância de vozes)
  { text: "I wake up at six in the morning.", file: "i_wake_up_at_six_in_the_morning.mp3", voice: ELLEN },
  { text: "She always has breakfast at seven.", file: "she_always_has_breakfast_at_seven.mp3", voice: ARTHUR },
  { text: "We usually exercise in the morning.", file: "we_usually_exercise_in_the_morning.mp3", voice: ELLEN },
  { text: "He sometimes travels for work.", file: "he_sometimes_travels_for_work.mp3", voice: ARTHUR },
  { text: "They never skip breakfast.", file: "they_never_skip_breakfast.mp3", voice: ELLEN },
  { text: "My schedule is very busy.", file: "my_schedule_is_very_busy.mp3", voice: ARTHUR },
];

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY
      }
    };

    const req = https.request(options, res => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', c => body += c);
        res.on('end', () => reject(new Error(`API ${res.statusCode}: ${body}`)));
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

async function main() {
  if (!fs.existsSync(AUDIO_DIR)) fs.mkdirSync(AUDIO_DIR, { recursive: true });

  let generated = 0;

  console.log(`\nRe-generating ${audioEntries.length} audio files for marlene-landucci (Aula 2 fixes)\n`);
  console.log('NOTE: Files will be OVERWRITTEN if they already exist.\n');

  for (let i = 0; i < audioEntries.length; i++) {
    const entry = audioEntries[i];
    const fullPath = path.join(AUDIO_DIR, entry.file);
    const voiceName = entry.voice === ELLEN ? 'Ellen' : 'Arthur';
    const existed = fs.existsSync(fullPath);

    try {
      const buffer = await generateAudio(entry.text, entry.voice);
      fs.writeFileSync(fullPath, buffer);
      generated++;
      console.log(`${generated}/${audioEntries.length} ${existed ? 'REPLACED' : 'CREATED'}: ${entry.file} (${voiceName}) — "${entry.text}"`);
      if (i < audioEntries.length - 1) await delay(500);
    } catch (err) {
      console.error(`FAILED: ${entry.file} — ${err.message}`);
    }
  }

  console.log(`\n=== SUMMARY ===`);
  console.log(`Total: ${audioEntries.length}`);
  console.log(`Generated: ${generated}`);
  console.log(`Failed: ${audioEntries.length - generated}`);
}

main();
