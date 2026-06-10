#!/usr/bin/env node
/**
 * Aula 6 — Gabriela Paulucci — "I Like, I Don't Like" (like/love/hate + -ing)
 * ElevenLabs audio generator. Model: eleven_multilingual_v2 (REGRA C1).
 * Voices (REGRA 35/C1): ellen=Gabriela (aluna), rachel=Sarah/3rd female, arthur=male.
 * Never overwrites existing MP3 (REGRA C9).
 *
 * Key is read from the canonical app .env.local (per task instruction):
 *   /home/dan/dev/work/better/alumni-plano-gerador/.env.local
 * Override with ELEVENLABS_API_KEY env var if set.
 */
const fs = require('fs');
const path = require('path');

const ENV_PATH = '/home/dan/dev/work/better/alumni-plano-gerador/.env.local';
function loadKey() {
  if (process.env.ELEVENLABS_API_KEY) return process.env.ELEVENLABS_API_KEY;
  try {
    const raw = fs.readFileSync(ENV_PATH, 'utf8');
    const m = raw.match(/ELEVENLABS_API_KEY\s*=\s*(.+)/);
    if (m) return m[1].trim();
  } catch (e) {}
  return null;
}
const API_KEY = loadKey();
if (!API_KEY) { console.error('No ELEVENLABS_API_KEY found.'); process.exit(1); }

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = {
  arthur: 'sfJopaWaOtauCD3HKX6Q',
  ellen:  'BIvP0GN1cAtSRTxNHnWS',
  josh:   'TxGEqnHWrfWFTfGW9XjX',
  rachel: '21m00Tcm4TlvDq8ikWAM',
  domi:   'AZnzlk1XvdvUeBnXmlld',
  bella:  'EXAVITQu4vr4xnSDxMaL'
};
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

// { text: spoken text -> ElevenLabs, file: output filename, voice: roster key }
const phrases = [
  // --- Vocab single words (Pre-class) — ellen (aluna) ---
  { text: 'Cooking', file: 'cooking.mp3', voice: 'ellen' },
  { text: 'Reading', file: 'reading.mp3', voice: 'ellen' },
  { text: 'Dancing', file: 'dancing.mp3', voice: 'ellen' },
  { text: 'Running', file: 'running.mp3', voice: 'ellen' },
  { text: 'Traveling', file: 'traveling.mp3', voice: 'ellen' },
  { text: 'Listening to music', file: 'listening_to_music.mp3', voice: 'ellen' },
  { text: 'Watching series', file: 'watching_series.mp3', voice: 'ellen' },
  { text: 'Swimming', file: 'swimming.mp3', voice: 'ellen' },

  // --- Example / grammar / drill sentences — ellen (aluna protagonist) ---
  { text: 'I love cooking.', file: 'aula6_i_love_cooking.mp3', voice: 'ellen' },
  { text: 'I like reading.', file: 'aula6_i_like_reading.mp3', voice: 'ellen' },
  { text: 'I love dancing.', file: 'aula6_i_love_dancing.mp3', voice: 'ellen' },
  { text: "I don't like running.", file: 'aula6_i_dont_like_running.mp3', voice: 'ellen' },
  { text: 'I like traveling.', file: 'aula6_i_like_traveling.mp3', voice: 'ellen' },
  { text: 'I love listening to music.', file: 'aula6_i_love_listening_to_music.mp3', voice: 'ellen' },
  { text: 'I like watching series.', file: 'aula6_i_like_watching_series.mp3', voice: 'ellen' },
  { text: "I don't like swimming.", file: 'aula6_i_dont_like_swimming.mp3', voice: 'ellen' },
  { text: 'I like cooking.', file: 'aula6_i_like_cooking.mp3', voice: 'ellen' },
  { text: 'She likes dancing.', file: 'aula6_she_likes_dancing.mp3', voice: 'ellen' },
  { text: 'He loves swimming.', file: 'aula6_he_loves_swimming.mp3', voice: 'ellen' },
  { text: 'We love traveling.', file: 'aula6_we_love_traveling.mp3', voice: 'ellen' },
  { text: 'Do you like reading?', file: 'aula6_do_you_like_reading.mp3', voice: 'ellen' },
  { text: 'I hate cleaning.', file: 'aula6_i_hate_cleaning.mp3', voice: 'ellen' },

  // --- Dialogue: Sarah (rachel) <-> Gabriela (ellen) ---
  { text: 'Hi Gabriela! What do you like doing in your free time?', file: 'aula6_dia_1.mp3', voice: 'rachel' },
  { text: 'I love cooking. I cook every weekend.', file: 'aula6_dia_2.mp3', voice: 'ellen' },
  { text: 'That sounds nice! Do you like reading too?', file: 'aula6_dia_3.mp3', voice: 'rachel' },
  { text: "Yes, I like reading. But I don't like running.", file: 'aula6_dia_4.mp3', voice: 'ellen' },
  { text: "Really? Why don't you like running?", file: 'aula6_dia_5.mp3', voice: 'rachel' },
  { text: 'It is too hard for me! I prefer dancing.', file: 'aula6_dia_6.mp3', voice: 'ellen' },
  { text: 'I love dancing too! What music do you like?', file: 'aula6_dia_7.mp3', voice: 'rachel' },
  { text: 'I love listening to Brazilian music. And you?', file: 'aula6_dia_8.mp3', voice: 'ellen' },
  { text: 'I like watching series. But I hate cleaning the house!', file: 'aula6_dia_9.mp3', voice: 'rachel' },
  { text: 'Me too! Cleaning is boring.', file: 'aula6_dia_10.mp3', voice: 'ellen' },

  // --- Listening 1 (full monologue, single MP3) — ellen ---
  { text: "Hello! Let me tell you about my free time. On weekends, I love cooking and dancing. I like reading books at night. I don't like running, but I love walking in the park. I hate cleaning, but I do it on Sundays.", file: 'aula6_listening1_free_time.mp3', voice: 'ellen' },

  // --- Listening 2 (3 distinct people / distinct voices) ---
  { text: "I love playing soccer. I don't like swimming.", file: 'aula6_listening2_p1.mp3', voice: 'arthur' },
  { text: 'I like painting. I love listening to music.', file: 'aula6_listening2_p2.mp3', voice: 'ellen' },
  { text: 'I hate cooking, but I love traveling.', file: 'aula6_listening2_p3.mp3', voice: 'rachel' },

  // --- Preferences kit recap — ellen ---
  { text: 'I love cooking and dancing.', file: 'aula6_kit_love.mp3', voice: 'ellen' },
  { text: 'I like reading at night.', file: 'aula6_kit_like.mp3', voice: 'ellen' },
  { text: 'Do you like watching series?', file: 'aula6_kit_question.mp3', voice: 'ellen' },
  { text: 'What do you like doing?', file: 'aula6_kit_ask.mp3', voice: 'ellen' },

  // --- Pre-class extras: ordering + reflection model — ellen ---
  { text: "I love cooking. I like reading. I don't like running. I hate cleaning.", file: 'aula6_order.mp3', voice: 'ellen' },
  { text: "My favorite hobby is cooking. I love cooking on weekends. I don't like running.", file: 'aula6_reflection.mp3', voice: 'ellen' }
];

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

async function generateAudio(text, filename, voiceKey) {
  const filePath = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(filePath)) return { skipped: true };
  const voiceId = VOICES[voiceKey];
  if (!voiceId) throw new Error('Unknown voice: ' + voiceKey);
  const res = await fetch(`${API_URL}/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true }
    })
  });
  if (!res.ok) {
    const body = await res.text();
    throw new Error(`${res.status} for "${text.substring(0, 40)}..." -> ${body.substring(0, 120)}`);
  }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(filePath, buf);
  return { skipped: false };
}

(async () => {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  let gen = 0, skip = 0, err = 0;
  for (const p of phrases) {
    try {
      const r = await generateAudio(p.text, p.file, p.voice);
      if (r.skipped) { skip++; process.stdout.write('.'); }
      else { gen++; process.stdout.write('+'); await sleep(350); }
    } catch (e) {
      err++; console.error('\n[ERROR] ' + p.file + ': ' + e.message);
    }
  }
  console.log(`\nDone. generated=${gen} skipped=${skip} errors=${err} total=${phrases.length}`);
  process.exit(err ? 2 : 0);
})();
