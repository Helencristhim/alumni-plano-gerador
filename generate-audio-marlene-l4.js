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
  "Beautiful": "/audio/marlene-landucci/beautiful.mp3",
  "Famous": "/audio/marlene-landucci/famous.mp3",
  "Crowded": "/audio/marlene-landucci/crowded.mp3",
  "Quiet": "/audio/marlene-landucci/quiet.mp3",
  "Modern": "/audio/marlene-landucci/modern.mp3",
  "Ancient": "/audio/marlene-landucci/ancient.mp3",
  "Friendly": "/audio/marlene-landucci/friendly.mp3",
  "Delicious": "/audio/marlene-landucci/delicious.mp3",
  "Rome is a beautiful city.": "/audio/marlene-landucci/rome_is_a_beautiful_city.mp3",
  "The Colosseum is very famous.": "/audio/marlene-landucci/the_colosseum_is_very_famous.mp3",
  "The streets are crowded in the morning.": "/audio/marlene-landucci/the_streets_are_crowded_in_the_morning.mp3",
  "My hotel is quiet and comfortable.": "/audio/marlene-landucci/my_hotel_is_quiet_and_comfortable.mp3",
  "Istanbul is a modern and ancient city.": "/audio/marlene-landucci/istanbul_is_a_modern_and_ancient_city.mp3",
  "The people are very friendly.": "/audio/marlene-landucci/the_people_are_very_friendly.mp3",
  "The food in Italy is delicious.": "/audio/marlene-landucci/the_food_in_italy_is_delicious.mp3",
  "There is a beautiful park near my hotel.": "/audio/marlene-landucci/there_is_a_beautiful_park_near_my_hotel.mp3",
  "There are many restaurants on this street.": "/audio/marlene-landucci/there_are_many_restaurants_on_this_street.mp3",
  "There is a big museum in the city center.": "/audio/marlene-landucci/there_is_a_big_museum_in_the_city_center.mp3",
  "Is there a pharmacy near here?": "/audio/marlene-landucci/is_there_a_pharmacy_near_here.mp3",
  "Are there any good restaurants nearby?": "/audio/marlene-landucci/are_there_any_good_restaurants_nearby.mp3",
  "There are two famous bridges in the city.": "/audio/marlene-landucci/there_are_two_famous_bridges_in_the_city.mp3",
  "Excuse me, is there a supermarket near here?": "/audio/marlene-landucci/excuse_me_is_there_a_supermarket_near_here.mp3",
  "Yes, there is one on the next street. It is very big.": "/audio/marlene-landucci/yes_there_is_one_on_the_next_street.mp3",
  "Are there any good cafes around here?": "/audio/marlene-landucci/are_there_any_good_cafes_around_here.mp3",
  "There are three cafes on this street. The one on the corner is very popular.": "/audio/marlene-landucci/there_are_three_cafes_on_this_street.mp3",
  "What is the city like?": "/audio/marlene-landucci/what_is_the_city_like.mp3",
  "It is beautiful and very old. The buildings are ancient.": "/audio/marlene-landucci/it_is_beautiful_and_very_old.mp3",
  "Is it crowded?": "/audio/marlene-landucci/is_it_crowded.mp3",
  "Yes, the center is crowded, but the parks are quiet.": "/audio/marlene-landucci/yes_the_center_is_crowded.mp3",
  "The hotel is comfortable and modern.": "/audio/marlene-landucci/the_hotel_is_comfortable_and_modern.mp3",
  "São Paulo is a big and modern city.": "/audio/marlene-landucci/sao_paulo_is_a_big_and_modern_city.mp3",
  "Vila Nova Conceição is quiet and beautiful.": "/audio/marlene-landucci/vila_nova_conceicao_is_quiet_and_beautiful.mp3",
  "[order-l4]": "/audio/marlene-landucci/order_l4_ordering.mp3",
  "[lp-listen-l4-1]": "/audio/marlene-landucci/lp_listen_l4_1_city_description.mp3",
  "[lp-listen-l4-2]": "/audio/marlene-landucci/lp_listen_l4_2_hotel_review.mp3",
  "There is a nice restaurant near the hotel.": "/audio/marlene-landucci/there_is_a_nice_restaurant_near_the_hotel.mp3",
  "The city is old but very interesting.": "/audio/marlene-landucci/the_city_is_old_but_very_interesting.mp3"
};

// Ellen = Marlene's voice (female protagonist)
const ellenPhrases = new Set([
  "Rome is a beautiful city.",
  "My hotel is quiet and comfortable.",
  "The people are very friendly.",
  "There is a beautiful park near my hotel.",
  "Is there a pharmacy near here?",
  "Are there any good restaurants nearby?",
  "Excuse me, is there a supermarket near here?",
  "Are there any good cafes around here?",
  "What is the city like?",
  "Is it crowded?",
  "São Paulo is a big and modern city.",
  "Vila Nova Conceição is quiet and beautiful.",
  "There is a nice restaurant near the hotel.",
  "[order-l4]",
  "[lp-listen-l4-1]",
]);

// Anna's lines (female character) = Riley-like but using Ellen for consistency
const annaPhrases = new Set([
  "Yes, there is one on the next street. It is very big.",
  "There are three cafes on this street. The one on the corner is very popular.",
  "It is beautiful and very old. The buildings are ancient.",
  "Yes, the center is crowded, but the parks are quiet.",
]);

let phraseAlternator = false;

function getVoice(text) {
  const wordCount = text.trim().split(/\s+/).length;
  if (wordCount <= 2) return { id: ELLEN, name: 'Ellen' };
  if (ellenPhrases.has(text)) return { id: ELLEN, name: 'Ellen' };
  if (annaPhrases.has(text)) return { id: ELLEN, name: 'Ellen' };
  if (text === '[lp-listen-l4-2]') return { id: ARTHUR, name: 'Arthur' };
  phraseAlternator = !phraseAlternator;
  return phraseAlternator ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  let actualText = text;
  if (text === '[lp-listen-l4-1]') {
    actualText = "Welcome to Rome! Rome is a beautiful and ancient city. There are many famous buildings. The Colosseum is very famous. It is very old. The streets are crowded in the morning, but the parks are quiet. There are many delicious restaurants near the center. The people are very friendly. If you visit Rome, there is a beautiful park near the Trevi Fountain. The food is delicious. Rome is modern and ancient at the same time.";
  } else if (text === '[lp-listen-l4-2]') {
    actualText = "I am staying at the Grand Hotel in Rome. The hotel is very modern and comfortable. My room is quiet. There is a big bed and a beautiful view of the city. The bathroom is modern and clean. There is a nice restaurant in the hotel. The food is delicious. The staff are very friendly. There are two swimming pools. The hotel is in the city center, so there are many shops and cafes nearby. I love this hotel!";
  } else if (text === '[order-l4]') {
    actualText = "Marlene arrives in Rome. The city is beautiful. She goes to her hotel. The hotel is quiet and modern. She walks to the Colosseum. It is very famous and ancient. The streets are crowded. She stops at a restaurant. The food is delicious. The people are very friendly.";
  }

  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: actualText,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });
    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(postData) }
    };
    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) { let body = ''; res.on('data', d => body += d); res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${body}`))); return; }
      const chunks = []; res.on('data', chunk => chunks.push(chunk)); res.on('end', () => resolve(Buffer.concat(chunks)));
    });
    req.on('error', reject); req.write(postData); req.end();
  });
}

async function main() {
  if (!fs.existsSync(AUDIO_DIR)) fs.mkdirSync(AUDIO_DIR, { recursive: true });
  const entries = Object.entries(audioMap);
  let generated = 0, skipped = 0, errors = 0;
  for (const [text, filePath] of entries) {
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
