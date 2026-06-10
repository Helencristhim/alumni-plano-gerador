#!/usr/bin/env node
/**
 * ElevenLabs audio for Elaine Mieko Pinho - Aula 10 (Special Requests / Allergies).
 * Voices: Ellen (Elaine / student) + Arthur (waiter Daniel). Roster per REGRA 35/C1.
 * Skips files that already exist (REGRA C9 - never overwrite MP3s).
 */
const fs = require('fs');
const path = require('path');
const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = { arthur: 'sfJopaWaOtauCD3HKX6Q', ellen: 'BIvP0GN1cAtSRTxNHnWS', josh: 'TxGEqnHWrfWFTfGW9XjX', rachel: '21m00Tcm4TlvDq8ikWAM', domi: 'AZnzlk1XvdvUeBnXmlld', bella: 'EXAVITQu4vr4xnSDxMaL' };
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'elaine-mieko-pinho');
if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const phrases = [
  { text: "Allergic", file: "allergic.mp3", voice: "ellen" },
  { text: "Allergy", file: "allergy.mp3", voice: "ellen" },
  { text: "Nuts", file: "nuts.mp3", voice: "ellen" },
  { text: "Shellfish", file: "shellfish.mp3", voice: "ellen" },
  { text: "Gluten", file: "gluten.mp3", voice: "ellen" },
  { text: "Dairy", file: "dairy.mp3", voice: "ellen" },
  { text: "Spicy", file: "spicy.mp3", voice: "ellen" },
  { text: "Ingredient", file: "ingredient.mp3", voice: "ellen" },
  { text: "Could I have the menu, please?", file: "could_i_have_the_menu_please.mp3", voice: "ellen" },
  { text: "I would like the grilled chicken, please.", file: "i_would_like_the_grilled_chicken_please.mp3", voice: "ellen" },
  { text: "I am allergic to nuts.", file: "i_am_allergic_to_nuts.mp3", voice: "ellen" },
  { text: "I am allergic to shellfish.", file: "i_am_allergic_to_shellfish.mp3", voice: "ellen" },
  { text: "Can you make it without dairy?", file: "can_you_make_it_without_dairy.mp3", voice: "ellen" },
  { text: "Does it have gluten in it?", file: "does_it_have_gluten_in_it.mp3", voice: "ellen" },
  { text: "Good evening. I sit down at the Grand Central Bistro. The waiter brings the menu. First, I tell him something important. I am allergic to nuts and I am allergic to shellfish. I ask the waiter, does the salad have nuts in it? He checks and says yes, it has nuts. So I ask, can you make it without nuts, please? Of course, he says. For the main course, I ask for a dish without dairy. The waiter recommends the grilled chicken with vegetables. It is not spicy and it has no dairy. Now I can eat my dinner safely.", file: "listening10_allergy_table.mp3", voice: "ellen" },
  { text: "Hello, I would like to book a table for two for tonight, please. There is one important thing. I am allergic to shellfish, so I cannot eat shrimp or crab. Can you prepare safe dishes without shellfish? The restaurant says yes, of course, we can prepare safe dishes for you. Thank you very much. I feel happy and safe before my dinner.", file: "listening10_phone_reservation.mp3", voice: "ellen" },
  { text: "Good evening. Are you ready to order?", file: "d10_good_evening_ready_to_order.mp3", voice: "arthur" },
  { text: "Almost. First, I am allergic to nuts. Does the salad have nuts in it?", file: "d10_almost_allergic_nuts_salad.mp3", voice: "ellen" },
  { text: "Let me check. Yes, the green salad has nuts in it.", file: "d10_let_me_check_salad_nuts.mp3", voice: "arthur" },
  { text: "Can you make it without nuts, please?", file: "d10_can_you_make_without_nuts.mp3", voice: "ellen" },
  { text: "Of course. I can make it without nuts.", file: "d10_of_course_without_nuts.mp3", voice: "arthur" },
  { text: "Thank you. I am also allergic to shellfish. Is there shellfish in the soup?", file: "d10_also_shellfish_soup.mp3", voice: "ellen" },
  { text: "No, the tomato soup has no shellfish. It is safe for you.", file: "d10_soup_no_shellfish_safe.mp3", voice: "arthur" },
  { text: "Good. Can you recommend a main course without dairy?", file: "d10_recommend_main_without_dairy.mp3", voice: "ellen" },
  { text: "Yes. The grilled chicken with vegetables has no dairy.", file: "d10_chicken_vegetables_no_dairy.mp3", voice: "arthur" },
  { text: "Is it spicy?", file: "d10_is_it_spicy.mp3", voice: "ellen" },
  { text: "No, it is not spicy. It is very mild.", file: "d10_not_spicy_very_mild.mp3", voice: "arthur" },
  { text: "Perfect. I would like the grilled chicken, please.", file: "d10_perfect_grilled_chicken.mp3", voice: "ellen" },
  { text: "I am allergic to nuts. Does it have nuts in it?", file: "drill_allergic_nuts_does_it_have.mp3", voice: "ellen" },
  { text: "Can you make it without dairy, please?", file: "drill_make_without_dairy_please.mp3", voice: "ellen" },
  { text: "Can you recommend a dish without shellfish?", file: "drill_recommend_without_shellfish.mp3", voice: "ellen" },
  { text: "Is there gluten in this? I am allergic to gluten.", file: "drill_gluten_in_this_allergic.mp3", voice: "ellen" },
  { text: "Does it have shellfish in it?", file: "does_it_have_shellfish_in_it.mp3", voice: "ellen" },
  { text: "Can you make it without gluten?", file: "can_you_make_it_without_gluten.mp3", voice: "ellen" },
  { text: "Can you recommend a dish without nuts?", file: "can_you_recommend_without_nuts.mp3", voice: "ellen" },
  { text: "Is this dish spicy?", file: "is_this_dish_spicy.mp3", voice: "ellen" },
  { text: "Can you recommend something without gluten?", file: "can_you_recommend_something_without_gluten.mp3", voice: "ellen" },
  { text: "The waiter brings the menu. Elaine says she is allergic to nuts. She asks if the salad has nuts in it. The waiter makes the salad without nuts. Elaine orders a safe main course without dairy.", file: "order_l10_sequence.mp3", voice: "ellen" },
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: "ellen" },
  { text: "I am not sure I understand. Could you explain?", file: "i_am_not_sure_i_understand_could_you_explain.mp3", voice: "ellen" },
  { text: "Could you speak more slowly, please?", file: "could_you_speak_more_slowly_please.mp3", voice: "ellen" },
  { text: "I am not sure how to say this in English.", file: "i_am_not_sure_how_to_say_this_in_english_v2.mp3", voice: "ellen" },
  { text: "Thank you for your patience.", file: "thank_you_for_your_patience.mp3", voice: "ellen" }
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
  console.log(`Generating ${phrases.length} audio files for Aula 10...`);
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
