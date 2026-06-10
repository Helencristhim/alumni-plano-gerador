const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) { console.error('ERROR: ELEVENLABS_API_KEY not set'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'anna-flavia-miranda-da-silva');

if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const audioMap = {
  "Could you repeat that, please?": "could_you_repeat_that_please.mp3",
  "I am not sure I understand. Could you explain?": "i_am_not_sure_i_understand.mp3",
  "Let me think about that for a moment.": "let_me_think_about_that.mp3",
  "That is a great question.": "that_is_a_great_question.mp3",
  "In my experience, I would say...": "in_my_experience.mp3",
  "Work": "work.mp3",
  "Company": "company.mp3",
  "Office": "office.mp3",
  "Financial": "financial.mp3",
  "Sugar": "sugar.mp3",
  "Export": "export.mp3",
  "Meeting": "meeting.mp3",
  "Partner": "partner.mp3",
  "I work at Usina Cururique.": "i_work_at_usina_cururique.mp3",
  "My company exports sugar.": "my_company_exports_sugar.mp3",
  "The office is in Sao Paulo.": "the_office_is_in_sao_paulo.mp3",
  "I work in the financial area.": "i_work_in_the_financial_area.mp3",
  "Brazil exports sugar.": "brazil_exports_sugar.mp3",
  "We export sugar.": "we_export_sugar.mp3",
  "I have a meeting today.": "i_have_a_meeting_today.mp3",
  "Our partners are international.": "our_partners_are_international.mp3",
  "Hi! Welcome to the Sao Paulo office. I am Carlos.": "dial_carlos_1.mp3",
  "Hi Carlos! I am Anna Flavia. Nice to meet you.": "dial_anna_1.mp3",
  "Nice to meet you too! Where are you from?": "dial_carlos_2.mp3",
  "I am from Minas Gerais. I work at the Cururique plant.": "dial_anna_2.mp3",
  "What do you do at Cururique?": "dial_carlos_3.mp3",
  "I work in the financial area. We export sugar.": "dial_anna_3.mp3",
  "That is interesting! We have a meeting at three. Would you like to join?": "dial_carlos_4.mp3",
  "Yes, I would love to! Thank you, Carlos.": "dial_anna_4.mp3",
  "Hello everyone. My name is Anna Flavia. I am from Minas Gerais. I work at Usina Cururique in the financial area. Our company exports sugar to many countries. I am happy to be here at the Sao Paulo office. I am looking forward to working with all of you.": "listening_intro.mp3",
  "My name is Anna Flavia.": "surv_my_name.mp3",
  "I work at Usina Cururique.": "surv_i_work.mp3",
  "Nice to meet you.": "surv_nice_to_meet.mp3",
  "I am from Minas Gerais.": "surv_i_am_from.mp3",
  "Hi, I am Anna Flavia. Nice to meet you.": "speech_1.mp3",
  "I work in the financial area at Usina Cururique.": "speech_2.mp3",
  "We export sugar to many countries.": "speech_3.mp3",
  "She works in the financial area.": "fill_she_works.mp3",
  "We export sugar to other countries.": "fill_we_export.mp3",
  "My name is Anna Flavia": "fill_my_name.mp3",
  "The office is in Sao Paulo": "fill_the_office.mp3",
  "Our company exports sugar.": "fill_our_company.mp3",
  "Nice to meet you too!": "nice_to_meet_you_too.mp3",
  "Anna Flavia works at Usina Cururique. She is from Minas Gerais. She works in the financial area. Her company exports sugar to many countries. She has a meeting with her partners today.": "grammar_context.mp3",
  "Hi, I am Anna Flavia. I am from Minas Gerais. I work at Usina Cururique. We export sugar. Nice to meet you.": "order_l1.mp3"
};

// Carlos lines = Arthur voice
const carlosLines = [
  "Hi! Welcome to the Sao Paulo office. I am Carlos.",
  "Nice to meet you too! Where are you from?",
  "What do you do at Cururique?",
  "That is interesting! We have a meeting at three. Would you like to join?"
];

// Anna Flavia lines = Ellen voice (student is female)
const annaLines = [
  "Hi Carlos! I am Anna Flavia. Nice to meet you.",
  "I am from Minas Gerais. I work at the Cururique plant.",
  "I work in the financial area. We export sugar.",
  "Yes, I would love to! Thank you, Carlos."
];

function countWords(t) { return t.trim().split(/\s+/).length; }
let alt = 0;
function getVoice(text) {
  if (carlosLines.includes(text)) return { id: ARTHUR, name: 'Arthur' };
  if (annaLines.includes(text)) return { id: ELLEN, name: 'Ellen' };
  // Single words = Ellen (student is female)
  if (countWords(text) <= 2) return { id: ELLEN, name: 'Ellen' };
  // Alternate for general phrases
  const v = alt % 2 === 0 ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
  alt++;
  return v;
}

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ text: text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const options = {
      hostname: 'api.elevenlabs.io',
      path: '/v1/text-to-speech/' + voiceId + '?output_format=mp3_44100_128',
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'xi-api-key': ELEVENLABS_API_KEY, 'Content-Length': Buffer.byteLength(postData) }
    };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let b = ''; res.on('data', d => b += d); res.on('end', () => reject(new Error('API ' + res.statusCode + ': ' + b))); return; }
      const chunks = [];
      res.on('data', c => chunks.push(c));
      res.on('end', () => { fs.writeFileSync(outputPath, Buffer.concat(chunks)); resolve(); });
    });
    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

async function main() {
  const entries = Object.entries(audioMap);
  let gen = 0, skip = 0;
  console.log('Generating ' + entries.length + ' audio files for Anna Flávia...');
  for (let i = 0; i < entries.length; i++) {
    const [text, file] = entries[i];
    const out = path.join(OUTPUT_DIR, file);
    if (fs.existsSync(out) && fs.statSync(out).size > 1000) {
      skip++;
      if (countWords(text) > 2 && !carlosLines.includes(text) && !annaLines.includes(text)) alt++;
      continue;
    }
    const voice = getVoice(text);
    try {
      await generateAudio(text, voice.id, out);
      gen++;
      console.log('Generated ' + (gen + skip) + '/' + entries.length + ': ' + file + ' (' + voice.name + ')');
    } catch (err) { console.error('FAILED ' + file + ': ' + err.message); }
    if (i < entries.length - 1) await new Promise(r => setTimeout(r, 500));
  }
  console.log('Done! Generated: ' + gen + ', Skipped: ' + skip);
}
main().catch(console.error);
