const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'erica-maria-machado-santarem');

if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const audioMap = {
  "Introduce": "introduce.mp3",
  "Routine": "routine.mp3",
  "Company": "company.mp3",
  "Challenge": "challenge.mp3",
  "Goal": "goal.mp3",
  "Comfortable": "comfortable.mp3",
  "Practice": "practice.mp3",
  "Let me introduce myself. I am Erica.": "let_me_introduce_myself_i_am_erica.mp3",
  "My routine starts at seven in the morning.": "my_routine_starts_at_seven_in_the_morning.mp3",
  "I work at a company called Biodelta.": "i_work_at_a_company_called_biodelta.mp3",
  "Learning English is a new challenge for me.": "learning_english_is_a_new_challenge_for_me.mp3",
  "My goal is to speak English with confidence.": "my_goal_is_to_speak_english_with_confidence.mp3",
  "I feel comfortable when the teacher speaks slowly.": "i_feel_comfortable_when_the_teacher_speaks_slowly.mp3",
  "I practice English a little every day.": "i_practice_english_a_little_every_day.mp3",
  "I work at Biodelta. I live in Sao Paulo.": "i_work_at_biodelta_i_live_in_sao_paulo.mp3",
  "Every day, I start my routine at seven.": "every_day_i_start_my_routine_at_seven.mp3",
  "My goal is to learn English this year.": "my_goal_is_to_learn_english_this_year.mp3",
  "She introduces herself at the meeting.": "she_introduces_herself_at_the_meeting.mp3",
  "Could you repeat that, please?": "could_you_repeat_that_please.mp3",
  "I do not understand. Could you say that again?": "i_do_not_understand_could_you_say_that_again.mp3",
  "How do you say that in English?": "how_do_you_say_that_in_english.mp3",
  "Could you speak more slowly, please?": "could_you_speak_more_slowly_please.mp3",
  "Challenge accepted!": "challenge_accepted.mp3",
  "My name is Erica. Nice to meet you.": "my_name_is_erica_nice_to_meet_you.mp3",
  "I work at Biodelta in Sao Paulo.": "i_work_at_biodelta_in_sao_paulo.mp3",
  "Hello! My name is David. I work here at the conference. What is your name?": "hello_my_name_is_david_i_work_here.mp3",
  "Hi David! I am Erica. Nice to meet you.": "hi_david_i_am_erica_nice_to_meet_you.mp3",
  "Nice to meet you, Erica! Where do you work?": "nice_to_meet_you_erica_where_do_you_work.mp3",
  "I work at Biodelta. It is a company in Sao Paulo.": "i_work_at_biodelta_it_is_a_company_in_sao_paulo.mp3",
  "That sounds interesting! What is your daily routine like?": "that_sounds_interesting_what_is_your_daily_routine.mp3",
  "I start work early, at eight. I finish at one in the afternoon.": "i_start_work_early_at_eight_i_finish_at_one.mp3",
  "Do you have any goals for this year?": "do_you_have_any_goals_for_this_year.mp3",
  "Yes! My goal is to practice English every day. Challenge accepted!": "yes_my_goal_is_to_practice_english_every_day.mp3",
  "I live in Sao Paulo.": "i_live_in_sao_paulo.mp3",
  "I work at Biodelta.": "i_work_at_biodelta.mp3",
  "My name is Erica.": "my_name_is_erica.mp3",
  "Nice to meet you.": "nice_to_meet_you.mp3",
  "I practice English every day.": "i_practice_english_every_day.mp3",
  "My goal is to speak with confidence.": "my_goal_is_to_speak_with_confidence.mp3",
  "Good morning. My name is Erica. I am from Sao Paulo. I work at Biodelta.": "good_morning_my_name_is_erica_i_am_from_sao_paulo.mp3",
  "Good morning. My name is Ana. I am from Brazil. I live in Sao Paulo, in the Pinheiros neighborhood. I work at a small company near my home. My routine starts early. I wake up at six, have breakfast, and start work at eight. My goal this year is to travel to London. I am learning English because it is important for my work and for my trip.": "listening_1_ana_intro.mp3",
  "Hi. I am Carlos. I am from Sao Paulo too. I work at a big company in the city center. My routine is simple. I wake up at seven. I have coffee at home. I drive to work. I finish at one in the afternoon. After work, I practice English at home. My big challenge is pronunciation. But I practice every day, and I feel more comfortable now.": "listening_2_carlos_routine.mp3",
  "My name is Erica. Nice to meet you. I work at a company called Biodelta. I live in Sao Paulo, in Pinheiros. My goal is to speak English with confidence. Challenge accepted!": "order_l1_self_intro.mp3"
};

const davidLines = [
  "Hello! My name is David. I work here at the conference. What is your name?",
  "Nice to meet you, Erica! Where do you work?",
  "That sounds interesting! What is your daily routine like?",
  "Do you have any goals for this year?"
];

const ericaLines = [
  "Hi David! I am Erica. Nice to meet you.",
  "I work at Biodelta. It is a company in Sao Paulo.",
  "I start work early, at eight. I finish at one in the afternoon.",
  "Yes! My goal is to practice English every day. Challenge accepted!"
];

function countWords(t) { return t.trim().split(/\s+/).length; }
let alt = 0;
function getVoice(text) {
  if (davidLines.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  if (ericaLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
  if (text.startsWith("Good morning. My name is Ana")) return { id: ELLEN, name: 'Ellen' };
  if (text.startsWith("Hi. I am Carlos")) return { id: ARTHUR, name: 'Arthur' };
  if (countWords(text) <= 2) return { id: ARTHUR, name: 'Arthur' };
  const v = alt % 2 === 0 ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
  alt++;
  return v;
}

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const options = { hostname: 'api.elevenlabs.io', path: '/v1/text-to-speech/' + voiceId + '?output_format=mp3_44100_128', method: 'POST', headers: { 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY, 'Content-Length': Buffer.byteLength(postData) } };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let b = ''; res.on('data', d => b += d); res.on('end', () => reject(new Error('API ' + res.statusCode + ': ' + b))); return; }
      const chunks = []; res.on('data', c => chunks.push(c)); res.on('end', () => { fs.writeFileSync(outputPath, Buffer.concat(chunks)); resolve(); });
    });
    req.on('error', reject); req.write(postData); req.end();
  });
}

async function main() {
  const entries = Object.entries(audioMap);
  let gen = 0, skip = 0;
  console.log('Generating ' + entries.length + ' audio files for Erica...');
  for (let i = 0; i < entries.length; i++) {
    const [text, file] = entries[i];
    const out = path.join(OUTPUT_DIR, file);
    if (fs.existsSync(out) && fs.statSync(out).size > 1000) {
      skip++;
      if (countWords(text) > 2 && !davidLines.includes(text) && !ericaLines.includes(text)) alt++;
      continue;
    }
    const voice = getVoice(text);
    try {
      await generateAudio(text, voice.id, out);
      gen++;
      console.log(`Generated ${gen+skip}/${entries.length}: ${file} (${voice.name})`);
    } catch (err) { console.error(`FAILED ${file}: ${err.message}`); }
    if (i < entries.length - 1) await new Promise(r => setTimeout(r, 500));
  }
  console.log(`Done! Generated: ${gen}, Skipped: ${skip}`);
}
main().catch(console.error);
