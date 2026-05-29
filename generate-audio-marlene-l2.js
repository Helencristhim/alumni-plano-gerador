const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY env variable'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';
const AUDIO_DIR = path.join(BASE_DIR, 'audio/marlene-landucci');

// Only Aula 2 new entries
const audioMap = {
  "Routine": "/audio/marlene-landucci/routine.mp3",
  "Wake up": "/audio/marlene-landucci/wake_up.mp3",
  "Breakfast": "/audio/marlene-landucci/breakfast.mp3",
  "Exercise": "/audio/marlene-landucci/exercise.mp3",
  "Usually": "/audio/marlene-landucci/usually.mp3",
  "Always": "/audio/marlene-landucci/always.mp3",
  "Sometimes": "/audio/marlene-landucci/sometimes.mp3",
  "Schedule": "/audio/marlene-landucci/schedule.mp3",
  "I have a morning routine.": "/audio/marlene-landucci/i_have_a_morning_routine.mp3",
  "I wake up at six in the morning.": "/audio/marlene-landucci/i_wake_up_at_six_in_the_morning.mp3",
  "I have breakfast before work.": "/audio/marlene-landucci/i_have_breakfast_before_work.mp3",
  "I exercise three times a week.": "/audio/marlene-landucci/i_exercise_three_times_a_week.mp3",
  "I usually go to the office at eight.": "/audio/marlene-landucci/i_usually_go_to_the_office_at_eight.mp3",
  "I always drink coffee in the morning.": "/audio/marlene-landucci/i_always_drink_coffee_in_the_morning.mp3",
  "Sometimes I play tennis after work.": "/audio/marlene-landucci/sometimes_i_play_tennis_after_work.mp3",
  "My schedule is very busy.": "/audio/marlene-landucci/my_schedule_is_very_busy.mp3",
  "She always wakes up early.": "/audio/marlene-landucci/she_always_wakes_up_early.mp3",
  "We sometimes have breakfast together.": "/audio/marlene-landucci/we_sometimes_have_breakfast_together.mp3",
  "He usually exercises in the morning.": "/audio/marlene-landucci/he_usually_exercises_in_the_morning.mp3",
  "They never skip breakfast.": "/audio/marlene-landucci/they_never_skip_breakfast.mp3",
  "I usually have coffee and fruit for breakfast.": "/audio/marlene-landucci/i_usually_have_coffee_and_fruit_for_breakfast.mp3",
  "I wake up at six. I always have coffee first.": "/audio/marlene-landucci/i_wake_up_at_six_i_always_have_coffee_first.mp3",
  "I usually check my properties in the morning.": "/audio/marlene-landucci/i_usually_check_my_properties_in_the_morning.mp3",
  "Sometimes I play tennis in the afternoon.": "/audio/marlene-landucci/sometimes_i_play_tennis_in_the_afternoon.mp3",
  "My schedule is always busy, but I love it.": "/audio/marlene-landucci/my_schedule_is_always_busy_but_i_love_it.mp3",
  "I always wake up at six in the morning.": "/audio/marlene-landucci/i_always_wake_up_at_six_in_the_morning.mp3",
  "I usually have breakfast at seven.": "/audio/marlene-landucci/i_usually_have_breakfast_at_seven.mp3",
  "I exercise three times a week. I play tennis.": "/audio/marlene-landucci/i_exercise_three_times_a_week_i_play_tennis.mp3",
  "Hi Lisa! I usually wake up at six.": "/audio/marlene-landucci/hi_lisa_i_usually_wake_up_at_six.mp3",
  "I always have coffee and fruit for breakfast.": "/audio/marlene-landucci/i_always_have_coffee_and_fruit_for_breakfast.mp3",
  "Then I check my properties. My schedule is busy!": "/audio/marlene-landucci/then_i_check_my_properties_my_schedule_is_busy.mp3",
  "Sometimes I play tennis in the afternoon. I love it!": "/audio/marlene-landucci/sometimes_i_play_tennis_in_the_afternoon_i_love_it.mp3",
  "Wow, you are so active! What time do you wake up?": "/audio/marlene-landucci/wow_you_are_so_active_what_time_do_you_wake_up.mp3",
  "That sounds lovely! Do you always have the same breakfast?": "/audio/marlene-landucci/that_sounds_lovely_do_you_always_have_the_same_breakfast.mp3",
  "I understand! I am a teacher. My schedule is busy too.": "/audio/marlene-landucci/i_understand_i_am_a_teacher_my_schedule_is_busy_too.mp3",
  "Tennis is great exercise! I usually go to the gym.": "/audio/marlene-landucci/tennis_is_great_exercise_i_usually_go_to_the_gym.mp3",
  "[lp-listen3]": "/audio/marlene-landucci/lp_listen3_morning_routine.mp3",
  "[lp-listen4]": "/audio/marlene-landucci/lp_listen4_daily_schedule.mp3",
  "I always wake up early.": "/audio/marlene-landucci/i_always_wake_up_early.mp3",
  "I usually have coffee for breakfast.": "/audio/marlene-landucci/i_usually_have_coffee_for_breakfast.mp3",
  "I sometimes play tennis after work.": "/audio/marlene-landucci/i_sometimes_play_tennis_after_work.mp3",
  "I never skip breakfast.": "/audio/marlene-landucci/i_never_skip_breakfast.mp3",
  "What time do you usually wake up?": "/audio/marlene-landucci/what_time_do_you_usually_wake_up.mp3",
  "What do you have for breakfast?": "/audio/marlene-landucci/what_do_you_have_for_breakfast.mp3",
  "Do you exercise every day?": "/audio/marlene-landucci/do_you_exercise_every_day.mp3"
};

// Ellen phrases (Marlene is female - her own lines, survival, speech cards)
const ellenPhrases = new Set([
  "I have a morning routine.",
  "I wake up at six in the morning.",
  "I have breakfast before work.",
  "I exercise three times a week.",
  "I usually go to the office at eight.",
  "I always drink coffee in the morning.",
  "Sometimes I play tennis after work.",
  "My schedule is very busy.",
  "I usually have coffee and fruit for breakfast.",
  "I wake up at six. I always have coffee first.",
  "I usually check my properties in the morning.",
  "Sometimes I play tennis in the afternoon.",
  "My schedule is always busy, but I love it.",
  "I always wake up at six in the morning.",
  "I usually have breakfast at seven.",
  "I exercise three times a week. I play tennis.",
  // Dialogue - Marlene's lines
  "Hi Lisa! I usually wake up at six.",
  "I always have coffee and fruit for breakfast.",
  "Then I check my properties. My schedule is busy!",
  "Sometimes I play tennis in the afternoon. I love it!",
  // Survival phrases
  "I always wake up early.",
  "I usually have coffee for breakfast.",
  "I sometimes play tennis after work.",
  "I never skip breakfast.",
  "What time do you usually wake up?",
  // Speech cards
  "What do you have for breakfast?",
  "Do you exercise every day?",
]);

// Lisa's lines (female character) = Ellen
const lisaPhrases = new Set([
  "Wow, you are so active! What time do you wake up?",
  "That sounds lovely! Do you always have the same breakfast?",
  "I understand! I am a teacher. My schedule is busy too.",
  "Tennis is great exercise! I usually go to the gym.",
]);

let phraseAlternator = false;

function getVoice(text) {
  // Single words (1-2 words) = Ellen (female student)
  const wordCount = text.trim().split(/\s+/).length;
  if (wordCount <= 2) return { id: ELLEN, name: 'Ellen' };

  // Marlene's own phrases = Ellen
  if (ellenPhrases.has(text)) return { id: ELLEN, name: 'Ellen' };

  // Lisa's lines = Ellen (female character)
  if (lisaPhrases.has(text)) return { id: ELLEN, name: 'Ellen' };

  // Listening audio keys
  if (text.startsWith('[lp-')) return { id: ELLEN, name: 'Ellen' };

  // For remaining phrases, alternate Arthur/Ellen
  phraseAlternator = !phraseAlternator;
  return phraseAlternator ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  // For listening keys, generate descriptive content
  let actualText = text;
  if (text === '[lp-listen3]') {
    actualText = "Good morning everyone! Welcome to the morning show. Today we are talking about morning routines. I always wake up at five thirty. First, I have a big breakfast. I usually have eggs, toast, and orange juice. Then I exercise for thirty minutes. I go to the gym three times a week. My schedule is very busy, but I always make time for breakfast. What about you? What is your morning routine?";
  } else if (text === '[lp-listen4]') {
    actualText = "Hi, my name is Carlos. I am from Mexico. Let me tell you about my daily schedule. I wake up at seven. I usually have coffee and a banana for breakfast. Then I go to work at eight thirty. I work in an office. I sometimes have lunch at a restaurant near my office. After work, I usually exercise. I go running three times a week. In the evening, I always cook dinner. My schedule is busy, but I love my routine.";
  }

  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: actualText,
      model_id: 'eleven_monolingual_v1',
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

  const entries = Object.entries(audioMap);
  const total = entries.length;
  let generated = 0;
  let skipped = 0;

  console.log(`\nFound ${total} audioMap entries for marlene-landucci Aula 2\n`);

  for (let i = 0; i < entries.length; i++) {
    const [text, relPath] = entries[i];
    const fullPath = path.join(BASE_DIR, relPath);
    const filename = path.basename(relPath);

    if (fs.existsSync(fullPath)) {
      skipped++;
      console.log(`Skipped: ${filename} (exists)`);
      continue;
    }

    const voice = getVoice(text);
    try {
      const buffer = await generateAudio(text, voice.id);
      fs.writeFileSync(fullPath, buffer);
      generated++;
      console.log(`Generated ${generated}/${total - skipped}: ${filename} (${voice.name})`);
      if (i < entries.length - 1) await delay(500);
    } catch (err) {
      console.error(`FAILED: ${filename} — ${err.message}`);
    }
  }

  console.log(`\n=== SUMMARY ===`);
  console.log(`Total entries: ${total}`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped (existing): ${skipped}`);
  console.log(`Failed: ${total - generated - skipped}`);
}

main();
