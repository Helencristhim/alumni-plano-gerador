const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('ERROR: Set ELEVENLABS_API_KEY env variable'); process.exit(1); }

const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';

const BASE_DIR = '/Users/helenmendes/alumni-plano-gerador/public';
const AUDIO_DIR = path.join(BASE_DIR, 'audio/elaine-mieko-pinho');

// Full audioMap from professor file
const audioMap = {
  "Could you repeat that, please?": "/audio/elaine-mieko-pinho/could_you_repeat_that_please.mp3",
  "I am not sure I understand. Could you explain?": "/audio/elaine-mieko-pinho/i_am_not_sure_i_understand_could_you_explain.mp3",
  "Could you speak more slowly, please?": "/audio/elaine-mieko-pinho/could_you_speak_more_slowly_please.mp3",
  "I am not sure how to say this in English.": "/audio/elaine-mieko-pinho/i_am_not_sure_how_to_say_this_in_english.mp3",
  "Thank you for your patience.": "/audio/elaine-mieko-pinho/thank_you_for_your_patience.mp3",
  "Trip": "/audio/elaine-mieko-pinho/trip.mp3",
  "Abroad": "/audio/elaine-mieko-pinho/abroad.mp3",
  "Alone": "/audio/elaine-mieko-pinho/alone.mp3",
  "Confident": "/audio/elaine-mieko-pinho/confident.mp3",
  "Nervous": "/audio/elaine-mieko-pinho/nervous.mp3",
  "Manage": "/audio/elaine-mieko-pinho/manage.mp3",
  "Check in": "/audio/elaine-mieko-pinho/check_in.mp3",
  "Deal with": "/audio/elaine-mieko-pinho/deal_with.mp3",
  "I usually travel with my family.": "/audio/elaine-mieko-pinho/i_usually_travel_with_my_family.mp3",
  "I want to feel more confident when I travel abroad.": "/audio/elaine-mieko-pinho/i_want_to_feel_more_confident_when_i_travel_abroad.mp3",
  "I am not sure how to say what I need at the airport.": "/audio/elaine-mieko-pinho/i_am_not_sure_how_to_say_what_i_need_at_the_airport.mp3",
  "I live in a small city in Sao Paulo state.": "/audio/elaine-mieko-pinho/i_live_in_a_small_city_in_sao_paulo_state.mp3",
  "My name is Elaine. I am from Brazil.": "/audio/elaine-mieko-pinho/my_name_is_elaine_i_am_from_brazil.mp3",
  "I am a lawyer and I manage a company.": "/audio/elaine-mieko-pinho/i_am_a_lawyer_and_i_manage_a_company.mp3",
  "I love to travel, but I feel nervous when I need to speak English.": "/audio/elaine-mieko-pinho/i_love_to_travel_but_i_feel_nervous_when_i_need_to_speak_eng.mp3",
  "I want to travel alone and feel confident.": "/audio/elaine-mieko-pinho/i_want_to_travel_alone_and_feel_confident.mp3",
  "I work as a lawyer in Itatuba.": "/audio/elaine-mieko-pinho/i_work_as_a_lawyer_in_itatuba.mp3",
  "I manage a company with my family.": "/audio/elaine-mieko-pinho/i_manage_a_company_with_my_family.mp3",
  "I usually travel to Europe and the United States.": "/audio/elaine-mieko-pinho/i_usually_travel_to_europe_and_the_united_states.mp3",
  "I want to check in at a hotel by myself.": "/audio/elaine-mieko-pinho/i_want_to_check_in_at_a_hotel_by_myself.mp3",
  "I need to learn how to deal with problems when I travel.": "/audio/elaine-mieko-pinho/i_need_to_learn_how_to_deal_with_problems_when_i_travel.mp3",
  "Good morning. My name is Elaine Mieko Pinho. I am from Itatuba, a small city in Sao Paulo, Brazil. I am a lawyer and I also manage a family company. I usually travel with my family, but I want to travel alone too. I feel nervous when I need to speak English abroad, but I am not going to give up. I want to feel confident.": "/audio/elaine-mieko-pinho/good_morning_my_name_is_elaine_mieko_pinho_i_am_from_itatuba.mp3",
  "Good morning. My name is Elaine.": "/audio/elaine-mieko-pinho/good_morning_my_name_is_elaine.mp3",
  "I am from Itatuba, in Sao Paulo.": "/audio/elaine-mieko-pinho/i_am_from_itatuba_in_sao_paulo.mp3",
  "I am a lawyer and I manage a company.": "/audio/elaine-mieko-pinho/i_am_a_lawyer_and_i_manage_a_company_v2.mp3",
  "I love traveling, but I feel nervous speaking English.": "/audio/elaine-mieko-pinho/i_love_traveling_but_i_feel_nervous_speaking_english.mp3",
  "I want to travel alone and feel confident abroad.": "/audio/elaine-mieko-pinho/i_want_to_travel_alone_and_feel_confident_abroad.mp3",
  "Hi! I am Sarah. I work at the front desk. Are you checking in today?": "/audio/elaine-mieko-pinho/hi_i_am_sarah_i_work_at_the_front_desk_are_you_checking_in_t.mp3",
  "Yes, I have a reservation. My name is Elaine Pinho.": "/audio/elaine-mieko-pinho/yes_i_have_a_reservation_my_name_is_elaine_pinho.mp3",
  "Welcome, Ms. Pinho! Where are you from?": "/audio/elaine-mieko-pinho/welcome_ms_pinho_where_are_you_from.mp3",
  "I am from Brazil. I live in a small city called Itatuba.": "/audio/elaine-mieko-pinho/i_am_from_brazil_i_live_in_a_small_city_called_itatuba.mp3",
  "How nice! Is this your first trip to New York?": "/audio/elaine-mieko-pinho/how_nice_is_this_your_first_trip_to_new_york.mp3",
  "No, I usually travel with my family. But this time I am alone.": "/audio/elaine-mieko-pinho/no_i_usually_travel_with_my_family_but_this_time_i_am_alone.mp3",
  "That is brave! Do you need help with anything?": "/audio/elaine-mieko-pinho/that_is_brave_do_you_need_help_with_anything.mp3",
  "I am not sure how to say this, but could I get a room with a view?": "/audio/elaine-mieko-pinho/i_am_not_sure_how_to_say_this_but_could_i_get_a_room_with_a.mp3",
  "Attention, please. Flight AA 402 to New York is now boarding at Gate 12. All passengers, please have your boarding pass and passport ready.": "/audio/elaine-mieko-pinho/attention_please_flight_aa_402_to_new_york_is_now_boarding_at.mp3",
  "Could I have a window seat, please?": "/audio/elaine-mieko-pinho/could_i_have_a_window_seat_please.mp3",
  "I would like to check in, please.": "/audio/elaine-mieko-pinho/i_would_like_to_check_in_please.mp3",
  "Could you help me find my gate?": "/audio/elaine-mieko-pinho/could_you_help_me_find_my_gate.mp3",
  "I am not sure how to say this in English.": "/audio/elaine-mieko-pinho/i_am_not_sure_how_to_say_this_in_english_v2.mp3",
  "I need to deal with a problem with my reservation.": "/audio/elaine-mieko-pinho/i_need_to_deal_with_a_problem_with_my_reservation.mp3",
  "I feel nervous, but I am not going to give up.": "/audio/elaine-mieko-pinho/i_feel_nervous_but_i_am_not_going_to_give_up.mp3",
  "My name is Elaine. I am from Brazil.": "/audio/elaine-mieko-pinho/my_name_is_elaine_i_am_from_brazil_v2.mp3",
  "I work as a lawyer and I manage a company.": "/audio/elaine-mieko-pinho/i_work_as_a_lawyer_and_i_manage_a_company.mp3",
  "I usually travel with my family, but I want to be independent.": "/audio/elaine-mieko-pinho/i_usually_travel_with_my_family_but_i_want_to_be_independent.mp3",
  "I feel nervous abroad, but I am learning.": "/audio/elaine-mieko-pinho/i_feel_nervous_abroad_but_i_am_learning.mp3",
  "I want to check in at hotels and deal with problems by myself.": "/audio/elaine-mieko-pinho/i_want_to_check_in_at_hotels_and_deal_with_problems_by_mysel.mp3",
  "Boarding pass": "/audio/elaine-mieko-pinho/boarding_pass.mp3",
  "Gate": "/audio/elaine-mieko-pinho/gate.mp3",
  "Luggage": "/audio/elaine-mieko-pinho/luggage.mp3",
  "Passport": "/audio/elaine-mieko-pinho/passport.mp3",
  "Departure": "/audio/elaine-mieko-pinho/departure.mp3",
  "Arrival": "/audio/elaine-mieko-pinho/arrival.mp3",
  "Seat": "/audio/elaine-mieko-pinho/seat.mp3",
  "Delay": "/audio/elaine-mieko-pinho/delay.mp3",
  "Could I see your boarding pass, please?": "/audio/elaine-mieko-pinho/could_i_see_your_boarding_pass_please.mp3",
  "The flight departs from Gate 14.": "/audio/elaine-mieko-pinho/the_flight_departs_from_gate_14.mp3",
  "Could I check in two pieces of luggage?": "/audio/elaine-mieko-pinho/could_i_check_in_two_pieces_of_luggage.mp3",
  "Please have your passport ready.": "/audio/elaine-mieko-pinho/please_have_your_passport_ready.mp3",
  "The departure time is 10:30 AM.": "/audio/elaine-mieko-pinho/the_departure_time_is_10_30_am.mp3",
  "What is the arrival time in New York?": "/audio/elaine-mieko-pinho/what_is_the_arrival_time_in_new_york.mp3",
  "Could I have a window seat, please?": "/audio/elaine-mieko-pinho/could_i_have_a_window_seat_please_v2.mp3",
  "There is a two-hour delay on our flight.": "/audio/elaine-mieko-pinho/there_is_a_two_hour_delay_on_our_flight.mp3",
  "Elaine arrives at Guarulhos Airport in Sao Paulo. She walks to the check-in counter with her luggage. The attendant asks for her passport and boarding pass. Elaine feels a little nervous, but she remembers her English.": "/audio/elaine-mieko-pinho/elaine_arrives_at_guarulhos_airport_paragraph1.mp3",
  "Could I have a window seat, please? she asks. The attendant smiles and says, Of course! Your departure is at Gate 14. The flight departs at 10:30 AM.": "/audio/elaine-mieko-pinho/elaine_arrives_at_guarulhos_airport_paragraph2.mp3",
  "Could I have an aisle seat, please?": "/audio/elaine-mieko-pinho/could_i_have_an_aisle_seat_please.mp3",
  "Where is the gate for Flight 402?": "/audio/elaine-mieko-pinho/where_is_the_gate_for_flight_402.mp3",
  "Please have your passport and boarding pass ready.": "/audio/elaine-mieko-pinho/please_have_your_passport_and_boarding_pass_ready.mp3",
  "There is a one-hour delay on our flight.": "/audio/elaine-mieko-pinho/there_is_a_one_hour_delay_on_our_flight.mp3",
  "The departure time is 3:15 PM.": "/audio/elaine-mieko-pinho/the_departure_time_is_3_15_pm.mp3",
  "Could I check in three pieces of luggage?": "/audio/elaine-mieko-pinho/could_i_check_in_three_pieces_of_luggage.mp3",
  "You arrive at the airport with your luggage.": "/audio/elaine-mieko-pinho/you_arrive_at_the_airport_with_your_luggage.mp3",
  "You go to the check-in counter and show your passport.": "/audio/elaine-mieko-pinho/you_go_to_the_check_in_counter_and_show_your_passport.mp3",
  "You receive your boarding pass and check in your luggage.": "/audio/elaine-mieko-pinho/you_receive_your_boarding_pass_and_check_in_your_luggage.mp3",
  "You go through security and find your gate.": "/audio/elaine-mieko-pinho/you_go_through_security_and_find_your_gate.mp3",
  "You hear the boarding announcement and get on the plane.": "/audio/elaine-mieko-pinho/you_hear_the_boarding_announcement_and_get_on_the_plane.mp3",
  "Where is Gate 14?": "/audio/elaine-mieko-pinho/where_is_gate_14.mp3",
  "There is a two-hour delay on our flight.": "/audio/elaine-mieko-pinho/there_is_a_two_hour_delay_on_our_flight_v2.mp3",
  "Please have your passport and boarding pass ready.": "/audio/elaine-mieko-pinho/please_have_your_passport_and_boarding_pass_ready_v2.mp3",
  "Is there a delay on this flight?": "/audio/elaine-mieko-pinho/is_there_a_delay_on_this_flight.mp3",
  "Could I check in my luggage here?": "/audio/elaine-mieko-pinho/could_i_check_in_my_luggage_here.mp3",
  "What time does the flight depart?": "/audio/elaine-mieko-pinho/what_time_does_the_flight_depart.mp3",
  "Good morning. I would like to check in for my flight to New York.": "/audio/elaine-mieko-pinho/good_morning_i_would_like_to_check_in_for_my_flight.mp3",
  "Of course! May I see your passport and booking confirmation?": "/audio/elaine-mieko-pinho/of_course_may_i_see_your_passport_and_booking.mp3",
  "Here you go. My name is Elaine Pinho.": "/audio/elaine-mieko-pinho/here_you_go_my_name_is_elaine_pinho.mp3",
  "Thank you, Ms. Pinho. Would you like a window or aisle seat?": "/audio/elaine-mieko-pinho/thank_you_ms_pinho_would_you_like_a_window_or_aisle.mp3",
  "Could I have a window seat, please? I love to see the view.": "/audio/elaine-mieko-pinho/could_i_have_a_window_seat_i_love_the_view.mp3",
  "Of course! Do you have any luggage to check in?": "/audio/elaine-mieko-pinho/of_course_do_you_have_any_luggage_to_check_in.mp3",
  "Yes, I have two pieces of luggage.": "/audio/elaine-mieko-pinho/yes_i_have_two_pieces_of_luggage.mp3",
  "Here is your boarding pass. Your departure is at Gate 14 at 10:30 AM.": "/audio/elaine-mieko-pinho/here_is_your_boarding_pass_gate_14_10_30.mp3",
  "Attention, please. Flight AA 402 to New York JFK has a two-hour delay. New departure time is 12:30 PM. We apologize for the inconvenience. Please remain near Gate 14.": "/audio/elaine-mieko-pinho/attention_flight_aa_402_delay_announcement.mp3",
  "Where are the restrooms?": "/audio/elaine-mieko-pinho/where_are_the_restrooms.mp3",
  "Excuse me, where is Gate 14?": "/audio/elaine-mieko-pinho/excuse_me_where_is_gate_14.mp3",
  "Could I change my seat, please?": "/audio/elaine-mieko-pinho/could_i_change_my_seat_please.mp3",
  "Is this the right gate for the flight to New York?": "/audio/elaine-mieko-pinho/is_this_the_right_gate_for_new_york.mp3",
  "How long is the delay?": "/audio/elaine-mieko-pinho/how_long_is_the_delay.mp3",
  "Could I get something to eat near the gate?": "/audio/elaine-mieko-pinho/could_i_get_something_to_eat_near_the_gate.mp3"
};

// Dialogue lines context for voice assignment
// Sarah/female attendant lines = Ellen, Elaine lines = Ellen, male/David lines = Arthur
// Announcement lines = Arthur (male PA voice)
const ellenPhrases = new Set([
  // Sarah (female front desk)
  "Hi! I am Sarah. I work at the front desk. Are you checking in today?",
  "Welcome, Ms. Pinho! Where are you from?",
  "How nice! Is this your first trip to New York?",
  "That is brave! Do you need help with anything?",
  // Female attendant at airport
  "Of course! May I see your passport and booking confirmation?",
  "Thank you, Ms. Pinho. Would you like a window or aisle seat?",
  "Of course! Do you have any luggage to check in?",
  "Here is your boarding pass. Your departure is at Gate 14 at 10:30 AM.",
  // Elaine's own lines (female student)
  "Yes, I have a reservation. My name is Elaine Pinho.",
  "I am from Brazil. I live in a small city called Itatuba.",
  "No, I usually travel with my family. But this time I am alone.",
  "I am not sure how to say this, but could I get a room with a view?",
  "Good morning. I would like to check in for my flight to New York.",
  "Here you go. My name is Elaine Pinho.",
  "Could I have a window seat, please? I love to see the view.",
  "Yes, I have two pieces of luggage.",
  // Elaine narrative / female voice lines
  "Good morning. My name is Elaine.",
  "I am from Itatuba, in Sao Paulo.",
  "I love traveling, but I feel nervous speaking English.",
  "I want to travel alone and feel confident abroad.",
  "Elaine arrives at Guarulhos Airport in Sao Paulo. She walks to the check-in counter with her luggage. The attendant asks for her passport and boarding pass. Elaine feels a little nervous, but she remembers her English.",
  "Could I have a window seat, please? she asks. The attendant smiles and says, Of course! Your departure is at Gate 14. The flight departs at 10:30 AM.",
  "Good morning. My name is Elaine Mieko Pinho. I am from Itatuba, a small city in Sao Paulo, Brazil. I am a lawyer and I also manage a family company. I usually travel with my family, but I want to travel alone too. I feel nervous when I need to speak English abroad, but I am not going to give up. I want to feel confident.",
]);

// Phrase alternation tracker for non-dialogue phrases
let phraseAlternator = false; // false=Arthur, true=Ellen

function getVoice(text) {
  // Single words (1-2 words) always Arthur
  const wordCount = text.trim().split(/\s+/).length;
  if (wordCount <= 2) return { id: ARTHUR, name: 'Arthur' };

  // Explicit Ellen phrases (female characters / Elaine herself)
  if (ellenPhrases.has(text)) return { id: ELLEN, name: 'Ellen' };

  // Announcements (PA system) = Arthur
  if (text.startsWith('Attention')) return { id: ARTHUR, name: 'Arthur' };

  // For remaining 3+ word phrases, alternate Arthur/Ellen
  phraseAlternator = !phraseAlternator;
  return phraseAlternator ? { id: ELLEN, name: 'Ellen' } : { id: ARTHUR, name: 'Arthur' };
}

function generateAudio(text, voiceId) {
  return new Promise((resolve, reject) => {
    const postData = JSON.stringify({
      text: text,
      model_id: 'eleven_monolingual_v1',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    });

    const options = {
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'Accept': 'audio/mpeg',
        'Content-Type': 'application/json',
        'xi-api-key': API_KEY
      }
    };

    const req = https.request(options, (res) => {
      if (res.statusCode !== 200) {
        let body = '';
        res.on('data', c => body += c);
        res.on('end', () => reject(new Error(`API ${res.statusCode}: ${body}`)));
        return;
      }
      const chunks = [];
      res.on('data', chunk => chunks.push(chunk));
      res.on('end', () => resolve(Buffer.concat(chunks)));
    });

    req.on('error', reject);
    req.write(postData);
    req.end();
  });
}

function delay(ms) { return new Promise(r => setTimeout(r, ms)); }

async function main() {
  // Ensure output directory exists
  if (!fs.existsSync(AUDIO_DIR)) fs.mkdirSync(AUDIO_DIR, { recursive: true });

  const entries = Object.entries(audioMap).filter(([_, p]) => p.includes('/audio/elaine-mieko-pinho/'));
  const total = entries.length;
  let generated = 0;
  let skipped = 0;

  console.log(`\nFound ${total} audioMap entries for elaine-mieko-pinho\n`);

  for (let i = 0; i < entries.length; i++) {
    const [text, relPath] = entries[i];
    const fullPath = path.join(BASE_DIR, relPath);
    const filename = path.basename(relPath);

    if (fs.existsSync(fullPath)) {
      skipped++;
      console.log(`Skipped: ${filename} (exists)`);
      continue;
    }

    const voice = getVoice(text);
    try {
      const buffer = await generateAudio(text, voice.id);
      fs.writeFileSync(fullPath, buffer);
      generated++;
      console.log(`Generated ${generated}/${total - skipped}: ${filename} (${voice.name})`);
      if (i < entries.length - 1) await delay(500);
    } catch (err) {
      console.error(`FAILED: ${filename} — ${err.message}`);
    }
  }

  console.log(`\n=== SUMMARY ===`);
  console.log(`Total entries: ${total}`);
  console.log(`Generated: ${generated}`);
  console.log(`Skipped (existing): ${skipped}`);
  console.log(`Failed: ${total - generated - skipped}`);
}

main();
