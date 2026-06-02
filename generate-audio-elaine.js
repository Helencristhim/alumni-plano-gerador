const fs = require('fs');
const path = require('path');
const https = require('https');

const ELEVENLABS_API_KEY = process.env.ELEVENLABS_API_KEY;
if (!ELEVENLABS_API_KEY) {
  console.error('ERROR: ELEVENLABS_API_KEY not set');
  process.exit(1);
}

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const OUTPUT_DIR = path.join(__dirname, 'public', 'audio', 'elaine-mieko-pinho');

// AudioMap from the HTML file (lines 10-63)
const audioMap = {
  "Could you repeat that, please?": "could_you_repeat_that_please.mp3",
  "I am not sure I understand. Could you explain?": "i_am_not_sure_i_understand_could_you_explain.mp3",
  "Could you speak more slowly, please?": "could_you_speak_more_slowly_please.mp3",
  "I am not sure how to say this in English.": "i_am_not_sure_how_to_say_this_in_english.mp3",
  "Thank you for your patience.": "thank_you_for_your_patience.mp3",
  "Trip": "trip.mp3",
  "Abroad": "abroad.mp3",
  "Alone": "alone.mp3",
  "Confident": "confident.mp3",
  "Nervous": "nervous.mp3",
  "Manage": "manage.mp3",
  "Check in": "check_in.mp3",
  "Deal with": "deal_with.mp3",
  "I usually travel with my family.": "i_usually_travel_with_my_family.mp3",
  "I want to feel more confident when I travel abroad.": "i_want_to_feel_more_confident_when_i_travel_abroad.mp3",
  "I am not sure how to say what I need at the airport.": "i_am_not_sure_how_to_say_what_i_need_at_the_airport.mp3",
  "I live in a small city in Sao Paulo state.": "i_live_in_a_small_city_in_sao_paulo_state.mp3",
  "My name is Elaine. I am from Brazil.": "my_name_is_elaine_i_am_from_brazil.mp3",
  "I am a lawyer and I manage a company.": "i_am_a_lawyer_and_i_manage_a_company.mp3",
  "I love to travel, but I feel nervous when I need to speak English.": "i_love_to_travel_but_i_feel_nervous_when_i_need_to_speak_eng.mp3",
  "I want to travel alone and feel confident.": "i_want_to_travel_alone_and_feel_confident.mp3",
  "I work as a lawyer in Itatuba.": "i_work_as_a_lawyer_in_itatuba.mp3",
  "I manage a company with my family.": "i_manage_a_company_with_my_family.mp3",
  "I usually travel to Europe and the United States.": "i_usually_travel_to_europe_and_the_united_states.mp3",
  "I want to check in at a hotel by myself.": "i_want_to_check_in_at_a_hotel_by_myself.mp3",
  "I need to learn how to deal with problems when I travel.": "i_need_to_learn_how_to_deal_with_problems_when_i_travel.mp3",
  "Good morning. My name is Elaine Mieko Pinho. I am from Itatuba, a small city in Sao Paulo, Brazil. I am a lawyer and I also manage a family company. I usually travel with my family, but I want to travel alone too. I feel nervous when I need to speak English abroad, but I am not going to give up. I want to feel confident.": "good_morning_my_name_is_elaine_mieko_pinho_i_am_from_itatuba.mp3",
  "Good morning. My name is Elaine.": "good_morning_my_name_is_elaine.mp3",
  "I am from Itatuba, in Sao Paulo.": "i_am_from_itatuba_in_sao_paulo.mp3",
  "I am a lawyer and I manage a company. (v2)": "i_am_a_lawyer_and_i_manage_a_company_v2.mp3",
  "I love traveling, but I feel nervous speaking English.": "i_love_traveling_but_i_feel_nervous_speaking_english.mp3",
  "I want to travel alone and feel confident abroad.": "i_want_to_travel_alone_and_feel_confident_abroad.mp3",
  "Hi! I am Sarah. I work at the front desk. Are you checking in today?": "hi_i_am_sarah_i_work_at_the_front_desk_are_you_checking_in_t.mp3",
  "Yes, I have a reservation. My name is Elaine Pinho.": "yes_i_have_a_reservation_my_name_is_elaine_pinho.mp3",
  "Welcome, Ms. Pinho! Where are you from?": "welcome_ms_pinho_where_are_you_from.mp3",
  "I am from Brazil. I live in a small city called Itatuba.": "i_am_from_brazil_i_live_in_a_small_city_called_itatuba.mp3",
  "How nice! Is this your first trip to New York?": "how_nice_is_this_your_first_trip_to_new_york.mp3",
  "No, I usually travel with my family. But this time I am alone.": "no_i_usually_travel_with_my_family_but_this_time_i_am_alone.mp3",
  "That is brave! Do you need help with anything?": "that_is_brave_do_you_need_help_with_anything.mp3",
  "I am not sure how to say this, but could I get a room with a view?": "i_am_not_sure_how_to_say_this_but_could_i_get_a_room_with_a.mp3",
  "Attention, please. Flight AA 402 to New York is now boarding at Gate 12. All passengers, please have your boarding pass and passport ready.": "attention_please_flight_aa_402_to_new_york_is_now_boarding_at.mp3",
  "Could I have a window seat, please?": "could_i_have_a_window_seat_please.mp3",
  "I would like to check in, please.": "i_would_like_to_check_in_please.mp3",
  "Could you help me find my gate?": "could_you_help_me_find_my_gate.mp3",
  "I am not sure how to say this in English. (v2)": "i_am_not_sure_how_to_say_this_in_english_v2.mp3",
  "I need to deal with a problem with my reservation.": "i_need_to_deal_with_a_problem_with_my_reservation.mp3",
  "I feel nervous, but I am not going to give up.": "i_feel_nervous_but_i_am_not_going_to_give_up.mp3",
  "My name is Elaine. I am from Brazil. (v2)": "my_name_is_elaine_i_am_from_brazil_v2.mp3",
  "I work as a lawyer and I manage a company.": "i_work_as_a_lawyer_and_i_manage_a_company.mp3",
  "I usually travel with my family, but I want to be independent.": "i_usually_travel_with_my_family_but_i_want_to_be_independent.mp3",
  "I feel nervous abroad, but I am learning.": "i_feel_nervous_abroad_but_i_am_learning.mp3",
  "I want to check in at hotels and deal with problems by myself.": "i_want_to_check_in_at_hotels_and_deal_with_problems_by_mysel.mp3"
};

// Dialogue lines by Sarah (female receptionist) - use Ellen
const sarahLines = [
  "Hi! I am Sarah. I work at the front desk. Are you checking in today?",
  "Welcome, Ms. Pinho! Where are you from?",
  "How nice! Is this your first trip to New York?",
  "That is brave! Do you need help with anything?"
];

// Dialogue lines by Elaine (female) - use Ellen
const elaineDialogueLines = [
  "Yes, I have a reservation. My name is Elaine Pinho.",
  "I am from Brazil. I live in a small city called Itatuba.",
  "No, I usually travel with my family. But this time I am alone.",
  "I am not sure how to say this, but could I get a room with a view?"
];

// Announcement line (neutral/male voice)
const announcementLines = [
  "Attention, please. Flight AA 402 to New York is now boarding at Gate 12. All passengers, please have your boarding pass and passport ready."
];

function countWords(text) {
  // Remove (v2) markers for word counting
  const clean = text.replace(/\s*\(v2\)\s*$/, '').trim();
  return clean.split(/\s+/).length;
}

// Track alternation for phrases
let phraseAlternator = 0;

function getVoice(text) {
  // Sarah's lines -> Ellen
  if (sarahLines.includes(text)) return { id: ELLEN, name: 'Ellen' };

  // Elaine's dialogue lines -> Ellen
  if (elaineDialogueLines.includes(text)) return { id: ELLEN, name: 'Ellen' };

  // Announcement -> Arthur
  if (announcementLines.includes(text)) return { id: ARTHUR, name: 'Arthur' };

  const words = countWords(text);

  // Single words (1-2) -> Arthur
  if (words <= 2) return { id: ARTHUR, name: 'Arthur' };

  // Phrases (3+) -> alternate Arthur/Ellen
  const voice = phraseAlternator % 2 === 0
    ? { id: ARTHUR, name: 'Arthur' }
    : { id: ELLEN, name: 'Ellen' };
  phraseAlternator++;
  return voice;
}

function generateAudio(text, voiceId, outputPath) {
  return new Promise((resolve, reject) => {
    // Clean text for TTS (remove version markers)
    const ttsText = text.replace(/\s*\(v2\)\s*$/, '').trim();

    const postData = JSON.stringify({
      text: ttsText,
      model_id: 'eleven_monolingual_v1',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75
      }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}?output_format=mp3_44100_128`,
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'xi-api-key': ELEVENLABS_API_KEY,
        'Content-Length': Buffer.byteLength(postData)
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', (d) => body += d);
        res.on('end', () => reject(new Error(`API ${res.statusCode}: ${body}`)));
        return;
      }

      const chunks = [];
      res.on('data', (chunk) => chunks.push(chunk));
      res.on('end', () => {
        const buffer = Buffer.concat(chunks);
        fs.writeFileSync(outputPath, buffer);
        resolve();
      });
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function delay(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function main() {
  const entries = Object.entries(audioMap);
  const total = entries.length;
  let generated = 0;
  let skipped = 0;

  console.log(`Starting audio generation: ${total} files`);
  console.log(`Output: ${OUTPUT_DIR}\n`);

  for (let i = 0; i < entries.length; i++) {
    const [text, filename] = entries[i];
    const outputPath = path.join(OUTPUT_DIR, filename);

    // Skip if file already exists
    if (fs.existsSync(outputPath)) {
      const stats = fs.statSync(outputPath);
      if (stats.size > 1000) { // Must be > 1KB to be valid
        skipped++;
        console.log(`Skipped ${i + 1}/${total}: ${filename} (already exists, ${stats.size} bytes)`);
        // Still need to advance alternator for consistent voice assignment
        const words = countWords(text);
        if (words > 2 && !sarahLines.includes(text) && !elaineDialogueLines.includes(text) && !announcementLines.includes(text)) {
          phraseAlternator++;
        }
        continue;
      }
    }

    const voice = getVoice(text);

    try {
      await generateAudio(text, voice.id, outputPath);
      generated++;
      console.log(`Generated ${generated}/${total - skipped}: ${filename} (${voice.name})`);
    } catch (err) {
      console.error(`FAILED ${filename}: ${err.message}`);
    }

    // Rate limit delay
    if (i < entries.length - 1) {
      await delay(500);
    }
  }

  console.log(`\nDone! Generated: ${generated}, Skipped: ${skipped}, Total entries: ${total}`);
}

main().catch(console.error);
