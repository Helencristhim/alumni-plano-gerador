#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for Elaine Mieko Pinho - Aula 9 (Restaurant Basics)
 * Voices: Ellen (Elaine / student) + Arthur (James the waiter / alternating narration)
 * Skips files that already exist (REGRA C9 - never overwrite MP3s).
 */
const fs = require('fs');
const path = require('path');
const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = { arthur: 'sfJopaWaOtauCD3HKX6Q', ellen: 'BIvP0GN1cAtSRTxNHnWS' };
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'elaine-mieko-pinho');
if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const phrases = [
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: "ellen" },
  { text: "I am not sure I understand. Could you explain?", file: "i_am_not_sure_i_understand_could_you_explain.mp3", voice: "ellen" },
  { text: "Could you speak more slowly, please?", file: "could_you_speak_more_slowly_please.mp3", voice: "ellen" },
  { text: "I am not sure how to say this in English.", file: "i_am_not_sure_how_to_say_this_in_english_v2.mp3", voice: "ellen" },
  { text: "Thank you for your patience.", file: "thank_you_for_your_patience.mp3", voice: "ellen" },
  { text: "Reservation", file: "reservation.mp3", voice: "ellen" },
  { text: "Menu", file: "menu.mp3", voice: "ellen" },
  { text: "Waiter", file: "waiter.mp3", voice: "ellen" },
  { text: "Appetizer", file: "appetizer.mp3", voice: "ellen" },
  { text: "Main Course", file: "main_course.mp3", voice: "ellen" },
  { text: "Dessert", file: "dessert.mp3", voice: "ellen" },
  { text: "The Check", file: "the_check.mp3", voice: "ellen" },
  { text: "Tip", file: "tip.mp3", voice: "ellen" },
  { text: "Order", file: "order_word.mp3", voice: "ellen" },
  { text: "I would like the soup, please.", file: "i_would_like_the_soup_please.mp3", voice: "ellen" },
  { text: "I would like the chicken, please.", file: "i_would_like_the_chicken_please.mp3", voice: "arthur" },
  { text: "Could I have the menu, please?", file: "could_i_have_the_menu_please.mp3", voice: "ellen" },
  { text: "Could I have the check, please?", file: "could_i_have_the_check_please.mp3", voice: "ellen" },
  { text: "Would you like something to drink?", file: "would_you_like_something_to_drink.mp3", voice: "arthur" },
  { text: "I would like a coffee, please.", file: "i_would_like_a_coffee_please.mp3", voice: "ellen" },
  { text: "It is evening in New York. Elaine is hungry after a long day. She walks to the Grand Central Bistro, near her hotel. A waiter welcomes her. She has a reservation under her name. The waiter gives her the menu. Elaine reads the menu carefully. For the appetizer, she orders the tomato soup. For the main course, she orders the grilled chicken. She would like a sparkling water to drink. At the end, she orders a chocolate cake for dessert. The food is delicious. Elaine asks for the check. She pays and leaves a tip. She is happy. She ordered her dinner all in English.", file: "listening9_restaurant_order.mp3", voice: "ellen" },
  { text: "Good evening. Welcome to the Grand Central Bistro. Do you have a reservation?", file: "welcome_bistro_reservation.mp3", voice: "arthur" },
  { text: "Good evening. Yes, I have a reservation under Elaine Pinho.", file: "good_evening_yes_reservation_elaine.mp3", voice: "ellen" },
  { text: "Here is the menu. Would you like something to drink?", file: "here_is_the_menu_drink.mp3", voice: "arthur" },
  { text: "Could I have a sparkling water, please?", file: "could_i_have_a_sparkling_water_please.mp3", voice: "ellen" },
  { text: "Of course. Are you ready to order?", file: "of_course_ready_to_order.mp3", voice: "arthur" },
  { text: "Yes. For the appetizer, I would like the tomato soup.", file: "appetizer_tomato_soup.mp3", voice: "ellen" },
  { text: "Excellent choice. And for the main course?", file: "excellent_choice_main_course.mp3", voice: "arthur" },
  { text: "I would like the grilled chicken, please.", file: "i_would_like_the_grilled_chicken_please.mp3", voice: "ellen" },
  { text: "Would you like a dessert?", file: "would_you_like_a_dessert.mp3", voice: "arthur" },
  { text: "Yes, please. I would like the chocolate cake.", file: "yes_please_chocolate_cake.mp3", voice: "ellen" },
  { text: "Here you are. Thank you very much.", file: "here_you_are_thank_you.mp3", voice: "arthur" },
  { text: "Could I have the menu, please? I would like to order.", file: "could_i_have_the_menu_i_would_like_to_order.mp3", voice: "ellen" },
  { text: "For the appetizer, I would like the soup. For the main course, the chicken.", file: "appetizer_soup_main_chicken.mp3", voice: "ellen" },
  { text: "Could I have the check, please? Thank you very much.", file: "could_i_have_the_check_thank_you.mp3", voice: "ellen" },
  { text: "I would like to order, please.", file: "i_would_like_to_order_please.mp3", voice: "ellen" },
  { text: "For the main course, I would like the chicken.", file: "for_the_main_course_chicken.mp3", voice: "ellen" },
  { text: "Could I have a glass of water, please?", file: "could_i_have_a_glass_of_water_please.mp3", voice: "ellen" },
  { text: "For dessert, I would like the chocolate cake.", file: "for_dessert_chocolate_cake.mp3", voice: "ellen" },
  { text: "Elaine reads the menu. She orders an appetizer. She orders a main course. She orders a dessert. She asks for the check. She leaves a tip.", file: "order_l9_sequence.mp3", voice: "ellen" }
];

async function generateAudio(text, filename, voiceId) {
  const filePath = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(filePath)) return { skipped: true };
  const response = await fetch(`${API_URL}/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true } })
  });
  if (!response.ok) throw new Error(`${response.status} for "${text.substring(0,40)}..."`);
  fs.writeFileSync(filePath, Buffer.from(await response.arrayBuffer()));
  return { skipped: false };
}

async function main() {
  console.log(`Generating ${phrases.length} audio files for Aula 9...`);
  let gen = 0, skip = 0, err = 0;
  for (const p of phrases) {
    try {
      const r = await generateAudio(p.text, p.file, VOICES[p.voice]);
      if (r.skipped) { skip++; process.stdout.write('.'); }
      else { gen++; process.stdout.write('+'); await new Promise(r => setTimeout(r, 300)); }
    } catch (e) { err++; console.error(`\n  [ERROR] ${e.message}`); }
  }
  console.log(`\n\nDone: ${gen} generated, ${skip} skipped, ${err} errors`);
}
main().catch(console.error);
