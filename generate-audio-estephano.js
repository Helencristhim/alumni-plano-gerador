const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'estephano-akihito-ishii');

const entries = [
  // SINGLE WORDS (Ash - student gender)
  { file: 'introduce.mp3', text: 'Introduce', voice: ASH },
  { file: 'student.mp3', text: 'Student', voice: ASH },
  { file: 'study.mp3', text: 'Study', voice: ASH },
  { file: 'course.mp3', text: 'Course', voice: ASH },
  { file: 'technology.mp3', text: 'Technology', voice: ASH },
  { file: 'goal.mp3', text: 'Goal', voice: ASH },
  { file: 'career.mp3', text: 'Career', voice: ASH },

  // VOCAB EXAMPLES (alternate Ash/Riley)
  { file: 'let_me_introduce_myself.mp3', text: 'Let me introduce myself.', voice: ASH },
  { file: 'i_am_a_student.mp3', text: 'I am a student.', voice: RILEY },
  { file: 'i_study_every_day.mp3', text: 'I study every day.', voice: ASH },
  { file: 'my_course_is_systems_analysis.mp3', text: 'My course is Systems Analysis.', voice: RILEY },
  { file: 'technology_is_important_for_my_career.mp3', text: 'Technology is important for my career.', voice: ASH },
  { file: 'my_goal_is_to_work_in_cybersecurity.mp3', text: 'My goal is to work in cybersecurity.', voice: RILEY },
  { file: 'i_want_a_career_in_technology.mp3', text: 'I want a career in technology.', voice: ASH },

  // SURVIVAL PHRASES (alternate)
  { file: 'my_name_is_estephano.mp3', text: 'My name is Estephano.', voice: ASH },
  { file: 'nice_to_meet_you.mp3', text: 'Nice to meet you.', voice: RILEY },
  { file: 'i_am_from_sao_paulo.mp3', text: 'I am from São Paulo.', voice: ASH },
  { file: 'could_you_repeat_that_please.mp3', text: 'Could you repeat that, please?', voice: RILEY },

  // FILL-IN PHRASES (alternate)
  { file: 'i_study_systems_analysis_at_university.mp3', text: 'I study Systems Analysis at university.', voice: ASH },
  { file: 'my_goal_is_to_have_a_career_in_cybersecuri.mp3', text: 'My goal is to have a career in cybersecurity.', voice: RILEY },
  { file: 'i_want_to_introduce_myself_to_the_team.mp3', text: 'I want to introduce myself to the team.', voice: ASH },
  { file: 'technology_is_part_of_my_daily_life.mp3', text: 'Technology is part of my daily life.', voice: RILEY },

  // DIALOGUE (Sara=Riley, Estephano=Ash)
  { file: 'hi_my_name_is_sara_nice_to_meet_you.mp3', text: 'Hi! My name is Sara. Nice to meet you.', voice: RILEY },
  { file: 'hi_i_am_estephano_nice_to_meet_you_too.mp3', text: 'Hi! I am Estephano. Nice to meet you too.', voice: ASH },
  { file: 'what_do_you_do_estephano.mp3', text: 'What do you do, Estephano?', voice: RILEY },
  { file: 'i_am_a_student_i_study_systems_analysis.mp3', text: 'I am a student. I study Systems Analysis.', voice: ASH },
  { file: 'that_sounds_interesting_do_you_like_technol.mp3', text: 'That sounds interesting! Do you like technology?', voice: RILEY },
  { file: 'yes_technology_is_very_important_for_my_car.mp3', text: 'Yes! Technology is very important for my career.', voice: ASH },
  { file: 'what_is_your_goal.mp3', text: 'What is your goal?', voice: RILEY },

  // SPEECH CARDS (Ash - student gender)
  { file: 'my_name_is_estephano_i_am_from_sao_paulo.mp3', text: 'My name is Estephano. I am from São Paulo.', voice: ASH },
  { file: 'i_study_systems_analysis_my_goal_is_cyberse.mp3', text: 'I study Systems Analysis. My goal is cybersecurity.', voice: ASH },

  // GRAMMAR EXAMPLES (alternate)
  { file: 'i_am_estephano.mp3', text: 'I am Estephano.', voice: ASH },
  { file: 'you_are_a_student.mp3', text: 'You are a student.', voice: RILEY },
  { file: 'she_is_from_sao_paulo.mp3', text: 'She is from São Paulo.', voice: RILEY },
  { file: 'we_are_in_class.mp3', text: 'We are in class.', voice: ASH },
  { file: 'they_are_students.mp3', text: 'They are students.', voice: RILEY },
  { file: 'he_is_a_programmer.mp3', text: 'He is a programmer.', voice: ASH },
  { file: 'i_am_twenty_seven_years_old.mp3', text: 'I am twenty-seven years old.', voice: ASH },
  { file: 'we_are_students_at_the_university.mp3', text: 'We are students at the university.', voice: RILEY },
  { file: 'i_am_from_brazil.mp3', text: 'I am from Brazil.', voice: ASH },
  { file: 'she_is_a_programmer.mp3', text: 'She is a programmer.', voice: RILEY },
  { file: 'my_name_is_estephano_ishii.mp3', text: 'My name is Estephano Ishii.', voice: ASH },

  // ORDERING
  { file: 'order_l1_introduction.mp3', text: 'My name is Estephano. I am from São Paulo. I study Systems Analysis. My goal is to work in cybersecurity. Nice to meet you!', voice: ASH },

  // LISTENING PASSAGES
  { file: 'listening_leo_introduction.mp3', text: 'Hi, my name is Leo. I am from São Paulo, Brazil. I am twenty-five years old. I study Computer Science at university. Technology is my passion. My goal is to work at a big tech company. I want a career in software development. Nice to meet you!', voice: ASH },
  { file: 'listening_ana_introduction.mp3', text: 'Good morning! My name is Ana. I am from Rio de Janeiro. I am a cybersecurity student. I study at Federal University. My goal is to work at a multinational company. Technology is very important for my career. Nice to meet you!', voice: RILEY },
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

  console.log(`Generating ${entries.length} audio files for Estephano Akihito Ishii...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  for (const entry of entries) {
    await generateAudio(entry);
    await new Promise(r => setTimeout(r, 500));
  }

  console.log('\nDone!');
}

main().catch(console.error);
