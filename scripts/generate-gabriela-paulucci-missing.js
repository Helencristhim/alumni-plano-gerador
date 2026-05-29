const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR_ID = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN_ID = 'BIvP0GN1cAtSRTxNHnWS';

const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-paulucci');

// ===== MISSING MP3s identified by audit + full scan =====
// Rule: 1-2 words = Arthur, 3+ words = alternate Arthur/Ellen

const PHRASES = [
  // Survival / Emergency phrases (missing MP3s)
  { text: "Could you repeat that, please?", voice: "ellen", filename: "could_you_repeat_that_please.mp3" },
  { text: "How do you say this in English?", voice: "arthur", filename: "how_do_you_say_this_in_english.mp3" },
  { text: "I do not understand.", voice: "ellen", filename: "i_do_not_understand.mp3" },
  { text: "Can you speak slowly?", voice: "arthur", filename: "can_you_speak_slowly.mp3" },
  { text: "Thank you!", voice: "ellen", filename: "thank_you.mp3" },

  // Aula 1 missing
  { text: "I am 33 years old", voice: "ellen", filename: "i_am_33_years_old_no_dot.mp3" },
  { text: "I am from Jau. It is a small city. But I live in Sao Paulo now.", voice: "ellen", filename: "i_am_from_jau_it_is_a_small_city_but_i_live_in_sao_paulo.mp3" },

  // Aula 2 missing (audit flagged)
  { text: "What color is your pen?", voice: "arthur", filename: "aula2_what_color_is_your_pen.mp3" },

  // Aula 3 missing
  { text: "I wake up at 7 in the morning.", voice: "ellen", filename: "aula3_i_wake_up_at_7.mp3" },
  { text: "I start work at 9 in the morning.", voice: "arthur", filename: "aula3_i_start_work_at_9.mp3" },
  { text: "I finish work at 6 in the afternoon.", voice: "ellen", filename: "aula3_i_finish_work_at_6.mp3" },
  { text: "In the afternoon, I work at Itau.", voice: "arthur", filename: "aula3_in_the_afternoon_i_work.mp3" },
  { text: "I eat dinner at 8 at night.", voice: "ellen", filename: "aula3_i_eat_dinner_at_8.mp3" },

  // Aula 4 missing (audit flagged: She speaks Portuguese and English.)
  { text: "My family is very important to me.", voice: "arthur", filename: "aula4_my_family_is_very_important.mp3" },
  { text: "We eat dinner together at night.", voice: "ellen", filename: "aula4_we_eat_dinner_together.mp3" },
  { text: "She wakes up at 6 in the morning.", voice: "arthur", filename: "aula4_she_wakes_up_at_6.mp3" },
  { text: "My mother is 58 years old.", voice: "ellen", filename: "aula4_my_mother_is_58.mp3" },
  { text: "She speaks Portuguese and English.", voice: "arthur", filename: "aula4_she_speaks_portuguese_and_english.mp3" },

  // Aula 5 missing
  { text: "My name is Gabriela. I am 33 years old. I am from Jau.", voice: "ellen", filename: "aula5_full_intro.mp3" },
  { text: "I live in Sao Paulo. I work at Itau.", voice: "arthur", filename: "aula5_live_work.mp3" },
  { text: "This is my phone. It is black.", voice: "ellen", filename: "aula5_this_phone_black.mp3" },
  { text: "That is my bag. It is big.", voice: "arthur", filename: "aula5_that_bag_big.mp3" },
  { text: "I wake up at 7. I eat breakfast at 8.", voice: "ellen", filename: "aula5_wake_breakfast.mp3" },
  { text: "I go to work at 9. I finish at 6.", voice: "arthur", filename: "aula5_go_work_finish.mp3" },
  { text: "My mother lives in Jau. She is 58.", voice: "ellen", filename: "aula5_mother_lives_jau.mp3" },
  { text: "My father works at a hospital.", voice: "arthur", filename: "aula5_father_hospital.mp3" },
  { text: "We eat dinner together on Sundays.", voice: "ellen", filename: "aula5_dinner_together.mp3" },
  { text: "She speaks English and Portuguese.", voice: "arthur", filename: "aula5_she_speaks.mp3" },
  { text: "Tell me about yourself, Gabriela.", voice: "ellen", filename: "aula5_tell_me_about_yourself.mp3" },
  { text: "Describe your daily routine.", voice: "arthur", filename: "aula5_describe_routine.mp3" },
  { text: "Who is important in your life?", voice: "ellen", filename: "aula5_who_is_important.mp3" },
  { text: "I am proud of my English!", voice: "arthur", filename: "aula5_proud_of_english.mp3" },

  // ===== ORDERING AUDIO (correct sequence spoken as one MP3) =====
  // order-l1: Self-introduction sequence
  { text: "My name is Gabriela. I am 33 years old. I am from Jau. I live in Sao Paulo. I work at Itau.", voice: "ellen", filename: "order_l1_intro.mp3" },
  // order-l2: Describing objects
  { text: "This is my phone. It is black. That is my bag. It is big and brown. I also have a blue pen.", voice: "ellen", filename: "order_l2_objects.mp3" },
  // order-l3: Daily routine chronological
  { text: "I wake up at 7 in the morning. I eat breakfast at 8. I go to work at 9. I eat lunch at noon. I finish work at 6. I go home at night.", voice: "arthur", filename: "order_l3_routine.mp3" },
  // order-l4: Describing a person (mother)
  { text: "This is my mother. Her name is Maria. She lives in Jau. She is 58 years old. She wakes up at 6 in the morning.", voice: "ellen", filename: "order_l4_family.mp3" },
  // order-l5: Gabriela's complete story
  { text: "My name is Gabriela. I am from Jau. I live in Sao Paulo. This is my phone. It is black. I wake up at 7. I eat breakfast at 8. I go to work at 9. I finish at 6. My mother lives in Jau. My father works at a hospital. We eat dinner together on Sundays.", voice: "ellen", filename: "order_l5_story.mp3" },
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
    console.error('Run: ELEVENLABS_API_KEY=your_key node scripts/generate-gabriela-paulucci-missing.js');
    process.exit(1);
  }

  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  let generated = 0;
  let skipped = 0;
  let failed = 0;

  console.log(`Generating ${PHRASES.length} missing audio files for Gabriela Paulucci...\n`);

  for (const phrase of PHRASES) {
    const outputPath = path.join(OUTPUT_DIR, phrase.filename);

    if (fs.existsSync(outputPath)) {
      console.log(`  SKIP (exists): ${phrase.filename}`);
      skipped++;
      continue;
    }

    const voiceId = phrase.voice === 'ellen' ? ELLEN_ID : ARTHUR_ID;

    try {
      const bytes = await generateAudio(phrase.text, voiceId, outputPath);
      console.log(`  OK [${phrase.voice}]: ${phrase.filename} (${(bytes/1024).toFixed(1)}KB)`);
      generated++;
      // Rate limit: 2 per second
      await new Promise(r => setTimeout(r, 500));
    } catch (err) {
      console.error(`  FAIL: ${phrase.filename} — ${err.message}`);
      failed++;
    }
  }

  console.log(`\nDone: ${generated} generated, ${skipped} skipped, ${failed} failed`);
  if (failed > 0) {
    console.error('WARNING: Some files failed to generate. Re-run the script to retry.');
    process.exit(1);
  }
}

main().catch(err => { console.error(err); process.exit(1); });
