const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'estephano-akihito-ishii');

const entries = [
  // SINGLE WORDS (Ash - student gender)
  { file: 'aula3_wake_up.mp3', text: 'Wake up', voice: ASH },
  { file: 'aula3_breakfast.mp3', text: 'Breakfast', voice: ASH },
  { file: 'aula3_attend.mp3', text: 'Attend', voice: ASH },
  { file: 'aula3_lunch.mp3', text: 'Lunch', voice: ASH },
  { file: 'aula3_usually.mp3', text: 'Usually', voice: ASH },
  { file: 'aula3_sometimes.mp3', text: 'Sometimes', voice: ASH },
  { file: 'aula3_every_day.mp3', text: 'Every day', voice: ASH },

  // VOCAB EXAMPLES (alternate Ash/Riley)
  { file: 'aula3_i_wake_up_at_8_am.mp3', text: 'I wake up at 8 AM.', voice: ASH },
  { file: 'aula3_i_have_breakfast_at_8_30.mp3', text: 'I have breakfast at 8:30.', voice: RILEY },
  { file: 'aula3_i_attend_class_in_the_morning.mp3', text: 'I attend class in the morning.', voice: ASH },
  { file: 'aula3_i_have_lunch_at_noon.mp3', text: 'I have lunch at noon.', voice: RILEY },
  { file: 'aula3_i_usually_study_in_the_afternoon.mp3', text: 'I usually study in the afternoon.', voice: ASH },
  { file: 'aula3_i_sometimes_play_video_games.mp3', text: 'I sometimes play video games at night.', voice: RILEY },
  { file: 'aula3_i_study_english_every_day.mp3', text: 'I study English every day.', voice: ASH },

  // FILL-IN PHRASES (alternate Ash/Riley)
  { file: 'aula3_i_wake_up_and_have_breakfast.mp3', text: 'I wake up at 8 and have breakfast.', voice: ASH },
  { file: 'aula3_i_usually_attend_class_morning.mp3', text: 'I usually attend class in the morning.', voice: RILEY },
  { file: 'aula3_sometimes_i_watch_tech_videos.mp3', text: 'Sometimes I watch tech videos on YouTube.', voice: ASH },
  { file: 'aula3_i_play_video_games_every_day.mp3', text: 'I play video games every day.', voice: RILEY },

  // DIALOGUE (Ana=Riley, Estephano=Ash)
  { file: 'aula3_hi_estephano_what_time.mp3', text: 'Hi Estephano! What time do you wake up?', voice: RILEY },
  { file: 'aula3_i_usually_wake_up_at_8.mp3', text: 'I usually wake up at 8 AM. And you?', voice: ASH },
  { file: 'aula3_i_wake_up_at_7_what_do_you_do.mp3', text: 'I wake up at 7. What do you do in the morning?', voice: RILEY },
  { file: 'aula3_i_have_breakfast_and_attend.mp3', text: 'I have breakfast and attend my ADS class.', voice: ASH },
  { file: 'aula3_do_you_study_in_afternoon.mp3', text: 'Do you study in the afternoon too?', voice: RILEY },
  { file: 'aula3_sometimes_i_usually_watch_tech.mp3', text: 'Sometimes. I usually watch tech videos on YouTube.', voice: ASH },
  { file: 'aula3_what_do_you_do_at_night.mp3', text: 'What do you do at night?', voice: RILEY },
  { file: 'aula3_i_play_games_go_to_bed.mp3', text: 'I play video games and go to bed at midnight.', voice: ASH },

  // GRAMMAR (alternate Ash/Riley)
  { file: 'aula3_i_study_ads.mp3', text: 'I study ADS.', voice: ASH },
  { file: 'aula3_he_studies_ads.mp3', text: 'He studies ADS.', voice: RILEY },
  { file: 'aula3_i_play_video_games.mp3', text: 'I play video games.', voice: ASH },
  { file: 'aula3_she_plays_video_games.mp3', text: 'She plays video games.', voice: RILEY },
  { file: 'aula3_i_watch_youtube.mp3', text: 'I watch YouTube.', voice: ASH },
  { file: 'aula3_he_watches_youtube.mp3', text: 'He watches YouTube.', voice: RILEY },

  // SPEECH CARDS (Ash - student gender)
  { file: 'aula3_speech1_morning.mp3', text: 'I wake up at 8 AM. I have breakfast. I attend my ADS class.', voice: ASH },
  { file: 'aula3_speech2_afternoon.mp3', text: 'I usually study in the afternoon. Sometimes I watch tech videos on YouTube.', voice: ASH },

  // ORDERING
  { file: 'order_l3_routine.mp3', text: 'I wake up at 8 AM. I have breakfast at 8:30. I attend my ADS class. I have lunch at noon. I play video games at night.', voice: ASH },

  // LISTENING PASSAGES
  { file: 'aula3_listening_carlos.mp3', text: 'Hi! My name is Carlos. I wake up at 7 AM every day. I have breakfast with my family. In the morning, I attend my computer science class. I usually have lunch at noon. In the afternoon, I study programming. I sometimes play video games after dinner. I go to bed at 11 PM.', voice: ASH },
  { file: 'aula3_listening_juliana.mp3', text: 'Hello! I\'m Juliana. I wake up at 6:30 AM. I always have breakfast before class. I attend my cybersecurity course in the morning. I have lunch at 12:30. In the afternoon, I usually study at the library. Sometimes I watch tech videos on YouTube at night. I go to bed at 10 PM.', voice: RILEY },

  // SURVIVAL
  { file: 'aula3_i_have_breakfast_every_day.mp3', text: 'I have breakfast every day.', voice: ASH },
  { file: 'aula3_what_time_do_you_wake_up.mp3', text: 'What time do you wake up?', voice: RILEY },
  { file: 'aula3_i_go_to_bed_at_midnight.mp3', text: 'I go to bed at midnight.', voice: ASH },
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

  console.log(`Generating ${entries.length} audio files for Estephano Akihito Ishii (Aula 3)...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  for (const entry of entries) {
    await generateAudio(entry);
    await new Promise(r => setTimeout(r, 500));
  }

  console.log('\nDone!');
}

main().catch(console.error);
