const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY env variable'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const AUDIO_DIR = '/Users/helenmendes/alumni-plano-gerador/public/audio/marlene-landucci';

// =============================================================
// IN CLASS Aula 2 — Audio fixes
// =============================================================
// 1. Listening 1: Re-gerar com 2 vozes (presenter=Arthur, Anna=Ellen)
//    e pausas entre frases (usando <break> SSML)
// 2. Listening 2: Re-gerar com Arthur (Marco, male) com pausas
// 3. Lisa dialogue lines: Re-gerar com Arthur (para diferenciar de Marlene/Ellen)
//    Nota: Lisa é feminina, mas precisamos diferenciar. Usamos Arthur com stability alta.
//    ALTERNATIVA: mantemos Ellen para Lisa conforme regra de gênero,
//    mas re-geramos com settings diferentes (stability 0.7) para soar diferente.
// =============================================================

const audioEntries = [
  // Listening 1 — presenter (Arthur) + Anna (Ellen), with pauses via longer text spacing
  {
    text: "Good morning! Today we talk to people about their daily routines. ... First, we have Anna from Germany. ... Anna, what is your daily routine? ... Well, I always wake up at six thirty. ... I have breakfast at seven. ... I usually have coffee and toast. ... Then I go to work at eight. ... I work in an office. ... I usually have lunch at twelve thirty. ... After work, I sometimes go to the gym. ... I always cook dinner at home. ... I never eat out on weekdays.",
    file: "lp_listen_l2_1_daily_routine.mp3",
    voice: ELLEN,
    stability: 0.45,
    similarity: 0.7
  },
  // Listening 2 — Marco (Arthur), male, with pauses
  {
    text: "My name is Marco. I am from Italy. I live in Rome. ... My morning schedule is very busy. ... I wake up at five forty-five every day. ... I always have a big Italian breakfast. Coffee, bread, and cheese. ... Then I exercise for twenty minutes. I usually run in the park near my house. ... After that, I go to work. I am a tour guide. ... I sometimes start work at eight, sometimes at nine. ... My schedule changes every day, but I always keep my morning routine the same.",
    file: "lp_listen_l2_2_morning_schedule.mp3",
    voice: ARTHUR,
    stability: 0.45,
    similarity: 0.7
  },
  // Lisa dialogue lines — re-generate with different stability for vocal distinction
  {
    text: "Marlene! What a surprise! How are you?",
    file: "marlene_what_a_surprise_how_are_you.mp3",
    voice: ARTHUR,
    stability: 0.5,
    similarity: 0.75
  },
  {
    text: "Me too! What is your morning routine here?",
    file: "me_too_what_is_your_morning_routine_here.mp3",
    voice: ARTHUR,
    stability: 0.5,
    similarity: 0.75
  },
  {
    text: "That sounds lovely! I sometimes skip breakfast and go straight to a cafe.",
    file: "that_sounds_lovely_i_sometimes_skip_breakfast.mp3",
    voice: ARTHUR,
    stability: 0.5,
    similarity: 0.75
  },
];

function generateAudio(text, voiceId, stability = 0.5, similarity = 0.75) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability, similarity_boost: similarity }
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

  console.log(`\nRe-generating ${audioEntries.length} IN CLASS audio files (Aula 2 fixes)\n`);

  for (let i = 0; i < audioEntries.length; i++) {
    const entry = audioEntries[i];
    const fullPath = path.join(AUDIO_DIR, entry.file);
    const voiceName = entry.voice === ELLEN ? 'Ellen' : 'Arthur';
    const existed = fs.existsSync(fullPath);

    try {
      const buffer = await generateAudio(entry.text, entry.voice, entry.stability || 0.5, entry.similarity || 0.75);
      fs.writeFileSync(fullPath, buffer);
      generated++;
      console.log(`${generated}/${audioEntries.length} ${existed ? 'REPLACED' : 'CREATED'}: ${entry.file} (${voiceName})`);
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
