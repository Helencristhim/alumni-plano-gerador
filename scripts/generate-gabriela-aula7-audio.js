#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for Gabriela Pires - Aula 7
 * Voice: Ellen (female/Gabriela) + Arthur (male/vocab/Liam)
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
  { text: "Country", file: "country.mp3", voice: "arthur" },
  { text: "Nationality", file: "nationality.mp3", voice: "arthur" },
  { text: "Brazilian", file: "brazilian.mp3", voice: "arthur" },
  { text: "French", file: "french.mp3", voice: "arthur" },
  { text: "American", file: "american.mp3", voice: "arthur" },
  { text: "Language", file: "language.mp3", voice: "arthur" },
  { text: "Passport", file: "passport.mp3", voice: "arthur" },
  { text: "International", file: "international.mp3", voice: "arthur" },
  // Vocab examples - alternating
  { text: "Brazil is a beautiful country.", file: "brazil_is_a_beautiful_country.mp3", voice: "ellen" },
  { text: "What is your nationality?", file: "what_is_your_nationality.mp3", voice: "arthur" },
  { text: "I am Brazilian.", file: "i_am_brazilian.mp3", voice: "ellen" },
  { text: "She is French.", file: "she_is_french.mp3", voice: "arthur" },
  { text: "Blake Lively is American.", file: "blake_lively_is_american.mp3", voice: "ellen" },
  { text: "I speak two languages.", file: "i_speak_two_languages.mp3", voice: "ellen" },
  { text: "Here is my passport.", file: "here_is_my_passport.mp3", voice: "ellen" },
  { text: "This is an international school.", file: "this_is_an_international_school.mp3", voice: "arthur" },
  // Grammar / key phrases
  { text: "Where are you from?", file: "where_are_you_from.mp3", voice: "arthur" },
  { text: "I am from Brazil.", file: "i_am_from_brazil.mp3", voice: "ellen" },
  { text: "I am from São Paulo, Brazil.", file: "i_am_from_sao_paulo_brazil_l7.mp3", voice: "ellen" },
  { text: "She is from France.", file: "she_is_from_france.mp3", voice: "arthur" },
  { text: "He is from the United States.", file: "he_is_from_the_united_states.mp3", voice: "arthur" },
  { text: "They are from Japan.", file: "they_are_from_japan.mp3", voice: "ellen" },
  { text: "What language do you speak?", file: "what_language_do_you_speak.mp3", voice: "arthur" },
  { text: "I speak Portuguese and I am learning English.", file: "i_speak_portuguese_and_i_am_learning_english.mp3", voice: "ellen" },
  { text: "Is she American?", file: "is_she_american.mp3", voice: "arthur" },
  { text: "No, she is not American. She is British.", file: "no_she_is_not_american_she_is_british.mp3", voice: "arthur" },
  { text: "Ed Westwick is British. He is from England.", file: "ed_westwick_is_british_he_is_from_england.mp3", voice: "arthur" },
  { text: "Blake Lively is American. She is from the United States.", file: "blake_lively_is_american_she_is_from_the_us.mp3", voice: "ellen" },
  // Dialogue - Gabriela (Ellen) meets Liam (Arthur) at hostel
  { text: "Hi there! Are you staying at this hostel too?", file: "hi_there_are_you_staying_at_this_hostel_too.mp3", voice: "arthur" },
  { text: "Yes! Hi! I am Gabriela. I am from Brazil. Where are you from?", file: "yes_hi_i_am_gabriela_i_am_from_brazil_where_are_you_from.mp3", voice: "ellen" },
  { text: "Nice to meet you, Gabriela! I am Liam. I am from Australia.", file: "nice_to_meet_you_gabriela_i_am_liam_from_australia.mp3", voice: "arthur" },
  { text: "Australia! That is so cool! What language do you speak?", file: "australia_that_is_so_cool_what_language_do_you_speak.mp3", voice: "ellen" },
  { text: "I speak English. It is my first language. Do you speak French?", file: "i_speak_english_it_is_my_first_language_do_you_speak_french.mp3", voice: "arthur" },
  { text: "No, I do not speak French. I speak Portuguese and I am learning English.", file: "no_i_do_not_speak_french_i_speak_portuguese.mp3", voice: "ellen" },
  { text: "Your English is great! Is this your first time in France?", file: "your_english_is_great_is_this_your_first_time_in_france.mp3", voice: "arthur" },
  { text: "Yes! I am so excited! I am Brazilian and this is my first international trip!", file: "yes_i_am_so_excited_i_am_brazilian_first_international_trip.mp3", voice: "ellen" },
  { text: "That is amazing! I love traveling. Let us explore Paris together!", file: "that_is_amazing_i_love_traveling_explore_paris.mp3", voice: "arthur" },
  { text: "Yes! That sounds great!", file: "yes_that_sounds_great.mp3", voice: "ellen" },
  // Listening - hostel introductions
  { text: "Welcome to Paris Youth Hostel! Let us meet some travelers. Hi, I am Sophie. I am from Canada. I am Canadian. I speak English and French. Next, hi, I am Kenji. I am from Japan. I am Japanese. I speak Japanese and a little English. And finally, hello, I am Maria. I am from Italy. I am Italian. I speak Italian, English, and a little French.", file: "hostel_introductions_listening.mp3", voice: "ellen" },
  // Listening 2 - three travelers
  { text: "My name is Pierre. I am French. I am from Paris. I speak French and English.", file: "my_name_is_pierre_i_am_french.mp3", voice: "arthur" },
  { text: "Hi, I am Yuki. I am Japanese. I am from Tokyo. I speak Japanese.", file: "hi_i_am_yuki_i_am_japanese.mp3", voice: "ellen" },
  { text: "Hey! I am Jake. I am American. I am from New York. I speak English and Spanish.", file: "hey_i_am_jake_i_am_american.mp3", voice: "arthur" },
  // Pronunciation
  { text: "Brazilian", file: "brazilian_pron.mp3", voice: "ellen" },
  { text: "Nationality", file: "nationality_pron.mp3", voice: "arthur" },
  { text: "International", file: "international_pron.mp3", voice: "arthur" },
  { text: "Language", file: "language_pron.mp3", voice: "arthur" },
  { text: "Where are you from? I am from Brazil. I am Brazilian.", file: "where_are_you_from_i_am_from_brazil_brazilian.mp3", voice: "ellen" },
  // Survival / speech practice
  { text: "I am from São Paulo, Brazil. I am Brazilian.", file: "i_am_from_sao_paulo_i_am_brazilian.mp3", voice: "ellen" },
  { text: "What nationality are you?", file: "what_nationality_are_you.mp3", voice: "arthur" },
  { text: "I speak Portuguese and I am learning English.", file: "i_speak_portuguese_learning_english.mp3", voice: "ellen" },
  { text: "Where in France are you from?", file: "where_in_france_are_you_from.mp3", voice: "arthur" },
  { text: "This is my first international trip.", file: "this_is_my_first_international_trip.mp3", voice: "ellen" },
  // Think response
  { text: "Hi! My name is Gabriela Pires. I am Brazilian. I am from São Paulo, Brazil. I speak Portuguese and I am learning English. This is my first time in France. I am 16 years old and I am a student. Nice to meet you!", file: "hi_my_name_is_gabriela_pires_i_am_brazilian_full_intro.mp3", voice: "ellen" },
];

async function generateAudio(text, filename, voiceId) {
  const filePath = path.join(OUTPUT_DIR, filename);
  if (fs.existsSync(filePath)) return { skipped: true };
  const response = await fetch(`${API_URL}/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text, model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75, style: 0.0, use_speaker_boost: true }
    })
  });
  if (!response.ok) throw new Error(`${response.status} for "${text.substring(0,40)}..."`);
  fs.writeFileSync(filePath, Buffer.from(await response.arrayBuffer()));
  return { skipped: false };
}

async function main() {
  console.log(`Generating ${phrases.length} audio files for Aula 7...`);
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
