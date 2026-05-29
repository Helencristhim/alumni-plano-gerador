const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'elaine-mieko-pinho');

const PHRASES = [
  { text: "Boarding Pass", file: "boarding_pass_review.mp3", voice: ELLEN },
  { text: "I showed my boarding pass and walked to the gate.", file: "i_showed_my_boarding_pass_and_walked_to_the_gate.mp3", voice: ARTHUR },
  { text: "The taxi fare from the airport to the hotel was forty dollars.", file: "the_taxi_fare_from_the_airport_to_hotel_was_forty.mp3", voice: ELLEN },
  { text: "I have a reservation at the Grand Central Hotel.", file: "i_have_a_reservation_at_the_grand_central_hotel.mp3", voice: ARTHUR },
  { text: "The receptionist gave me my key card for room 712.", file: "the_receptionist_gave_me_my_key_card_for_room_712.mp3", voice: ELLEN },
  { text: "I had a complaint about the air conditioning.", file: "i_had_a_complaint_about_the_air_conditioning.mp3", voice: ARTHUR },
  { text: "The maintenance worker came to fix the problem.", file: "the_maintenance_worker_came_to_fix_the_problem.mp3", voice: ELLEN },
  { text: "I took my luggage and went to the check-in counter.", file: "i_took_my_luggage_and_went_to_the_check_in_counter.mp3", voice: ARTHUR },
  { text: "Elaine lives in Indaiatuba. She travels alone. She arrives at the airport with her luggage. She shows her boarding pass and passport. The officer at immigration checks her documents. She takes a taxi to the hotel. The fare is forty dollars. At the hotel, she has a reservation. The receptionist gives her the key card. In the room, there is a problem. The air conditioning is not working. She makes a complaint. The maintenance worker comes to fix it.", file: "review_full_journey_narrative.mp3", voice: ELLEN },
  { text: "Good morning. I would like to check in for my flight. Here is my passport. Could I have a window seat, please? The attendant gives me my boarding pass. I go through security and walk to the gate. At immigration, the officer asks about my visit. I take a taxi to the Grand Central Hotel. At the hotel, I have a reservation under my name. The receptionist gives me the key card. In my room, I notice the air conditioning is not working. I call the front desk and make a complaint. The maintenance worker comes to fix it. Now I can relax.", file: "listening15_full_journey.mp3", voice: ELLEN },
  { text: "After the maintenance worker fixed the air conditioning and the leak, Elaine finally relaxed in room 712. She ordered room service, a club sandwich and water. She looked out the window at the New York skyline. She thought about her day. She checked in at the airport, flew to New York, went through immigration, took a taxi, checked in at the hotel, and solved the room problems, all in English. She felt proud.", file: "listening16_hotel_night_recap.mp3", voice: ARTHUR },
  { text: "Good morning. I would like to check in for my flight.", file: "good_morning_check_in_flight_review.mp3", voice: ELLEN },
  { text: "Could I have my boarding pass, please?", file: "could_i_have_my_boarding_pass_please.mp3", voice: ELLEN },
  { text: "Welcome to the United States. What is the purpose of your visit?", file: "welcome_us_purpose_of_visit.mp3", voice: ARTHUR },
  { text: "Five nights.", file: "five_nights.mp3", voice: ELLEN },
  { text: "Good evening. Where would you like to go?", file: "good_evening_where_would_you_like_to_go.mp3", voice: ARTHUR },
  { text: "I would like to go to the Grand Central Hotel, please.", file: "i_would_like_to_go_grand_central_hotel.mp3", voice: ELLEN },
  { text: "That will be forty dollars.", file: "that_will_be_forty_dollars.mp3", voice: ARTHUR },
  { text: "Here you go. Thank you, Miguel.", file: "here_you_go_thank_you_miguel.mp3", voice: ELLEN },
  { text: "Good evening. I have a reservation under Elaine Pinho.", file: "good_evening_reservation_under_elaine_pinho.mp3", voice: ELLEN },
  { text: "Yes, room 712. Here is your key card.", file: "yes_room_712_here_is_your_key_card.mp3", voice: ARTHUR },
  { text: "Excuse me, the air conditioning is not working in my room.", file: "excuse_me_ac_not_working_my_room.mp3", voice: ELLEN },
  { text: "I am sorry to hear that. I will send someone to fix it right away.", file: "i_am_sorry_send_someone_to_fix_it.mp3", voice: ARTHUR },
  { text: "Hi, I am Tom from maintenance. I am here to fix the air conditioning in room 712.", file: "hi_i_am_tom_maintenance_fix_ac_room_712.mp3", voice: ARTHUR },
  { text: "Thank you, Tom. There is also a problem with the shower.", file: "thank_you_tom_problem_with_shower.mp3", voice: ELLEN },
  { text: "No problem. I can fix both.", file: "no_problem_i_can_fix_both.mp3", voice: ARTHUR },
  { text: "Could I have a window seat, please? I showed my boarding pass at the gate.", file: "could_i_have_window_seat_showed_boarding_pass.mp3", voice: ELLEN },
  { text: "I would like to go to the Grand Central Hotel. The fare was forty dollars.", file: "i_would_like_grand_central_fare_forty.mp3", voice: ARTHUR },
  { text: "There is a problem with the air conditioning. It is not working.", file: "there_is_problem_ac_not_working.mp3", voice: ELLEN },
  { text: "I have a complaint. Could you send someone to fix the shower?", file: "i_have_complaint_send_someone_fix_shower.mp3", voice: ARTHUR },
];

if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

async function generate(text, file, voiceId) {
  const filePath = path.join(DIR, file);
  if (fs.existsSync(filePath)) { console.log(`SKIP: ${file}`); return; }
  console.log(`Generating: ${file} (${voiceId === ARTHUR ? 'Arthur' : 'Ellen'})`);
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
  });
  if (!resp.ok) { console.error(`ERROR ${file}: ${resp.status}`); return; }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  console.log(`OK: ${file} (${(buffer.length/1024).toFixed(1)} KB)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  console.log(`Generating ${PHRASES.length} audio files for Elaine Aula 8 (Review)...\n`);
  for (const p of PHRASES) { await generate(p.text, p.file, p.voice); await new Promise(r => setTimeout(r, 500)); }
  console.log('\nDone!');
}
main();
