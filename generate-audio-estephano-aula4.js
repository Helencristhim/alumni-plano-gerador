const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'estephano-akihito-ishii');

const entries = [
  // SINGLE WORDS (Ash - student gender)
  { file: 'aula4_number.mp3', text: 'Number', voice: ASH },
  { file: 'aula4_clock.mp3', text: 'Clock', voice: ASH },
  { file: 'aula4_hour.mp3', text: 'Hour', voice: ASH },
  { file: 'aula4_minute.mp3', text: 'Minute', voice: ASH },
  { file: 'aula4_day.mp3', text: 'Day', voice: ASH },
  { file: 'aula4_week.mp3', text: 'Week', voice: ASH },
  { file: 'aula4_schedule.mp3', text: 'Schedule', voice: ASH },

  // VOCAB EXAMPLES (alternate Ash/Riley)
  { file: 'aula4_my_phone_number.mp3', text: 'My phone number is 99123-4567.', voice: ASH },
  { file: 'aula4_look_at_the_clock.mp3', text: 'Look at the clock. It\'s 9 AM.', voice: RILEY },
  { file: 'aula4_class_one_hour.mp3', text: 'The class is one hour long.', voice: ASH },
  { file: 'aula4_wait_five_minutes.mp3', text: 'Wait five minutes, please.', voice: RILEY },
  { file: 'aula4_monday_favorite_day.mp3', text: 'Monday is my favorite day.', voice: ASH },
  { file: 'aula4_three_days_a_week.mp3', text: 'I have classes three days a week.', voice: RILEY },
  { file: 'aula4_this_is_my_schedule.mp3', text: 'This is my class schedule.', voice: ASH },

  // GRAMMAR/PRACTICE PHRASES (alternate)
  { file: 'aula4_nine_oclock.mp3', text: 'It\'s nine o\'clock.', voice: ASH },
  { file: 'aula4_ten_fifteen.mp3', text: 'It\'s ten fifteen.', voice: RILEY },
  { file: 'aula4_half_past_two.mp3', text: 'It\'s half past two.', voice: ASH },
  { file: 'aula4_what_time_is_it.mp3', text: 'What time is it?', voice: RILEY },
  { file: 'aula4_class_starts_at_8.mp3', text: 'The class starts at 8 AM.', voice: ASH },
  { file: 'aula4_study_monday_wednesday.mp3', text: 'I study on Monday and Wednesday.', voice: ASH },
  { file: 'aula4_class_in_the_morning.mp3', text: 'My class is in the morning.', voice: RILEY },
  { file: 'aula4_break_at_10.mp3', text: 'I have a break at 10 AM.', voice: ASH },
  { file: 'aula4_test_on_friday.mp3', text: 'The test is on Friday.', voice: RILEY },

  // DIALOGUE (Ana=Riley, Estephano=Ash)
  { file: 'aula4_dialogue_ana_1.mp3', text: 'Hi Estephano! What time is your first class?', voice: RILEY },
  { file: 'aula4_dialogue_estephano_1.mp3', text: 'It\'s at 8 AM. I have ADS on Monday, Wednesday, and Friday.', voice: ASH },
  { file: 'aula4_dialogue_ana_2.mp3', text: 'What about Tuesday?', voice: RILEY },
  { file: 'aula4_dialogue_estephano_2.mp3', text: 'On Tuesday I study cybersecurity from 9 to noon.', voice: ASH },
  { file: 'aula4_dialogue_ana_3.mp3', text: 'How many hours of class do you have?', voice: RILEY },
  { file: 'aula4_dialogue_estephano_3.mp3', text: 'About twenty hours a week. What about you?', voice: ASH },
  { file: 'aula4_dialogue_ana_4.mp3', text: 'I have fifteen hours. My schedule is different.', voice: RILEY },
  { file: 'aula4_dialogue_estephano_4.mp3', text: 'What day is the test?', voice: ASH },

  // SPEECH CARDS (Ash - student)
  { file: 'aula4_speech1_schedule.mp3', text: 'My ADS class starts at 8 AM on Monday. The class is two hours long.', voice: ASH },
  { file: 'aula4_speech2_weekly.mp3', text: 'I study cybersecurity on Tuesday. I have a break at 10 AM for fifteen minutes.', voice: ASH },

  // ORDERING
  { file: 'order_l4_schedule.mp3', text: 'What time is it? It\'s 8 AM. My class starts now. The class is two hours long. I have a break at 10.', voice: ASH },

  // LISTENING PASSAGES
  { file: 'aula4_listening_schedule.mp3', text: 'Hi! My name is Rafael. I\'m a computer science student. My schedule is very busy. On Monday and Wednesday, I have programming class at 8 AM. The class is two hours long. I have a break at 10 AM for fifteen minutes. On Tuesday and Thursday, I have math class at 9 AM. On Friday, I have a lab from 2 PM to 5 PM. I have twenty hours of class a week. My favorite day is Friday because I only have class in the afternoon.', voice: ASH },
  { file: 'aula4_listening_teacher.mp3', text: 'Good morning, everyone. Today is Wednesday. Let me check the schedule. Your first class is at 9 o\'clock. It\'s English. The class is one hour long. At 10 o\'clock, you have a fifteen-minute break. Then, at 10:15, you have mathematics for two hours. Lunch is at noon. In the afternoon, at 2 PM, you have computer science. That class finishes at half past three. Please check the schedule on the board.', voice: RILEY },

  // SURVIVAL PHRASES
  { file: 'aula4_its_9_oclock.mp3', text: 'It\'s 9 o\'clock.', voice: ASH },
  { file: 'aula4_my_class_starts.mp3', text: 'My class starts at 8 AM.', voice: ASH },
  { file: 'aula4_today_is_monday.mp3', text: 'Today is Monday.', voice: RILEY },
  { file: 'aula4_class_on_wednesday.mp3', text: 'I have class on Wednesday.', voice: ASH },
];

function generateAudio(entry) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text: entry.text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${entry.voice}`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY,
        'Content-Length': Buffer.byteLength(data)
      }
    };

    const outPath = path.join(OUTPUT_DIR, entry.file);

    if (fs.existsSync(outPath)) {
      console.log(`SKIP (exists): ${entry.file}`);
      return resolve();
    }

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', d => body += d);
        res.on('end', () => {
          console.error(`ERROR ${res.statusCode} for ${entry.file}: ${body}`);
          resolve();
        });
        return;
      }
      const ws = fs.createWriteStream(outPath);
      res.pipe(ws);
      ws.on('finish', () => {
        console.log(`OK: ${entry.file}`);
        resolve();
      });
      ws.on('error', reject);
    });

    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  if (!API_KEY) {
    console.error('ERROR: ELEVENLABS_API_KEY not set. Export it or add to ~/.zshrc');
    process.exit(1);
  }

  if (!fs.existsSync(OUTPUT_DIR)) {
    fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  }

  console.log(`Generating ${entries.length} audio files for Estephano Akihito Ishii (Aula 4)...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  for (const entry of entries) {
    await generateAudio(entry);
    await new Promise(r => setTimeout(r, 500));
  }

  console.log('\nDone!');
}

main().catch(console.error);
