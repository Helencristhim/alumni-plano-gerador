const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'elaine-mieko-pinho');

// Elaine = female → ELLEN for her lines/exercises
// David (front desk, male) = ARTHUR
// Tom (maintenance, male) = ARTHUR

const PHRASES = [
  // ===== Vocab words (ELLEN) =====
  { text: "Towel", file: "towel.mp3", voice: ELLEN },
  { text: "Air Conditioning", file: "air_conditioning.mp3", voice: ELLEN },
  { text: "Noise", file: "noise.mp3", voice: ELLEN },
  { text: "Broken", file: "broken.mp3", voice: ELLEN },
  { text: "Complaint", file: "complaint.mp3", voice: ELLEN },
  { text: "Fix", file: "fix.mp3", voice: ELLEN },
  { text: "Leak", file: "leak.mp3", voice: ELLEN },
  { text: "Manager", file: "manager.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate) =====
  { text: "Could I get extra towels, please?", file: "could_i_get_extra_towels_please.mp3", voice: ELLEN },
  { text: "The air conditioning is not working.", file: "the_air_conditioning_is_not_working.mp3", voice: ARTHUR },
  { text: "There is a lot of noise from the room next door.", file: "there_is_a_lot_of_noise_from_the_room_next_door.mp3", voice: ELLEN },
  { text: "The TV in my room is broken.", file: "the_tv_in_my_room_is_broken.mp3", voice: ARTHUR },
  { text: "I would like to make a complaint about the noise.", file: "i_would_like_to_make_a_complaint_about_the_noise.mp3", voice: ELLEN },
  { text: "Could you send someone to fix it?", file: "could_you_send_someone_to_fix_it.mp3", voice: ARTHUR },
  { text: "There is a leak in the bathroom.", file: "there_is_a_leak_in_the_bathroom.mp3", voice: ELLEN },
  { text: "I would like to speak with the manager, please.", file: "i_would_like_to_speak_with_the_manager_please.mp3", voice: ARTHUR },

  // ===== Grammar context paragraphs =====
  { text: "Elaine is in room 712 at the Grand Central Hotel. It is her first night in New York. She is tired from the long flight, but she is happy to be here. She puts her bags on the bed and goes to the bathroom. There is a leak under the sink. Water is coming out. She also notices the air conditioning is not working. The room is very hot. Then she hears noise from the room next door. It is very loud.", file: "elaine_room_712_paragraph1.mp3", voice: ELLEN },
  { text: "Elaine picks up the phone and calls the front desk. She needs to explain the problems and ask for help. She is nervous, but she remembers her English. She knows she can use there is and there are to describe problems, and could you to make polite requests.", file: "elaine_room_712_paragraph2.mp3", voice: ARTHUR },

  // ===== Grammar examples =====
  { text: "There is a problem with my room.", file: "there_is_a_problem_with_my_room.mp3", voice: ELLEN },
  { text: "There are no towels in my bathroom.", file: "there_are_no_towels_in_my_bathroom.mp3", voice: ARTHUR },
  { text: "The air conditioning is not working in my room.", file: "the_air_conditioning_is_not_working_in_my_room.mp3", voice: ELLEN },
  { text: "Could you send someone to fix the leak?", file: "could_you_send_someone_to_fix_the_leak.mp3", voice: ARTHUR },
  { text: "There is a lot of noise from next door.", file: "there_is_a_lot_of_noise_from_next_door.mp3", voice: ELLEN },
  { text: "I would like to make a complaint.", file: "i_would_like_to_make_a_complaint.mp3", voice: ARTHUR },

  // ===== Dialogue — David (ARTHUR), Elaine (ELLEN) =====
  { text: "Hello, this is David at the front desk. How can I help you?", file: "hello_this_is_david_at_the_front_desk.mp3", voice: ARTHUR },
  { text: "Hi, this is Elaine in room 712. There is a problem with my room.", file: "hi_this_is_elaine_in_room_712_there_is_a_problem.mp3", voice: ELLEN },
  { text: "I am sorry to hear that. What is the problem?", file: "i_am_sorry_to_hear_that_what_is_the_problem.mp3", voice: ARTHUR },
  { text: "The air conditioning is not working, and there is a leak in the bathroom.", file: "the_air_conditioning_is_not_working_and_there_is_a_leak.mp3", voice: ELLEN },
  { text: "I understand. I will send someone right away. Is there anything else?", file: "i_understand_i_will_send_someone_right_away.mp3", voice: ARTHUR },
  { text: "Yes, there is a lot of noise from the room next door. Could you do something about it?", file: "yes_there_is_a_lot_of_noise_from_the_room_next_door.mp3", voice: ELLEN },
  { text: "Of course. I will call that room and ask them to be quiet. I am very sorry for the trouble.", file: "of_course_i_will_call_that_room_and_ask_them.mp3", voice: ARTHUR },
  { text: "Thank you very much, David.", file: "thank_you_very_much_david.mp3", voice: ELLEN },
  { text: "You are welcome, Ms. Pinho. Someone will be there in ten minutes.", file: "you_are_welcome_ms_pinho_someone_will_be_there.mp3", voice: ARTHUR },

  // ===== Listening full =====
  { text: "Hello, this is David at the front desk. How can I help you? Hi, this is Elaine in room 712. There is a problem with my room. The air conditioning is not working and there is a leak in the bathroom. Also, there is a lot of noise from the room next door. I am sorry to hear that. I will send someone right away to fix the air conditioning and the leak. And I will call the other room about the noise. Thank you very much, David. You are welcome. Someone will be there in ten minutes.", file: "listening13_hotel_problems_full.mp3", voice: ARTHUR },
  { text: "Hi, I am Tom from maintenance. I am here to fix the air conditioning and the leak. Let me take a look at the air conditioning first. Yes, it is broken. I can fix it in about twenty minutes. And the leak is under the sink. I will fix that too. Everything should be working fine soon.", file: "listening14_maintenance_call_full.mp3", voice: ARTHUR },

  // ===== Dialogue 2 — Tom (ARTHUR), Elaine (ELLEN) =====
  { text: "Hi, I am Tom from maintenance. I am here to fix the air conditioning.", file: "hi_i_am_tom_from_maintenance.mp3", voice: ARTHUR },
  { text: "Thank you for coming. The air conditioning is not working and it is very hot.", file: "thank_you_for_coming_the_ac_is_not_working.mp3", voice: ELLEN },
  { text: "Let me take a look. Yes, it is broken. I can fix it in about twenty minutes.", file: "let_me_take_a_look_yes_it_is_broken.mp3", voice: ARTHUR },
  { text: "That would be great. There is also a leak in the bathroom. Could you fix that too?", file: "that_would_be_great_there_is_also_a_leak.mp3", voice: ELLEN },
  { text: "Of course. I will fix both problems for you.", file: "of_course_i_will_fix_both_problems.mp3", voice: ARTHUR },
  { text: "Thank you so much. I really appreciate it.", file: "thank_you_so_much_i_really_appreciate_it.mp3", voice: ELLEN },

  // ===== Speech practice (ELLEN) =====
  { text: "There is a problem with the air conditioning.", file: "there_is_a_problem_with_the_air_conditioning.mp3", voice: ELLEN },
  { text: "Could you send someone to fix it, please?", file: "could_you_send_someone_to_fix_it_please.mp3", voice: ELLEN },
  { text: "There is a leak in the bathroom. Could you fix it?", file: "there_is_a_leak_in_the_bathroom_could_you_fix_it.mp3", voice: ELLEN },
  { text: "There are no towels in my room.", file: "there_are_no_towels_in_my_room.mp3", voice: ELLEN },

  // ===== Survival / Quick fire =====
  { text: "The shower is not working.", file: "the_shower_is_not_working.mp3", voice: ELLEN },
  { text: "There are problems with my room.", file: "there_are_problems_with_my_room.mp3", voice: ARTHUR },
  { text: "There is no hot water.", file: "there_is_no_hot_water.mp3", voice: ELLEN },
  { text: "The TV is broken and the air conditioning is not working.", file: "the_tv_is_broken_and_the_ac_is_not_working.mp3", voice: ARTHUR },

  // ===== Ordering =====
  { text: "You notice the air conditioning is broken. Call the front desk.", file: "you_notice_ac_broken_call_front_desk.mp3", voice: ARTHUR },
  { text: "You call the front desk and describe the problem.", file: "you_call_front_desk_describe_problem.mp3", voice: ELLEN },
  { text: "The maintenance worker arrives and fixes the air conditioning.", file: "maintenance_worker_arrives_fixes_ac.mp3", voice: ARTHUR },
  { text: "You tell the maintenance worker about the leak in the bathroom.", file: "you_tell_maintenance_about_leak.mp3", voice: ELLEN },
  { text: "The maintenance worker fixes the leak and you thank him.", file: "maintenance_fixes_leak_you_thank_him.mp3", voice: ARTHUR },

  // ===== Ordering full sequence =====
  { text: "You notice the air conditioning is broken. You call the front desk and describe the problem. The maintenance worker arrives and fixes the air conditioning. You tell the maintenance worker about the leak in the bathroom. The maintenance worker fixes the leak and you thank him.", file: "order_l7_hotel_problems.mp3", voice: ELLEN },
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
    headers: { 'Content-Type': 'application/json', 'xi-api-key': API_KEY },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } })
  });
  if (!resp.ok) { console.error(`ERROR ${file}: ${resp.status} ${await resp.text()}`); return; }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(filePath, buffer);
  console.log(`OK: ${file} (${(buffer.length/1024).toFixed(1)} KB)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  console.log(`Generating ${PHRASES.length} audio files for Elaine Aula 7...\n`);
  for (const p of PHRASES) {
    await generate(p.text, p.file, p.voice);
    await new Promise(r => setTimeout(r, 500));
  }
  console.log('\nDone!');
}

main();
