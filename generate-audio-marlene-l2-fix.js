const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY env variable'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';
const AUDIO_DIR = path.join(BASE_DIR, 'audio/marlene-landucci');

// Missing audio entries from Aula 2
const audioEntries = [
  { text: "I wake up early every day.", file: "i_wake_up_early_every_day.mp3", voice: ELLEN },
  { text: "She always has breakfast at seven.", file: "she_always_has_breakfast_at_seven.mp3", voice: ARTHUR },
  { text: "We usually exercise in the morning.", file: "we_usually_exercise_in_the_morning.mp3", voice: ELLEN },
  { text: "He sometimes travels for work.", file: "he_sometimes_travels_for_work.mp3", voice: ARTHUR },
  { text: "I usually walk my dogs in the morning.", file: "i_usually_walk_my_dogs_in_the_morning.mp3", voice: ELLEN },
  { text: "She wakes up at six every day.", file: "she_wakes_up_at_six_every_day.mp3", voice: ARTHUR },
  { text: "Marlene wakes up at six. She has breakfast at seven. She usually checks her properties in the morning. She always has lunch at noon. In the afternoon, she sometimes plays tennis. She never goes to bed late.", file: "marlene_wakes_up_at_six_she_has_breakfast.mp3", voice: ELLEN },
  { text: "She usually checks her properties in the morning.", file: "she_usually_checks_her_properties.mp3", voice: ARTHUR },
  { text: "She always has lunch at noon.", file: "she_always_has_lunch_at_noon.mp3", voice: ELLEN },
  { text: "In the afternoon, she sometimes plays tennis.", file: "in_the_afternoon_she_sometimes_plays_tennis.mp3", voice: ARTHUR },
  { text: "She never goes to bed late.", file: "she_never_goes_to_bed_late.mp3", voice: ELLEN },
  { text: "I always have coffee in the morning.", file: "i_always_have_coffee_in_the_morning.mp3", voice: ELLEN },
  { text: "I usually check my properties before lunch.", file: "i_usually_check_my_properties_before_lunch.mp3", voice: ELLEN },
  { text: "I sometimes play tennis in the afternoon.", file: "i_sometimes_play_tennis_in_the_afternoon.mp3", voice: ELLEN },
  { text: "My schedule is busy but I love it.", file: "my_schedule_is_busy_but_i_love_it.mp3", voice: ELLEN },
  { text: "I never skip my morning routine.", file: "i_never_skip_my_morning_routine.mp3", voice: ELLEN },
  // Dialogue - Marlene lines = Ellen
  { text: "Hi Lisa! So nice to see you here in Rome!", file: "hi_lisa_so_nice_to_see_you_here_in_rome.mp3", voice: ELLEN },
  { text: "I am great! I always wake up early when I travel.", file: "i_am_great_i_always_wake_up_early_when_i_travel.mp3", voice: ELLEN },
  { text: "I usually have breakfast at the hotel. Then I walk around the city.", file: "i_usually_have_breakfast_at_the_hotel.mp3", voice: ELLEN },
  { text: "Do you exercise when you travel?", file: "do_you_exercise_when_you_travel.mp3", voice: ELLEN },
  { text: "Not always. But I always walk a lot! My schedule is very busy with sightseeing.", file: "not_always_but_i_always_walk_a_lot.mp3", voice: ELLEN },
  // Dialogue - Lisa lines = Ellen (female character)
  { text: "Marlene! What a surprise! How are you?", file: "marlene_what_a_surprise_how_are_you.mp3", voice: ELLEN },
  { text: "Me too! What is your morning routine here?", file: "me_too_what_is_your_morning_routine_here.mp3", voice: ELLEN },
  { text: "That sounds lovely! I sometimes skip breakfast and go straight to a cafe.", file: "that_sounds_lovely_i_sometimes_skip_breakfast.mp3", voice: ELLEN },
  // Listenings
  { text: "Good morning! Today we talk to people about their daily routines. First, we have Anna from Germany. Anna, what is your daily routine? Well, I always wake up at six thirty. I have breakfast at seven. I usually have coffee and toast. Then I go to work at eight. I work in an office. I usually have lunch at twelve thirty. After work, I sometimes go to the gym. I always cook dinner at home. I never eat out on weekdays.", file: "lp_listen_l2_1_daily_routine.mp3", voice: ELLEN },
  { text: "My name is Marco. I am from Italy. I live in Rome. My morning schedule is very busy. I wake up at five forty-five every day. I always have a big Italian breakfast. Coffee, bread, and cheese. Then I exercise for twenty minutes. I usually run in the park near my house. After that, I go to work. I am a tour guide. I sometimes start work at eight, sometimes at nine. My schedule changes every day, but I always keep my morning routine the same.", file: "lp_listen_l2_2_morning_schedule.mp3", voice: ARTHUR },
  // Additional
  { text: "She usually wakes up at six.", file: "she_usually_wakes_up_at_six.mp3", voice: ARTHUR },
];

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: text,
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

  let generated = 0;
  let skipped = 0;

  console.log(`\nGenerating ${audioEntries.length} missing audio files for marlene-landucci Aula 2\n`);

  for (let i = 0; i < audioEntries.length; i++) {
    const entry = audioEntries[i];
    const fullPath = path.join(AUDIO_DIR, entry.file);

    if (fs.existsSync(fullPath)) {
      skipped++;
      console.log(`Skipped: ${entry.file} (exists)`);
      continue;
    }

    const voiceName = entry.voice === ELLEN ? 'Ellen' : 'Arthur';
    try {
      const buffer = await generateAudio(entry.text, entry.voice);
      fs.writeFileSync(fullPath, buffer);
      generated++;
      console.log(`Generated ${generated}: ${entry.file} (${voiceName})`);
      if (i < audioEntries.length - 1) await delay(500);
    } catch (err) {
      console.error(`FAILED: ${entry.file} — ${err.message}`);
    }
  }

  console.log(`\n=== SUMMARY ===`);
  console.log(`Total: ${audioEntries.length}`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped: ${skipped}`);
  console.log(`Failed: ${audioEntries.length - generated - skipped}`);
}

main();
