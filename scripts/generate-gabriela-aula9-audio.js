#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for Gabriela Pires - Aula 9 (Where Is It? / Directions)
 * Voices: Ellen (Gabriela / student) + Arthur (local / alternating narration)
 * Skips files that already exist (REGRA C9 - never overwrite MP3s).
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
  { text: "Street", file: "street.mp3", voice: "ellen" },
  { text: "Corner", file: "corner.mp3", voice: "ellen" },
  { text: "Straight", file: "straight.mp3", voice: "ellen" },
  { text: "Right", file: "right.mp3", voice: "ellen" },
  { text: "Cross", file: "cross.mp3", voice: "ellen" },
  { text: "Station", file: "station.mp3", voice: "ellen" },
  { text: "Walk down this street.", file: "walk_down_this_street.mp3", voice: "ellen" },
  { text: "The cafe is on the corner.", file: "the_cafe_is_on_the_corner.mp3", voice: "ellen" },
  { text: "Turn at the corner.", file: "turn_at_the_corner.mp3", voice: "ellen" },
  { text: "Turn left.", file: "turn_left.mp3", voice: "ellen" },
  { text: "Turn right at the corner.", file: "turn_right_at_the_corner.mp3", voice: "ellen" },
  { text: "Go straight.", file: "go_straight.mp3", voice: "ellen" },
  { text: "Cross the street.", file: "cross_the_street.mp3", voice: "ellen" },
  { text: "The metro station is near.", file: "the_metro_station_is_near.mp3", voice: "ellen" },
  { text: "Excuse me, how do I get to the Eiffel Tower?", file: "excuse_me_how_do_i_get_to_the_eiffel_tower.mp3", voice: "ellen" },
  { text: "It is easy. Go straight on this street.", file: "it_is_easy_go_straight_on_this_street.mp3", voice: "arthur" },
  { text: "And then?", file: "and_then.mp3", voice: "ellen" },
  { text: "Turn left at the corner. Then cross the street.", file: "turn_left_at_the_corner_then_cross.mp3", voice: "arthur" },
  { text: "Is it far?", file: "is_it_far.mp3", voice: "ellen" },
  { text: "No, it is near. It is next to a big park.", file: "no_it_is_near_next_to_a_big_park.mp3", voice: "arthur" },
  { text: "Can you show me on the map?", file: "can_you_show_me_on_the_map.mp3", voice: "ellen" },
  { text: "Of course. We are here. The tower is in front of the park.", file: "of_course_we_are_here_tower_in_front_of_park.mp3", voice: "arthur" },
  { text: "Thank you so much!", file: "thank_you_so_much.mp3", voice: "ellen" },
  { text: "You are welcome! Enjoy Paris!", file: "you_are_welcome_enjoy_paris.mp3", voice: "arthur" },
  { text: "Gabriela is at the metro station. She wants to go to her hotel. She asks a woman: How do I get to Hotel Le Marais? The woman says: Go straight on this street. Turn right at the corner. Then cross the street. The hotel is next to a cafe, across from the station. Gabriela asks: Is it far? No, the woman says, it is near. It is five minutes. Gabriela says: Thank you! Can you show me on the map? The woman shows her. Now Gabriela can find her hotel.", file: "gabriela_directions_listening_full.mp3", voice: "ellen" },
  { text: "Where is the bakery? Go straight and turn left. It is on the corner.", file: "listening2_situation1_bakery.mp3", voice: "arthur" },
  { text: "How do I get to the museum? Cross the street. It is in front of the park.", file: "listening2_situation2_museum.mp3", voice: "ellen" },
  { text: "Is the station far? No, it is near. It is behind the hotel.", file: "listening2_situation3_station.mp3", voice: "arthur" },
  { text: "The cafe is next to the bank.", file: "the_cafe_is_next_to_the_bank.mp3", voice: "ellen" },
  { text: "The hotel is across from the station.", file: "the_hotel_is_across_from_the_station.mp3", voice: "arthur" },
  { text: "The bakery is on the corner.", file: "the_bakery_is_on_the_corner.mp3", voice: "ellen" },
  { text: "The park is behind the museum.", file: "the_park_is_behind_the_museum.mp3", voice: "arthur" },
  { text: "How do I get to the station?", file: "how_do_i_get_to_the_station.mp3", voice: "ellen" },
  { text: "Where is the hotel?", file: "where_is_the_hotel.mp3", voice: "ellen" },
  { text: "Go straight and turn left.", file: "go_straight_and_turn_left.mp3", voice: "ellen" },
  { text: "It is next to the cafe.", file: "it_is_next_to_the_cafe.mp3", voice: "ellen" },
  { text: "The hotel is next to the cafe.", file: "the_hotel_is_next_to_the_cafe.mp3", voice: "ellen" },
  { text: "Turn left at the corner.", file: "turn_left_at_the_corner.mp3", voice: "ellen" },
  { text: "Excuse me, how do I get to my hotel? Is it far? Can you show me on the map?", file: "excuse_me_how_do_i_get_to_my_hotel_full.mp3", voice: "ellen" },
  { text: "Excuse me, how do I get to the hotel? Go straight on this street. Turn right at the corner. Is it far? No, it is near. It is next to the cafe.", file: "order_l9_ordering.mp3", voice: "ellen" }
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
