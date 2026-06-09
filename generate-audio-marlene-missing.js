const fs = require('fs');
const path = require('path');
const https = require('https');
const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY'); process.exit(1); }
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';

// All 37 missing phrases with voice assignment
const missing = [
  // L4/L5 survival/slides - Marlene protagonist = Ellen
  { text: "There is a park near my hotel.", voice: ELLEN, file: "there_is_a_park_near_my_hotel_v2.mp3" },
  { text: "There are many restaurants in Rome.", voice: ELLEN, file: "there_are_many_restaurants_in_rome.mp3" },
  { text: "The city is very beautiful.", voice: ELLEN, file: "the_city_is_very_beautiful.mp3" },
  { text: "The people are friendly.", voice: ELLEN, file: "the_people_are_friendly_short.mp3" },
  { text: "There are many restaurants.", voice: ELLEN, file: "there_are_many_restaurants_short.mp3" },
  { text: "I usually wake up at six.", voice: ELLEN, file: "i_usually_wake_up_at_six_short.mp3" },
  { text: "My flight is at half past two.", voice: ELLEN, file: "my_flight_is_at_half_past_two_short.mp3" },
  { text: "The gate number is twelve.", voice: ARTHUR, file: "the_gate_number_is_twelve.mp3" },
  { text: "Rome is beautiful and ancient.", voice: ELLEN, file: "rome_is_beautiful_and_ancient_short.mp3" },
  // L6 survival cards
  { text: "Could I have a window seat?", voice: ELLEN, file: "could_i_have_a_window_seat_short.mp3" },
  { text: "I would like to check in.", voice: ELLEN, file: "i_would_like_to_check_in_short.mp3" },
  { text: "Here is my passport.", voice: ELLEN, file: "here_is_my_passport_short.mp3" },
  { text: "Could you help me with my bag?", voice: ELLEN, file: "could_you_help_me_with_my_bag_short.mp3" },
  { text: "Sao Paulo is a big and modern city.", voice: ELLEN, file: "sao_paulo_is_a_big_and_modern_city_v2.mp3" },
  // L5 Dialogue (David) - alternating voices
  { text: "Hello! I am David. I am from London. Are you traveling alone?", voice: ARTHUR, file: "hello_i_am_david_from_london.mp3" },
  { text: "Hi David! I am Marlene. I am from Brazil. Yes, this is my first trip alone!", voice: ELLEN, file: "hi_david_i_am_marlene_first_trip.mp3" },
  { text: "How wonderful! What do you do in Brazil?", voice: ARTHUR, file: "how_wonderful_what_do_you_do.mp3" },
  { text: "I manage properties. I usually wake up at six and check my schedule.", voice: ELLEN, file: "i_manage_properties_wake_up_six.mp3" },
  { text: "That sounds busy! How is Rome so far?", voice: ARTHUR, file: "that_sounds_busy_how_is_rome.mp3" },
  { text: "Rome is beautiful and ancient! There are many amazing restaurants.", voice: ELLEN, file: "rome_is_beautiful_ancient_restaurants.mp3" },
  { text: "I agree! What time is your flight back?", voice: ARTHUR, file: "i_agree_what_time_flight_back.mp3" },
  { text: "My flight is at half past two on Sunday. Gate B7!", voice: ELLEN, file: "my_flight_half_past_two_sunday.mp3" },
  // L6 Dialogue (agent)
  { text: "Good morning! Welcome to Alitalia. Could I see your passport, please?", voice: ARTHUR, file: "good_morning_welcome_alitalia.mp3" },
  { text: "Good morning! Here is my passport. I would like to check in for the flight to Rome.", voice: ELLEN, file: "good_morning_here_is_my_passport.mp3" },
  { text: "Of course. How many pieces of luggage do you have?", voice: ARTHUR, file: "of_course_how_many_luggage.mp3" },
  { text: "I have one suitcase and one carry-on bag.", voice: ELLEN, file: "i_have_one_suitcase_one_carry_on.mp3" },
  { text: "Would you like an aisle seat or a window seat?", voice: ARTHUR, file: "would_you_like_aisle_or_window.mp3" },
  { text: "Here is your boarding pass. Your departure is at Gate B5 at 10:30.", voice: ARTHUR, file: "here_is_boarding_pass_gate_b5.mp3" },
  { text: "Thank you so much! Gate B5 at 10:30. Got it!", voice: ELLEN, file: "thank_you_gate_b5_got_it.mp3" },
  // L7 Dialogue (flight attendant)
  { text: "Good afternoon! Welcome aboard. Please put your bag in the overhead compartment and fasten your seatbelt.", voice: ARTHUR, file: "good_afternoon_welcome_aboard.mp3" },
  { text: "Thank you! Can I have a blanket, please? It is cold.", voice: ELLEN, file: "thank_you_can_i_have_blanket_cold.mp3" },
  { text: "Of course! Here you go. Would you like headphones for the movie?", voice: ARTHUR, file: "of_course_here_you_go_headphones.mp3" },
  { text: "Yes, please! Can I have headphones?", voice: ELLEN, file: "yes_please_can_i_have_headphones.mp3" },
  { text: "Here you are. We will be serving a snack soon. Please fold down your tray table.", voice: ARTHUR, file: "here_you_are_snack_soon_tray_table.mp3" },
  { text: "Can I have a snack and some juice, please?", voice: ELLEN, file: "can_i_have_snack_and_juice.mp3" },
  { text: "Attention, passengers. We are experiencing some turbulence. Please fasten your seatbelt.", voice: ARTHUR, file: "attention_passengers_turbulence.mp3" },
  { text: "OK! Could you tell me when we are landing?", voice: ELLEN, file: "ok_could_you_tell_me_landing.mp3" },
];

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const d = JSON.stringify({ text, model_id: 'eleven_monolingual_v1', voice_settings: { stability: 0.5, similarity_boost: 0.75 } });
    const o = { hostname: 'api.elevenlabs.io', path: `/v1/text-to-speech/${voiceId}`, method: 'POST', headers: { 'Accept': 'audio/mpeg', 'Content-Type': 'application/json', 'xi-api-key': API_KEY, 'Content-Length': Buffer.byteLength(d) } };
    const req = https.request(o, (res) => {
      if (res.statusCode !== 200) { let b = ''; res.on('data', x => b += x); res.on('end', () => reject(new Error(`HTTP ${res.statusCode}: ${b}`))); return; }
      const c = []; res.on('data', x => c.push(x)); res.on('end', () => resolve(Buffer.concat(c)));
    }); req.on('error', reject); req.write(d); req.end();
  });
}

async function main() {
  const dir = path.join(BASE_DIR, 'audio/marlene-landucci');
  let gen = 0, skip = 0;
  const audioMapEntries = [];
  for (const { text, voice, file } of missing) {
    const fp = path.join(dir, file);
    const mapPath = `/audio/marlene-landucci/${file}`;
    audioMapEntries.push(`  "${text}": "${mapPath}"`);
    if (fs.existsSync(fp)) { skip++; continue; }
    const vName = voice === ELLEN ? 'Ellen' : 'Arthur';
    console.log(`GEN [${vName}]: "${text.substring(0,50)}..." → ${file}`);
    try { fs.writeFileSync(fp, await generateAudio(text, voice)); gen++; await new Promise(r => setTimeout(r, 500)); }
    catch (e) { console.error(`ERR: ${e.message}`); }
  }
  console.log(`\nDone! Gen:${gen} Skip:${skip}`);
  console.log('\n=== ADD TO AUDIOMAP ===');
  console.log(audioMapEntries.join(',\n'));
}
main();
