const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

// Missing IN CLASS dialogue MP3s for aulas 2-5
// Dialogue: Teacher (David) = Arthur, Gabriela = Ellen
// Alternation for non-dialogue: 3+ words alternate Arthur/Ellen

const PHRASES = [
  // === AULA 2 — Dialogue: David (Arthur) + Gabriela (Ellen) ===
  { text: "Good morning, Gabriela! How are you today?", voice: "arthur", filename: "aula2_good_morning_gabriela.mp3" },
  { text: "Do you remember your 5 sentences from Lesson 1?", voice: "arthur", filename: "aula2_do_you_remember.mp3" },
  { text: "Hi Gabriela! Look at your desk. What do you see?", voice: "arthur", filename: "aula2_hi_gabriela_look_at_desk.mp3" },
  { text: "Good! And what is that over there?", voice: "arthur", filename: "aula2_good_and_what_is_that.mp3" },
  { text: "That is my bag. It is big and brown.", voice: "ellen", filename: "aula2_that_is_my_bag_it_is_big.mp3" },
  { text: "What else do you have on your desk?", voice: "arthur", filename: "aula2_what_else_do_you_have.mp3" },
  { text: "I have a pen and a book. This is a blue pen.", voice: "ellen", filename: "aula2_i_have_a_pen_and_a_book.mp3" },
  { text: "The book is red. It is small.", voice: "ellen", filename: "aula2_the_book_is_red.mp3" },
  { text: "Excellent! And where is your key?", voice: "arthur", filename: "aula2_excellent_and_where_is_key.mp3" },
  { text: "My key is here. This is my key.", voice: "ellen", filename: "aula2_my_key_is_here.mp3" },

  // === AULA 3 — Dialogue: David (Arthur) + Gabriela (Ellen) ===
  { text: "Good morning, Gabriela! Tell me about your day.", voice: "arthur", filename: "aula3_good_morning_tell_me.mp3" },
  { text: "What do you do first in the morning?", voice: "arthur", filename: "aula3_what_do_you_do_first.mp3" },
  { text: "I wake up at 7. Then I eat breakfast.", voice: "ellen", filename: "aula3_i_wake_up_then_eat.mp3" },
  { text: "What time do you go to work?", voice: "arthur", filename: "aula3_what_time_go_to_work.mp3" },
  { text: "I go to work at 9. I take the metro.", voice: "ellen", filename: "aula3_i_go_to_work_metro.mp3" },
  { text: "I start work at 9. I finish at 6.", voice: "ellen", filename: "aula3_i_start_finish.mp3" },
  { text: "And what do you do at night?", voice: "arthur", filename: "aula3_what_do_at_night.mp3" },
  { text: "At night, I go home. I eat dinner at 8.", voice: "ellen", filename: "aula3_at_night_dinner.mp3" },
  { text: "That sounds like a busy day!", voice: "arthur", filename: "aula3_busy_day.mp3" },
  { text: "Yes! I am very busy.", voice: "ellen", filename: "aula3_yes_very_busy.mp3" },

  // === AULA 4 — Dialogue: David (Arthur) + Gabriela (Ellen) ===
  { text: "Tell me about your family, Gabriela.", voice: "arthur", filename: "aula4_tell_me_about_family.mp3" },
  { text: "Do you have brothers or sisters?", voice: "arthur", filename: "aula4_do_you_have_brothers.mp3" },
  { text: "I have one brother. He lives in Sao Paulo.", voice: "ellen", filename: "aula4_i_have_one_brother.mp3" },
  { text: "Where does your mother live?", voice: "arthur", filename: "aula4_where_does_mother_live.mp3" },
  { text: "My mother lives in Jau. She is 58 years old.", voice: "ellen", filename: "aula4_my_mother_lives_jau_58.mp3" },
  { text: "And your father? What does he do?", voice: "arthur", filename: "aula4_and_your_father.mp3" },
  { text: "My father works at a hospital. He wakes up very early.", voice: "ellen", filename: "aula4_father_works_hospital.mp3" },
  { text: "Do you see your family often?", voice: "arthur", filename: "aula4_do_you_see_family.mp3" },
  { text: "We eat dinner together on Sundays.", voice: "ellen", filename: "aula4_we_eat_dinner_sundays.mp3" },
  { text: "That is wonderful! Family is important.", voice: "arthur", filename: "aula4_that_is_wonderful.mp3" },
  { text: "Yes! My family is very important to me.", voice: "ellen", filename: "aula4_yes_family_important.mp3" },

  // === AULA 5 — Review questions (alternate) ===
  { text: "Where do you live and work?", voice: "arthur", filename: "aula5_where_do_you_live_and_work.mp3" },
  { text: "What do you have on your desk?", voice: "ellen", filename: "aula5_what_do_you_have_on_your_desk.mp3" },
];

async function generateAudio(phrase, voiceId, outputPath) {
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: {
      'xi-api-key': API_KEY,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      text: phrase,
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
    console.error('ERROR: ELEVENLABS_API_KEY not set');
    process.exit(1);
  }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  let generated = 0, skipped = 0, failed = 0;
  console.log(`Generating ${PHRASES.length} IN CLASS dialogue audio files...\n`);

  for (const phrase of PHRASES) {
    const outputPath = path.join(OUTPUT_DIR, phrase.filename);
    if (fs.existsSync(outputPath)) { console.log(`  SKIP: ${phrase.filename}`); skipped++; continue; }
    const voiceId = phrase.voice === 'ellen' ? ELLEN_ID : ARTHUR_ID;
    try {
      const bytes = await generateAudio(phrase.text, voiceId, outputPath);
      console.log(`  OK [${phrase.voice}]: ${phrase.filename} (${(bytes/1024).toFixed(1)}KB)`);
      generated++;
      await new Promise(r => setTimeout(r, 500));
    } catch (err) {
      console.error(`  FAIL: ${phrase.filename} — ${err.message}`);
      failed++;
    }
  }
  console.log(`\nDone: ${generated} generated, ${skipped} skipped, ${failed} failed`);
  if (failed > 0) process.exit(1);
}

main().catch(err => { console.error(err); process.exit(1); });
