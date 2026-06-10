#!/usr/bin/env node
/**
 * Generate ElevenLabs audio for Gabriela Pires - Aula 10 (What Do You Look Like? / Descriptions)
 * Voices: Ellen (Gabriela / student) + Rachel (friend Bea) + Arthur (alternating narration)
 * Roster per REGRA 35/C1. Skips files that already exist (REGRA C9 - never overwrite MP3s).
 */
const fs = require('fs');
const path = require('path');
const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = { arthur: 'sfJopaWaOtauCD3HKX6Q', ellen: 'BIvP0GN1cAtSRTxNHnWS', josh: 'TxGEqnHWrfWFTfGW9XjX', rachel: '21m00Tcm4TlvDq8ikWAM', domi: 'AZnzlk1XvdvUeBnXmlld', bella: 'EXAVITQu4vr4xnSDxMaL' };
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'gabriela-pires');
if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const phrases = [
  { text: "Tall", file: "tall.mp3", voice: "ellen" },
  { text: "Short", file: "short.mp3", voice: "ellen" },
  { text: "Hair", file: "hair.mp3", voice: "ellen" },
  { text: "Eyes", file: "eyes.mp3", voice: "ellen" },
  { text: "Curly", file: "curly.mp3", voice: "ellen" },
  { text: "Blond", file: "blond.mp3", voice: "ellen" },
  { text: "Beard", file: "beard.mp3", voice: "ellen" },
  { text: "Glasses", file: "glasses.mp3", voice: "ellen" },
  { text: "She is tall.", file: "she_is_tall.mp3", voice: "ellen" },
  { text: "He is short.", file: "he_is_short.mp3", voice: "ellen" },
  { text: "She has long hair.", file: "she_has_long_hair.mp3", voice: "ellen" },
  { text: "He has blue eyes.", file: "he_has_blue_eyes.mp3", voice: "ellen" },
  { text: "She has curly hair.", file: "she_has_curly_hair.mp3", voice: "ellen" },
  { text: "She has blond hair.", file: "she_has_blond_hair.mp3", voice: "ellen" },
  { text: "He has a beard.", file: "he_has_a_beard.mp3", voice: "ellen" },
  { text: "He has glasses.", file: "he_has_glasses.mp3", voice: "ellen" },
  { text: "Let us play a game. Describe a character, and I guess who!", file: "lets_play_a_game_describe_a_character.mp3", voice: "rachel" },
  { text: "OK. She is tall. She has long blond hair.", file: "ok_she_is_tall_she_has_long_blond_hair.mp3", voice: "ellen" },
  { text: "Does she have blue eyes?", file: "does_she_have_blue_eyes.mp3", voice: "rachel" },
  { text: "Yes, she has blue eyes. She is beautiful.", file: "yes_she_has_blue_eyes_she_is_beautiful.mp3", voice: "ellen" },
  { text: "Is it Serena from Gossip Girl?", file: "is_it_serena_from_gossip_girl.mp3", voice: "rachel" },
  { text: "Yes! Now it is your turn.", file: "yes_now_it_is_your_turn.mp3", voice: "ellen" },
  { text: "He is not tall. He has short dark hair and a beard.", file: "he_is_not_tall_short_dark_hair_and_beard.mp3", voice: "rachel" },
  { text: "Does he have glasses?", file: "does_he_have_glasses.mp3", voice: "ellen" },
  { text: "No, he does not. He is handsome.", file: "no_he_does_not_he_is_handsome.mp3", voice: "rachel" },
  { text: "Is it Chuck?", file: "is_it_chuck.mp3", voice: "ellen" },
  { text: "Yes! You are good at this!", file: "yes_you_are_good_at_this.mp3", voice: "rachel" },
  { text: "This is my favorite character. Her name is Serena. She is tall and she is beautiful. She has long blond hair and blue eyes. She is young. Her friend is different. He is short. He has short dark hair and a beard. He has brown eyes and glasses. They are very different, but they are best friends.", file: "describe_listening_full.mp3", voice: "ellen" },
  { text: "She is tall. She has curly brown hair. She has green eyes.", file: "listening2_situation1_curly.mp3", voice: "arthur" },
  { text: "He is young. He has short blond hair and a beard.", file: "listening2_situation2_blond_beard.mp3", voice: "ellen" },
  { text: "She has long black hair and glasses. She is short.", file: "listening2_situation3_black_hair_glasses.mp3", voice: "arthur" },
  { text: "He is young.", file: "he_is_young.mp3", voice: "arthur" },
  { text: "What does she look like?", file: "what_does_she_look_like.mp3", voice: "ellen" },
  { text: "She has long blond hair.", file: "she_has_long_blond_hair.mp3", voice: "ellen" },
  { text: "He has blue eyes and a beard.", file: "he_has_blue_eyes_and_a_beard.mp3", voice: "ellen" },
  { text: "He is tall and he has short hair.", file: "he_is_tall_and_he_has_short_hair.mp3", voice: "ellen" },
  { text: "My favorite character is tall. She has long blond hair and blue eyes. She is beautiful.", file: "my_favorite_character_is_tall_description.mp3", voice: "ellen" },
  { text: "What does she look like? She is tall. She has long blond hair. She has blue eyes. She is beautiful.", file: "order_l10_ordering.mp3", voice: "ellen" }
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
