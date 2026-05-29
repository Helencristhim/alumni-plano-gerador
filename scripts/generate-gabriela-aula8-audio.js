#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for Gabriela Pires - Aula 8
 * Voice: Ellen (Gabriela) + Arthur (passerby/vocab)
 */
const fs = require('fs');
const path = require('path');
const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = { arthur: 'sfJopaWaOtauCD3HKX6Q', ellen: 'BIvP0GN1cAtSRTxNHnWS' };
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-pires');
if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const phrases = [
  // Vocab words - Arthur
  { text: "Speak", file: "speak.mp3", voice: "arthur" },
  { text: "Understand", file: "understand.mp3", voice: "arthur" },
  { text: "Help", file: "help.mp3", voice: "arthur" },
  { text: "Repeat", file: "repeat.mp3", voice: "arthur" },
  { text: "Find", file: "find.mp3", voice: "arthur" },
  { text: "Show", file: "show.mp3", voice: "arthur" },
  { text: "Slower", file: "slower.mp3", voice: "arthur" },
  { text: "Map", file: "map.mp3", voice: "arthur" },
  // Vocab examples
  { text: "I can speak English.", file: "i_can_speak_english.mp3", voice: "ellen" },
  { text: "I can't understand.", file: "i_cant_understand.mp3", voice: "ellen" },
  { text: "Can you help me?", file: "can_you_help_me.mp3", voice: "ellen" },
  { text: "Can you repeat that, please?", file: "can_you_repeat_that_please.mp3", voice: "ellen" },
  { text: "I can't find my hotel.", file: "i_cant_find_my_hotel.mp3", voice: "ellen" },
  { text: "Can you show me on the map?", file: "can_you_show_me_on_the_map.mp3", voice: "ellen" },
  { text: "Can you speak slower, please?", file: "can_you_speak_slower_please.mp3", voice: "ellen" },
  { text: "I have a map.", file: "i_have_a_map.mp3", voice: "ellen" },
  // Key grammar phrases
  { text: "I can swim.", file: "i_can_swim.mp3", voice: "ellen" },
  { text: "I can't drive.", file: "i_cant_drive.mp3", voice: "ellen" },
  { text: "Can you speak French?", file: "can_you_speak_french.mp3", voice: "arthur" },
  { text: "Yes, I can.", file: "yes_i_can.mp3", voice: "ellen" },
  { text: "No, I can't.", file: "no_i_cant.mp3", voice: "ellen" },
  { text: "Could you help me, please?", file: "could_you_help_me_please.mp3", voice: "ellen" },
  { text: "I can speak Portuguese.", file: "i_can_speak_portuguese.mp3", voice: "ellen" },
  { text: "She can play guitar.", file: "she_can_play_guitar.mp3", voice: "arthur" },
  { text: "He can't cook.", file: "he_cant_cook.mp3", voice: "arthur" },
  { text: "Can she speak English?", file: "can_she_speak_english.mp3", voice: "arthur" },
  // Dialogue - Gabriela (Ellen) asks Passerby (Arthur) for help
  { text: "Excuse me! Can you help me, please?", file: "excuse_me_can_you_help_me_please.mp3", voice: "ellen" },
  { text: "Of course! What do you need?", file: "of_course_what_do_you_need.mp3", voice: "arthur" },
  { text: "I can't find my hotel. Can you show me on the map?", file: "i_cant_find_my_hotel_show_me_map.mp3", voice: "ellen" },
  { text: "Sure! Where is your hotel?", file: "sure_where_is_your_hotel.mp3", voice: "arthur" },
  { text: "It is called Hotel Montmartre. I can't understand the street names.", file: "hotel_montmartre_cant_understand_streets.mp3", voice: "ellen" },
  { text: "Ah, I know that hotel! It is near here. I can show you.", file: "i_know_that_hotel_i_can_show_you.mp3", voice: "arthur" },
  { text: "Thank you so much! Can you speak slower, please? I am still learning English.", file: "thank_you_can_you_speak_slower.mp3", voice: "ellen" },
  { text: "No problem! Walk straight and turn left. You can't miss it!", file: "no_problem_walk_straight_turn_left.mp3", voice: "arthur" },
  { text: "Thank you! You are very kind!", file: "thank_you_you_are_very_kind.mp3", voice: "ellen" },
  { text: "You are welcome! Enjoy Paris!", file: "you_are_welcome_enjoy_paris.mp3", voice: "arthur" },
  // Listening - survival situations
  { text: "Gabriela is lost in Paris. She stops a person and says: Excuse me, can you help me? I can't find my hotel. The person speaks very fast. Gabriela says: I am sorry, I can't understand. Can you speak slower, please? Can you show me on the map? The person shows her the map and says: Your hotel is here. You can walk there in five minutes. Gabriela says: Thank you so much! I can see it now!", file: "gabriela_lost_in_paris_listening.mp3", voice: "ellen" },
  // Listening 2
  { text: "Can you swim? Yes, I can. I can swim very well. Can you cook? No, I can't cook. But I can make coffee! Can you speak French? No, I can't speak French. But I can speak English and Portuguese.", file: "can_you_abilities_listening.mp3", voice: "ellen" },
  // Speech practice / survival
  { text: "Excuse me, can you help me? I can't find my hotel. Can you show me on the map? Can you speak slower, please? I can speak English.", file: "full_survival_speech.mp3", voice: "ellen" },
  { text: "I don't speak French, but I can speak English.", file: "i_dont_speak_french_but_can_speak_english.mp3", voice: "ellen" },
  { text: "Can you repeat that, please? I can't understand.", file: "can_you_repeat_that_cant_understand.mp3", voice: "ellen" },
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
  console.log(`Generating ${phrases.length} audio files for Aula 8...`);
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
