const https = require('https');
const fs = require('fs');
const path = require('path');

const ASH = 'VU16byTywsWv5JpI8rbc';
const RILEY = 'hA4zGnmTwX2NQiTRMt7o';
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'estephano-akihito-ishii');

const entries = [
  // SINGLE WORDS (Ash - student gender)
  { file: 'aula2_age.mp3', text: 'Age', voice: ASH },
  { file: 'aula2_years_old.mp3', text: 'Years old', voice: ASH },
  { file: 'aula2_university.mp3', text: 'University', voice: ASH },
  { file: 'aula2_development.mp3', text: 'Development', voice: ASH },
  { file: 'aula2_passion.mp3', text: 'Passion', voice: ASH },
  { file: 'aula2_profile.mp3', text: 'Profile', voice: ASH },
  { file: 'aula2_interested.mp3', text: 'Interested', voice: ASH },

  // VOCAB EXAMPLES (alternate Riley/Ash)
  { file: 'aula2_what_is_your_age.mp3', text: 'What is your age?', voice: RILEY },
  { file: 'aula2_im_twenty_seven_years_old.mp3', text: "I'm twenty-seven years old.", voice: ASH },
  { file: 'aula2_i_study_at_a_university.mp3', text: 'I study at a university.', voice: RILEY },
  { file: 'aula2_i_study_systems_analysis_and_developm.mp3', text: 'I study Systems Analysis and Development.', voice: ASH },
  { file: 'aula2_technology_is_my_passion.mp3', text: 'Technology is my passion.', voice: RILEY },
  { file: 'aula2_this_is_my_linkedin_profile.mp3', text: 'This is my LinkedIn profile.', voice: ASH },
  { file: 'aula2_im_interested_in_cybersecurity.mp3', text: "I'm interested in cybersecurity.", voice: RILEY },

  // CONTRACTION EXAMPLES (alternate Ash/Riley)
  { file: 'aula2_im_estephano.mp3', text: "I'm Estephano.", voice: ASH },
  { file: 'aula2_im_from_sao_paulo.mp3', text: "I'm from São Paulo.", voice: ASH },
  { file: 'aula2_im_a_student.mp3', text: "I'm a student.", voice: ASH },
  { file: 'aula2_youre_a_developer.mp3', text: "You're a developer.", voice: RILEY },
  { file: 'aula2_hes_from_campinas.mp3', text: "He's from Campinas.", voice: ASH },
  { file: 'aula2_shes_a_cybersecurity_analyst.mp3', text: "She's a cybersecurity analyst.", voice: RILEY },
  { file: 'aula2_were_students.mp3', text: "We're students.", voice: ASH },
  { file: 'aula2_theyre_interested_in_technology.mp3', text: "They're interested in technology.", voice: RILEY },

  // FILL-IN PHRASES (alternate Ash/Riley)
  { file: 'aula2_im_a_systems_analysis_student_at_uni.mp3', text: "I'm a Systems Analysis student at university.", voice: ASH },
  { file: 'aula2_my_passion_is_technology_and_cybersec.mp3', text: 'My passion is technology and cybersecurity.', voice: RILEY },
  { file: 'aula2_im_very_interested_in_this_area.mp3', text: "I'm very interested in this area.", voice: ASH },

  // DIALOGUE (Lisa=Riley, Estephano=Ash)
  { file: 'aula2_good_morning_im_lisa_from_techcorp.mp3', text: "Good morning! I'm Lisa from TechCorp. Please, tell me about yourself.", voice: RILEY },
  { file: 'aula2_hi_im_estephano_im_twenty_seven.mp3', text: "Hi! I'm Estephano. I'm twenty-seven years old.", voice: ASH },
  { file: 'aula2_nice_to_meet_you_where_are_you_from.mp3', text: 'Nice to meet you, Estephano. Where are you from?', voice: RILEY },
  { file: 'aula2_im_from_sao_paulo_im_a_student.mp3', text: "I'm from São Paulo. I'm a student at university.", voice: ASH },
  { file: 'aula2_whats_your_course.mp3', text: "What's your course?", voice: RILEY },
  { file: 'aula2_i_study_sad_technology_is_my_passion.mp3', text: 'I study Systems Analysis and Development. Technology is my passion.', voice: ASH },
  { file: 'aula2_thats_great_whats_your_goal.mp3', text: "That's great! What's your goal?", voice: RILEY },
  { file: 'aula2_my_goal_cybersecurity_interested.mp3', text: "My goal is to work in cybersecurity. I'm very interested in this area.", voice: ASH },

  // SPEECH CARDS (Ash - student gender)
  { file: 'aula2_speech1_full_intro.mp3', text: "I'm Estephano. I'm twenty-seven years old. I'm from São Paulo.", voice: ASH },
  { file: 'aula2_speech2_studies_passion.mp3', text: "I'm a student. I study Systems Analysis and Development. Technology is my passion.", voice: ASH },

  // ORDERING
  { file: 'order_l2_contraction_intro.mp3', text: "I'm Estephano. I'm twenty-seven years old. I'm from São Paulo. I'm a student at university. Technology is my passion. I'm very interested in this area.", voice: ASH },

  // LISTENING PASSAGES
  { file: 'aula2_listening_alex.mp3', text: "Hi, I'm Alex. I'm twenty-three years old. I'm from Campinas, Brazil. I'm a software developer. I work at a tech company. My passion is programming. I'm interested in artificial intelligence. Nice to meet you!", voice: ASH },
  { file: 'aula2_listening_maria.mp3', text: "Hello! I'm Maria. I'm twenty-nine years old. I'm from São Paulo. I'm a cybersecurity analyst. I work at a multinational company. My experience is in network security. I'm passionate about technology. Nice to meet you!", voice: RILEY },

  // SURVIVAL (new phrases only)
  { file: 'aula2_im_a_student_at_university.mp3', text: "I'm a student at university.", voice: ASH },
  { file: 'aula2_whats_your_name.mp3', text: "What's your name?", voice: RILEY },
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

  console.log(`Generating ${entries.length} audio files for Estephano Akihito Ishii (Aula 2)...`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  for (const entry of entries) {
    await generateAudio(entry);
    await new Promise(r => setTimeout(r, 500));
  }

  console.log('\nDone!');
}

main().catch(console.error);
