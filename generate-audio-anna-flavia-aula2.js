const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'anna-flavia-miranda-da-silva');

const audioMap = {
  "Wake Up": "aula2_wake_up.mp3",
  "Commute": "aula2_commute.mp3",
  "Schedule": "aula2_schedule.mp3",
  "Lunch Break": "aula2_lunch_break.mp3",
  "Report": "aula2_report.mp3",
  "Check": "aula2_check.mp3",
  "Leave": "aula2_leave.mp3",
  "Deadline": "aula2_deadline.mp3",
  "I wake up at six thirty every day.": "aula2_i_wake_up.mp3",
  "I commute to the office by car.": "aula2_i_commute.mp3",
  "I check my schedule every morning.": "aula2_i_check_schedule.mp3",
  "I have a lunch break at noon.": "aula2_i_have_lunch.mp3",
  "I write reports in the afternoon.": "aula2_i_write_reports.mp3",
  "I check the export numbers every week.": "aula2_i_check_export.mp3",
  "I leave the office at six.": "aula2_i_leave.mp3",
  "I do not work on weekends.": "aula2_i_dont_work.mp3",
  "Do you work on Saturdays?": "aula2_do_you_work.mp3",
  "She does not commute by bus.": "aula2_she_doesnt.mp3",
  "What time do you wake up?": "aula2_what_time.mp3",
  "I usually check my emails first.": "aula2_usually_check.mp3",
  "Good morning, Anna Flavia! How is your day going?": "aula2_dial_carlos_1.mp3",
  "Good morning, Carlos! I am good, thank you. I woke up early today.": "aula2_dial_anna_1.mp3",
  "What time do you usually wake up?": "aula2_dial_carlos_2.mp3",
  "I usually wake up at six thirty. I commute to the office by car.": "aula2_dial_anna_2.mp3",
  "Do you check your emails first thing in the morning?": "aula2_dial_carlos_3.mp3",
  "Yes, I always check my emails and my schedule before the first meeting.": "aula2_dial_anna_3.mp3",
  "Do you work on weekends?": "aula2_dial_carlos_4.mp3",
  "No, I do not work on weekends. I relax and spend time with my family.": "aula2_dial_anna_4.mp3",
  "My name is Anna Flavia. I work at Usina Cururique. I wake up at six thirty every morning. I commute to the office by car. I check my schedule and emails first. I have meetings in the morning. In the afternoon, I write reports and check the export numbers. I leave the office at six. I do not work on weekends.": "aula2_listening.mp3",
  "I wake up at six thirty.": "aula2_surv_wake.mp3",
  "I do not work on weekends.": "aula2_surv_dont.mp3",
  "What time do you leave the office?": "aula2_surv_whattime.mp3",
  "I usually have lunch at noon.": "aula2_surv_lunch.mp3",
  "Do you have a meeting today?": "aula2_surv_meeting.mp3",
  "I wake up at six thirty and commute to the office.": "aula2_speech_1.mp3",
  "I check my emails and write reports every day.": "aula2_speech_2.mp3",
  "I do not work on weekends. I relax at home.": "aula2_speech_3.mp3",
  "She commutes to the office by car.": "aula2_fill_commute.mp3",
  "I check my emails every morning.": "aula2_fill_check.mp3",
  "I do not work on weekends.": "aula2_fill_work.mp3",
  "Do you have a meeting today?": "aula2_fill_do.mp3",
  "She does not commute by bus.": "aula2_fill_does.mp3",
  "I usually wake up at six thirty.": "aula2_oral_wake.mp3",
  "What time do you leave the office?": "aula2_oral_leave.mp3",
  "Do you check your emails in the morning?": "aula2_oral_check.mp3",
  "I write reports and check the export numbers.": "aula2_oral_reports.mp3",
  "I wake up at six thirty. I commute to the office. I check my schedule. I have lunch at noon. I leave at six.": "aula2_order.mp3"
};

const carlosLines = [
  "Good morning, Anna Flavia! How is your day going?",
  "What time do you usually wake up?",
  "Do you check your emails first thing in the morning?",
  "Do you work on weekends?"
];

const annaLines = [
  "Good morning, Carlos! I am good, thank you. I woke up early today.",
  "I usually wake up at six thirty. I commute to the office by car.",
  "Yes, I always check my emails and my schedule before the first meeting.",
  "No, I do not work on weekends. I relax and spend time with my family."
];

function countWords(t) { return t.trim().split(/\s+/).length; }
let alt = 0;
function getVoice(text) {
  if (carlosLines.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  if (annaLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
  if (countWords(text) <= 2) return { id: ELLEN, name: 'Ellen' };
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
  console.log('Generating ' + entries.length + ' Aula 2 audio files...');
  for (let i = 0; i < entries.length; i++) {
    const [text, file] = entries[i];
    const out = path.join(OUTPUT_DIR, file);
    if (fs.existsSync(out) && fs.statSync(out).size > 1000) { skip++; if (countWords(text) > 2 && !carlosLines.includes(text) && !annaLines.includes(text)) alt++; continue; }
    const voice = getVoice(text);
    try { await generateAudio(text, voice.id, out); gen++; console.log(`Generated ${gen+skip}/${entries.length}: ${file} (${voice.name})`); }
    catch (err) { console.error(`FAILED ${file}: ${err.message}`); }
    if (i < entries.length - 1) await new Promise(r => setTimeout(r, 500));
  }
  console.log(`Done! Generated: ${gen}, Skipped: ${skip}`);
}
main().catch(console.error);
