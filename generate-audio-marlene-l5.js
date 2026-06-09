const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY env variable'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';
const AUDIO_DIR = path.join(BASE_DIR, 'audio/marlene-landucci');

const audioMap = {
  "My name is Marlene. I am from Brazil. I manage properties.": "/audio/marlene-landucci/my_name_is_marlene_i_am_from_brazil_i_manage.mp3",
  "I usually wake up at six. I always have coffee.": "/audio/marlene-landucci/i_usually_wake_up_at_six_i_always_have_coffee.mp3",
  "My flight is at half past two. Gate fourteen.": "/audio/marlene-landucci/my_flight_is_at_half_past_two_gate_fourteen.mp3",
  "Rome is beautiful and ancient. The people are friendly.": "/audio/marlene-landucci/rome_is_beautiful_and_ancient_the_people.mp3",
  "There is a nice cafe near my hotel.": "/audio/marlene-landucci/there_is_a_nice_cafe_near_my_hotel.mp3",
  "Hi, I am Marlene. I am from São Paulo, Brazil.": "/audio/marlene-landucci/hi_i_am_marlene_i_am_from_sao_paulo.mp3",
  "Nice to meet you! Where are you from?": "/audio/marlene-landucci/nice_to_meet_you_where_are_you_from.mp3",
  "I am David. I am from London, England.": "/audio/marlene-landucci/i_am_david_i_am_from_london.mp3",
  "What do you do?": "/audio/marlene-landucci/what_do_you_do.mp3",
  "I manage properties. What about you?": "/audio/marlene-landucci/i_manage_properties_what_about_you.mp3",
  "I am a teacher. I teach math.": "/audio/marlene-landucci/i_am_a_teacher_i_teach_math.mp3",
  "What is London like?": "/audio/marlene-landucci/what_is_london_like.mp3",
  "It is big and modern. There are many famous buildings.": "/audio/marlene-landucci/it_is_big_and_modern_there_are_many_famous.mp3",
  "Do you usually travel alone?": "/audio/marlene-landucci/do_you_usually_travel_alone.mp3",
  "Sometimes. This is my first solo trip!": "/audio/marlene-landucci/sometimes_this_is_my_first_solo_trip.mp3",
  "[order-l5]": "/audio/marlene-landucci/order_l5_ordering.mp3",
  "[lp-listen-l5-1]": "/audio/marlene-landucci/lp_listen_l5_1_self_intro_review.mp3",
  "[lp-listen-l5-2]": "/audio/marlene-landucci/lp_listen_l5_2_city_description_review.mp3",
  "I am Brazilian. I live in São Paulo.": "/audio/marlene-landucci/i_am_brazilian_i_live_in_sao_paulo.mp3",
  "She always wakes up early and has coffee.": "/audio/marlene-landucci/she_always_wakes_up_early_and_has_coffee.mp3",
  "The flight is at a quarter to three.": "/audio/marlene-landucci/the_flight_is_at_a_quarter_to_three.mp3",
  "There are many beautiful places in Rome.": "/audio/marlene-landucci/there_are_many_beautiful_places_in_rome.mp3",
  "How much is a cappuccino?": "/audio/marlene-landucci/how_much_is_a_cappuccino.mp3",
  "It is four dollars and fifty cents.": "/audio/marlene-landucci/it_is_four_dollars_and_fifty_cents.mp3"
};

const ellenPhrases = new Set([
  "My name is Marlene. I am from Brazil. I manage properties.",
  "I usually wake up at six. I always have coffee.",
  "My flight is at half past two. Gate fourteen.",
  "Rome is beautiful and ancient. The people are friendly.",
  "There is a nice cafe near my hotel.",
  "Hi, I am Marlene. I am from São Paulo, Brazil.",
  "Nice to meet you! Where are you from?",
  "What do you do?",
  "I manage properties. What about you?",
  "What is London like?",
  "Do you usually travel alone?",
  "Sometimes. This is my first solo trip!",
  "I am Brazilian. I live in São Paulo.",
  "How much is a cappuccino?",
  "There are many beautiful places in Rome.",
  "[order-l5]",
  "[lp-listen-l5-1]",
]);

const arthurPhrases = new Set([
  "I am David. I am from London, England.",
  "I am a teacher. I teach math.",
  "It is big and modern. There are many famous buildings.",
]);

let alt = false;
function getVoice(text) {
  if (text.trim().split(/\s+/).length <= 2) return { id: ELLEN, name: 'Ellen' };
  if (ellenPhrases.has(text)) return { id: ELLEN, name: 'Ellen' };
  if (arthurPhrases.has(text)) return { id: ARTHUR, name: 'Arthur' };
  if (text === '[lp-listen-l5-2]') return { id: ARTHUR, name: 'Arthur' };
  alt = !alt;
  return alt ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  let actualText = text;
  if (text === '[lp-listen-l5-1]') {
    actualText = "Hi everyone! My name is Sofia. I am from Argentina. I am a doctor. I usually wake up at seven. I always have tea for breakfast. I sometimes exercise before work. My schedule is very busy. I am traveling to Rome for vacation. My flight is at half past three. I love to travel! Rome is a beautiful city. The food is delicious and the people are very friendly.";
  } else if (text === '[lp-listen-l5-2]') {
    actualText = "Welcome to our city guide. Today we are talking about Istanbul. Istanbul is a very famous city in Turkey. It is modern and ancient at the same time. The streets are crowded but the parks are quiet. There are many beautiful mosques. The food is delicious, especially the kebabs. There is a famous market called the Grand Bazaar. The people are very friendly. A cup of Turkish tea costs about two dollars. Istanbul is a wonderful place to visit.";
  } else if (text === '[order-l5]') {
    actualText = "Hi, I am Marlene. I am from Brazil. I manage properties. I usually wake up at six. I always have coffee. My flight to Rome is at half past two. Gate fourteen. Rome is beautiful and ancient. The people are friendly. There is a nice cafe near my hotel.";
  }
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({ text: actualText, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const options = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voiceId}`, method: 'POST', headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(postData) } };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let body = ''; res.on('data', d => body += d); res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`))); return; }
      const chunks = []; res.on('data', chunk => chunks.push(chunk)); res.on('end', () => resolve(Buffer.concat(chunks)));
    });
    req.on('error', reject); req.write(postData); req.end();
  });
}

async function main() {
  if (!fs.existsSync(AUDIO_DIR)) fs.mkdirSync(AUDIO_DIR, { recursive: true });
  let generated = 0, skipped = 0, errors = 0;
  for (const [text, filePath] of Object.entries(audioMap)) {
    const fullPath = path.join(BASE_DIR, filePath);
    if (fs.existsSync(fullPath)) { console.log(`SKIP: ${filePath}`); skipped++; continue; }
    const voice = getVoice(text);
    console.log(`GEN [${voice.name}]: "${text.substring(0, 50)}..." → ${filePath}`);
    try {
      const buffer = await generateAudio(text, voice.id);
      fs.writeFileSync(fullPath, buffer);
      generated++;
      await new Promise(r => setTimeout(r, 500));
    } catch (err) { console.error(`ERROR: ${text} — ${err.message}`); errors++; }
  }
  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Errors: ${errors}`);
}
main();
