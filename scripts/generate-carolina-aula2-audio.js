const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carolina-paludetto-rodrigues');

// Voice rules:
// - Carolina is FEMALE → her lines/exercises = ELLEN
// - Lucas is MALE → his lines = ARTHUR
// - Single vocab words → ELLEN (student gender)
// - General phrases → ALTERNATE Arthur/Ellen
// - Dialogue lines → by character gender

const PHRASES = [
  // ===== Vocab words (Carolina is female → ELLEN) =====
  { text: "Routine", file: "aula2_routine.mp3", voice: ELLEN },
  { text: "Schedule", file: "aula2_schedule.mp3", voice: ELLEN },
  { text: "Wake up", file: "aula2_wake_up.mp3", voice: ELLEN },
  { text: "Commute", file: "aula2_commute.mp3", voice: ELLEN },
  { text: "Practice", file: "aula2_practice.mp3", voice: ELLEN },
  { text: "Homework", file: "aula2_homework.mp3", voice: ELLEN },
  { text: "Relax", file: "aula2_relax.mp3", voice: ELLEN },
  { text: "Bedtime", file: "aula2_bedtime.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "I have a busy routine on school days.", file: "aula2_i_have_a_busy_routine.mp3", voice: ELLEN },
  { text: "My schedule is full every Monday.", file: "aula2_my_schedule_is_full.mp3", voice: ARTHUR },
  { text: "I wake up at seven every morning.", file: "aula2_i_wake_up_at_seven.mp3", voice: ELLEN },
  { text: "My commute to school takes thirty minutes.", file: "aula2_my_commute_to_school.mp3", voice: ARTHUR },
  { text: "I practice handball three times a week.", file: "aula2_i_practice_handball.mp3", voice: ELLEN },
  { text: "I always do my homework before dinner.", file: "aula2_i_always_do_my_homework.mp3", voice: ARTHUR },
  { text: "I relax by writing stories in the evening.", file: "aula2_i_relax_by_writing.mp3", voice: ELLEN },
  { text: "My bedtime is ten o'clock on school nights.", file: "aula2_my_bedtime_is_ten.mp3", voice: ARTHUR },

  // ===== Grammar examples (alternate) =====
  { text: "I always wake up at seven.", file: "aula2_i_always_wake_up.mp3", voice: ELLEN },
  { text: "She usually has breakfast at seven thirty.", file: "aula2_she_usually_has_breakfast.mp3", voice: ARTHUR },
  { text: "We never skip homework.", file: "aula2_we_never_skip_homework.mp3", voice: ELLEN },
  { text: "Do you sometimes practice on weekends?", file: "aula2_do_you_sometimes_practice.mp3", voice: ARTHUR },

  // ===== Speech practice (Carolina = ELLEN) =====
  { text: "I usually wake up at seven and have breakfast with my family.", file: "aula2_speech_1.mp3", voice: ELLEN },
  { text: "My commute to school takes about thirty minutes by bus.", file: "aula2_speech_2.mp3", voice: ELLEN },
  { text: "I always do my homework before dinner.", file: "aula2_speech_3.mp3", voice: ELLEN },
  { text: "I sometimes relax by writing stories in the evening.", file: "aula2_speech_4.mp3", voice: ELLEN },
  { text: "My bedtime is usually ten o'clock on school nights.", file: "aula2_speech_5.mp3", voice: ELLEN },

  // ===== Survival card (alternate) =====
  { text: "What time do you usually wake up?", file: "aula2_survival_1.mp3", voice: ARTHUR },
  { text: "I always have breakfast before school.", file: "aula2_survival_2.mp3", voice: ELLEN },
  { text: "How long is your commute?", file: "aula2_survival_3.mp3", voice: ARTHUR },
  { text: "I sometimes practice sports after school.", file: "aula2_survival_4.mp3", voice: ELLEN },
  { text: "My bedtime is usually at ten.", file: "aula2_survival_5.mp3", voice: ARTHUR },

  // ===== Dialogue — Lucas (male = ARTHUR), Carolina (female = ELLEN) =====
  { text: "Hey Carolina! What time do you usually wake up on school days?", file: "aula2_dialogue_lucas_1.mp3", voice: ARTHUR },
  { text: "I always wake up at seven. What about you, Lucas?", file: "aula2_dialogue_carolina_1.mp3", voice: ELLEN },
  { text: "I usually wake up at six thirty. Do you have a long commute?", file: "aula2_dialogue_lucas_2.mp3", voice: ARTHUR },
  { text: "My commute takes about thirty minutes by bus. It is not bad.", file: "aula2_dialogue_carolina_2.mp3", voice: ELLEN },
  { text: "Do you practice handball every day?", file: "aula2_dialogue_lucas_3.mp3", voice: ARTHUR },
  { text: "No, I practice three times a week. I sometimes relax and write stories.", file: "aula2_dialogue_carolina_3.mp3", voice: ELLEN },
  { text: "That sounds like a busy schedule! What is your bedtime?", file: "aula2_dialogue_lucas_4.mp3", voice: ARTHUR },
  { text: "My bedtime is usually ten o'clock. I never stay up late on school nights.", file: "aula2_dialogue_carolina_4.mp3", voice: ELLEN },

  // ===== Dialogue duplicates for IN CLASS (separate slide) =====
  { text: "I usually wake up at six thirty. Do you have a long commute?", file: "aula2_dialogue_lucas_2b.mp3", voice: ARTHUR },
  { text: "My commute takes about thirty minutes by bus. It is not bad.", file: "aula2_dialogue_carolina_2b.mp3", voice: ELLEN },
  { text: "Do you practice handball every day?", file: "aula2_dialogue_lucas_3b.mp3", voice: ARTHUR },
  { text: "No, I practice three times a week. I sometimes relax and write stories.", file: "aula2_dialogue_carolina_3b.mp3", voice: ELLEN },
  { text: "That sounds like a busy schedule! What is your bedtime?", file: "aula2_dialogue_lucas_4b.mp3", voice: ARTHUR },

  // ===== Ordering exercise =====
  { text: "I wake up at seven. I have breakfast with my family. I commute to school by bus. I check my schedule for the day. I get to school and start my classes.", file: "aula2_order_morning_routine.mp3", voice: ELLEN },

  // ===== IN CLASS grammar practice sentences (alternate) =====
  { text: "Carolina always wakes up at seven.", file: "aula2_carolina_always_wakes_up.mp3", voice: ARTHUR },
  { text: "She usually has breakfast before school.", file: "aula2_she_usually_has_breakfast_before.mp3", voice: ELLEN },
  { text: "I never skip my homework.", file: "aula2_i_never_skip_homework.mp3", voice: ARTHUR },
  { text: "We often practice after school.", file: "aula2_we_often_practice.mp3", voice: ELLEN },
  { text: "She is usually tired after handball.", file: "aula2_she_is_usually_tired.mp3", voice: ARTHUR },

  // ===== Fill-in-the-blank phrases (alternate) =====
  { text: "I always eat breakfast at seven thirty.", file: "aula2_fill_1.mp3", voice: ELLEN },
  { text: "She never watches TV before homework.", file: "aula2_fill_2.mp3", voice: ARTHUR },
  { text: "We usually walk to school together.", file: "aula2_fill_3.mp3", voice: ELLEN },
  { text: "Do you sometimes read before bedtime?", file: "aula2_fill_4.mp3", voice: ARTHUR },
  { text: "He often plays soccer after school.", file: "aula2_fill_5.mp3", voice: ELLEN },

  // ===== Listening 1 — Maya (female = ELLEN) =====
  { text: "Hi, I am Maya. I am fourteen years old and I live in New York.", file: "aula2_listening1_maya.mp3", voice: ELLEN },
  { text: "I always wake up at six thirty. My commute to school is short. I usually walk. After school, I sometimes practice volleyball. I always do my homework before dinner. My bedtime is nine thirty on school nights.", file: "aula2_listening1_full.mp3", voice: ELLEN },

  // ===== Listening 2 — Tom (male = ARTHUR) =====
  { text: "Good morning! I am Tom, and this is a typical school day for me.", file: "aula2_listening2_tom.mp3", voice: ARTHUR },
  { text: "I usually wake up at seven fifteen. I never skip breakfast. My commute takes twenty minutes by bike. I often practice basketball after school. I sometimes relax by playing video games. My bedtime is ten o'clock.", file: "aula2_listening2_full.mp3", voice: ARTHUR },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    }),
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
  const unique = PHRASES.filter(p => {
    const k = p.file.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' audio files for Carolina Aula 2...');
  let generated = 0;
  let skipped = 0;

  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('  SKIP (exists): ' + p.file);
      skipped++;
      continue;
    }
    try {
      const size = await gen(p.text, p.voice, outPath);
      generated++;
      console.log('  OK: ' + p.file + ' (' + Math.round(size / 1024) + ' KB)');
      // Rate limit: wait 500ms between calls
      await new Promise(r => setTimeout(r, 500));
    } catch (e) {
      console.error('  FAIL: ' + p.file + ' - ' + e.message);
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + unique.length);
}

main();
