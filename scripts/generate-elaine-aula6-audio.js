const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'elaine-mieko-pinho');

// Voice rules:
// - Elaine is FEMALE → her lines/exercises = ELLEN
// - Lisa (receptionist, female) = ELLEN
// - James (bellhop, male) = ARTHUR
// - Single vocab words → ELLEN (student gender)
// - General phrases → ALTERNATE Arthur/Ellen
// - Dialogue lines → by character gender

const PHRASES = [
  // ===== Vocab words (Elaine is female → ELLEN) =====
  { text: "Reservation", file: "reservation.mp3", voice: ELLEN },
  { text: "Front Desk", file: "front_desk.mp3", voice: ELLEN },
  { text: "Key Card", file: "key_card.mp3", voice: ELLEN },
  { text: "Lobby", file: "lobby.mp3", voice: ELLEN },
  { text: "Floor", file: "floor.mp3", voice: ELLEN },
  { text: "Elevator", file: "elevator.mp3", voice: ELLEN },
  { text: "Bellhop", file: "bellhop.mp3", voice: ELLEN },
  { text: "Room Service", file: "room_service.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "I have a reservation under Elaine Pinho.", file: "i_have_a_reservation_under_elaine_pinho.mp3", voice: ELLEN },
  { text: "Could I have a key card for room 712, please?", file: "could_i_have_a_key_card_for_room_712_please.mp3", voice: ARTHUR },
  { text: "I would like a room on a high floor, please.", file: "i_would_like_a_room_on_a_high_floor_please.mp3", voice: ELLEN },
  { text: "Could I get a late checkout, please?", file: "could_i_get_a_late_checkout_please.mp3", voice: ARTHUR },
  { text: "I would like to order room service, please.", file: "i_would_like_to_order_room_service_please.mp3", voice: ELLEN },
  { text: "Where is the elevator?", file: "where_is_the_elevator.mp3", voice: ARTHUR },
  { text: "The bellhop helped me with my bags.", file: "the_bellhop_helped_me_with_my_bags.mp3", voice: ELLEN },
  { text: "I am waiting in the lobby.", file: "i_am_waiting_in_the_lobby.mp3", voice: ARTHUR },

  // ===== Grammar examples (alternate) =====
  { text: "My room is on the seventh floor.", file: "my_room_is_on_the_seventh_floor.mp3", voice: ELLEN },
  { text: "Could I have extra towels, please?", file: "could_i_have_extra_towels_please.mp3", voice: ARTHUR },
  { text: "I would like a wake-up call at 7 AM, please.", file: "i_would_like_a_wake_up_call_at_7am_please.mp3", voice: ELLEN },

  // ===== Grammar in Context paragraphs =====
  { text: "Elaine arrives at the Grand Central Hotel in Manhattan. She walks into the lobby and goes to the front desk. I have a reservation under Elaine Pinho, she says. The receptionist checks the computer.", file: "elaine_hotel_checkin_paragraph1.mp3", voice: ELLEN },
  { text: "Welcome, Ms. Pinho! Your room is on the seventh floor. Here is your key card. The elevator is on your right. Would you like a bellhop to help with your bags?", file: "elaine_hotel_checkin_paragraph2.mp3", voice: ARTHUR },

  // ===== Dialogue — Lisa (female = ELLEN), Elaine (female = ELLEN), James (male = ARTHUR) =====
  { text: "Good evening! Welcome to the Grand Central Hotel. Do you have a reservation?", file: "good_evening_welcome_grand_central.mp3", voice: ELLEN },
  { text: "Yes, I have a reservation under Elaine Pinho.", file: "yes_i_have_a_reservation_under_elaine_pinho.mp3", voice: ELLEN },
  { text: "Let me check. Yes, here it is! A single room for five nights. Is that correct?", file: "let_me_check_yes_here_it_is.mp3", voice: ELLEN },
  { text: "Yes, that is correct. Could I have a room on a high floor, please?", file: "yes_that_is_correct_high_floor.mp3", voice: ELLEN },
  { text: "Of course! Room 712, on the seventh floor. Here is your key card.", file: "of_course_room_712_seventh_floor.mp3", voice: ELLEN },
  { text: "Thank you! Where is the elevator?", file: "thank_you_where_is_the_elevator.mp3", voice: ELLEN },
  { text: "It is on your right, just past the lobby. Would you like a bellhop to help with your bags?", file: "it_is_on_your_right_past_the_lobby.mp3", voice: ELLEN },
  { text: "Yes, please. I would like some help. Thank you, Lisa!", file: "yes_please_i_would_like_some_help.mp3", voice: ELLEN },
  { text: "Good evening, ma'am. I am James. Let me take your bags to room 712.", file: "good_evening_i_am_james_let_me_take_bags.mp3", voice: ARTHUR },
  { text: "Thank you, James! That is very kind.", file: "thank_you_james_that_is_very_kind.mp3", voice: ELLEN },

  // ===== Listening audio (full recordings) =====
  { text: "Good evening. Welcome to the Grand Central Hotel. My name is Lisa. Do you have a reservation? Yes, I have a reservation under Elaine Pinho. Let me check. Yes, here it is. A single room for five nights. Your room is number 712, on the seventh floor. Here is your key card. The elevator is on your right. Would you like a bellhop to help with your bags? Yes, please. That would be great. Thank you, Lisa!", file: "listening11_hotel_checkin_full.mp3", voice: ELLEN },
  { text: "Good evening. Room service. You ordered a club sandwich and a bottle of water. Where would you like me to put the tray? The total is 28 dollars. Would you like to add it to your room bill?", file: "listening12_room_service_full.mp3", voice: ARTHUR },
  { text: "Good evening. Room service. You ordered a club sandwich and a bottle of water. Where would you like me to put the tray? The total is 28 dollars. Would you like to add it to your room bill?", file: "room_service_delivery.mp3", voice: ARTHUR },

  // ===== Speech practice (Elaine = ELLEN) =====
  { text: "I have a reservation under Elaine Pinho.", file: "speech_reservation_elaine.mp3", voice: ELLEN },
  { text: "Could I have a key card for room 712, please?", file: "speech_key_card_712.mp3", voice: ELLEN },
  { text: "I would like a room on a high floor, please.", file: "speech_high_floor.mp3", voice: ELLEN },
  { text: "I would like to order room service, please.", file: "speech_room_service.mp3", voice: ELLEN },

  // ===== Survival card (alternate) =====
  { text: "I have a reservation under the name Johnson.", file: "i_have_a_reservation_under_johnson.mp3", voice: ELLEN },
  { text: "Could I have a room with a view, please?", file: "could_i_have_a_room_with_a_view_please.mp3", voice: ARTHUR },
  { text: "I would like to order breakfast to my room.", file: "i_would_like_to_order_breakfast_to_my_room.mp3", voice: ELLEN },
  { text: "Where is the front desk?", file: "where_is_the_front_desk.mp3", voice: ARTHUR },
  { text: "Could I get an extra pillow, please?", file: "could_i_get_an_extra_pillow_please.mp3", voice: ELLEN },
  { text: "I would like a non-smoking room, please.", file: "i_would_like_a_non_smoking_room_please.mp3", voice: ARTHUR },

  // ===== Ordering exercise phrases =====
  { text: "You arrive at the hotel and walk into the lobby.", file: "you_arrive_at_the_hotel_and_walk_into_the_lobby.mp3", voice: ARTHUR },
  { text: "You go to the front desk and say your name.", file: "you_go_to_the_front_desk_and_say_your_name.mp3", voice: ELLEN },
  { text: "You receive your key card and ask about the elevator.", file: "you_receive_your_key_card_and_ask_about_the_elevator.mp3", voice: ARTHUR },
  { text: "The bellhop takes your bags to your room.", file: "the_bellhop_takes_your_bags_to_your_room.mp3", voice: ELLEN },
  { text: "You enter your room and order room service.", file: "you_enter_your_room_and_order_room_service.mp3", voice: ARTHUR },

  // ===== Quick fire / drilling =====
  { text: "Please go to the front desk to check in.", file: "please_go_to_the_front_desk_to_check_in.mp3", voice: ARTHUR },
  { text: "Here is your key card for room 712.", file: "here_is_your_key_card_for_room_712.mp3", voice: ELLEN },
];

if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

async function generate(text, file, voiceId) {
  const filePath = path.join(DIR, file);
  if (fs.existsSync(filePath)) {
    console.log(`SKIP (exists): ${file}`);
    return;
  }
  console.log(`Generating: ${file} (${voiceId === ARTHUR ? 'Arthur' : 'Ellen'})`);
  const resp = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'xi-api-key': API_KEY
    },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    })
  });
  if (!resp.ok) {
    const err = await resp.text();
    console.error(`ERROR ${file}: ${resp.status} ${err}`);
    return;
  }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  console.log(`OK: ${file} (${(buffer.length/1024).toFixed(1)} KB)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  console.log(`Generating ${PHRASES.length} audio files for Elaine Aula 6...`);
  console.log(`Output: ${DIR}\n`);
  for (const p of PHRASES) {
    await generate(p.text, p.file, p.voice);
    await new Promise(r => setTimeout(r, 500)); // rate limit
  }
  console.log('\nDone!');
}

main();
