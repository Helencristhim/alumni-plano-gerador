const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carolina-paludetto-rodrigues');

// Voice rules:
// - Carolina is FEMALE -> her lines/exercises = ELLEN
// - Tyler is MALE -> his lines = ARTHUR
// - Single vocab words -> ELLEN (student gender)
// - General phrases -> ALTERNATE Arthur/Ellen
// - Dialogue lines -> by character gender

const PHRASES = [
  // ===== Vocab words (Carolina is female -> ELLEN) =====
  { text: "Enjoy", file: "aula4_enjoy.mp3", voice: ELLEN },
  { text: "Prefer", file: "aula4_prefer.mp3", voice: ELLEN },
  { text: "Hobby", file: "aula4_hobby.mp3", voice: ELLEN },
  { text: "Collect", file: "aula4_collect.mp3", voice: ELLEN },
  { text: "Create", file: "aula4_create.mp3", voice: ELLEN },
  { text: "Rank", file: "aula4_rank.mp3", voice: ELLEN },
  { text: "Passion", file: "aula4_passion.mp3", voice: ELLEN },
  { text: "Relaxing", file: "aula4_relaxing.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate Ellen/Arthur) =====
  { text: "I enjoy writing stories in my free time.", file: "aula4_i_enjoy_writing_stories.mp3", voice: ELLEN },
  { text: "Do you prefer reading or watching movies?", file: "aula4_do_you_prefer_reading.mp3", voice: ARTHUR },
  { text: "My favorite hobby is playing handball.", file: "aula4_my_favorite_hobby.mp3", voice: ELLEN },
  { text: "She collects stickers from every country.", file: "aula4_she_collects_stickers.mp3", voice: ARTHUR },
  { text: "I love to create new characters for my stories.", file: "aula4_i_love_to_create.mp3", voice: ELLEN },
  { text: "Can you rank your top three subjects?", file: "aula4_can_you_rank.mp3", voice: ARTHUR },
  { text: "Writing is my true passion.", file: "aula4_writing_is_my_true_passion.mp3", voice: ELLEN },
  { text: "Listening to music is very relaxing after school.", file: "aula4_listening_to_music.mp3", voice: ARTHUR },

  // ===== Grammar discovery sentences (alternate) =====
  { text: "I like writing.", file: "aula4_grammar_i_like_writing.mp3", voice: ELLEN },
  { text: "She loves reading.", file: "aula4_grammar_she_loves_reading.mp3", voice: ARTHUR },
  { text: "They enjoy playing.", file: "aula4_grammar_they_enjoy_playing.mp3", voice: ELLEN },
  { text: "We prefer walking.", file: "aula4_grammar_we_prefer_walking.mp3", voice: ARTHUR },

  // ===== Dialogue -- Tyler (ARTHUR) and Carolina (ELLEN) =====
  { text: "Hi Carolina! What do you enjoy doing after school?", file: "aula4_dialogue_tyler_1.mp3", voice: ARTHUR },
  { text: "I love writing stories! It is my favorite hobby. What about you?", file: "aula4_dialogue_carolina_1.mp3", voice: ELLEN },
  { text: "I enjoy playing guitar. Do you prefer writing or reading?", file: "aula4_dialogue_tyler_2.mp3", voice: ARTHUR },
  { text: "I prefer writing, but I also enjoy reading adventure books.", file: "aula4_dialogue_carolina_2.mp3", voice: ELLEN },
  { text: "That is cool! Do you collect anything?", file: "aula4_dialogue_tyler_3.mp3", voice: ARTHUR },
  { text: "I collect notebooks! I love creating stories in different ones.", file: "aula4_dialogue_carolina_3.mp3", voice: ELLEN },
  { text: "Nice! Can you rank your top three hobbies?", file: "aula4_dialogue_tyler_4.mp3", voice: ARTHUR },
  { text: "Number one is writing, number two is handball, and number three is reading. What is your passion?", file: "aula4_dialogue_carolina_4.mp3", voice: ELLEN },

  // ===== Listening 1 -- Mia (ELLEN, female) =====
  { text: "Hi! My name is Mia. I am fourteen and I live in Toronto.", file: "aula4_listening1_mia.mp3", voice: ELLEN },
  { text: "I enjoy many things in my free time. My favorite hobby is painting. I love creating colorful pictures. I also enjoy reading fantasy books. I prefer painting over reading because it is very relaxing. I collect art supplies from different stores. My passion is making art that tells a story.", file: "aula4_listening1_full.mp3", voice: ELLEN },

  // ===== Listening 2 -- Jake (ARTHUR, male) =====
  { text: "Good morning! My name is Jake. I am fifteen and I live in Melbourne.", file: "aula4_listening2_jake.mp3", voice: ARTHUR },
  { text: "I enjoy playing sports after school. My favorite hobby is surfing. I love being in the ocean. I prefer surfing over skateboarding. I also enjoy collecting seashells on the beach. I rank surfing as my number one passion. Listening to music is very relaxing after a long day of surfing.", file: "aula4_listening2_full.mp3", voice: ARTHUR },

  // ===== Survival card (Carolina = ELLEN) =====
  { text: "What do you enjoy doing on weekends?", file: "aula4_survival_1.mp3", voice: ELLEN },
  { text: "I love writing stories.", file: "aula4_survival_2.mp3", voice: ELLEN },
  { text: "Do you prefer reading or watching movies?", file: "aula4_survival_3.mp3", voice: ELLEN },
  { text: "My hobby is playing handball.", file: "aula4_survival_4.mp3", voice: ELLEN },
  { text: "What is your passion?", file: "aula4_survival_5.mp3", voice: ELLEN },

  // ===== Speech cards (Carolina = ELLEN) =====
  { text: "I enjoy writing stories and playing handball in my free time.", file: "aula4_speech_1.mp3", voice: ELLEN },
  { text: "My favorite hobby is creating new characters for my stories.", file: "aula4_speech_2.mp3", voice: ELLEN },
  { text: "Do you prefer sports or creative activities? I prefer writing.", file: "aula4_speech_3.mp3", voice: ELLEN },
  { text: "I collect notebooks because I love writing in different ones.", file: "aula4_speech_4.mp3", voice: ELLEN },
  { text: "Listening to music is very relaxing after a busy school day.", file: "aula4_speech_5.mp3", voice: ELLEN },

  // ===== Fill-in-blank sentences (alternate) =====
  { text: "I enjoy playing handball after school.", file: "aula4_fill_1.mp3", voice: ELLEN },
  { text: "She loves creating new stories every week.", file: "aula4_fill_2.mp3", voice: ARTHUR },
  { text: "We prefer walking to school together.", file: "aula4_fill_3.mp3", voice: ELLEN },
  { text: "Do you enjoy collecting things?", file: "aula4_fill_4.mp3", voice: ARTHUR },
  { text: "He prefers playing guitar over piano.", file: "aula4_fill_5.mp3", voice: ELLEN },

  // ===== Ordering audio =====
  { text: "First, I enjoy writing stories in my free time. Then, my favorite hobby is playing handball after school. I also enjoy reading adventure books. I collect notebooks because I love creating stories. Finally, writing is my number one passion.", file: "aula4_order_l4.mp3", voice: ELLEN },
];

if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

async function generate(text, file, voice) {
  const outPath = path.join(DIR, file);
  if (fs.existsSync(outPath)) {
    console.log(`SKIP (exists): ${file}`);
    return;
  }
  console.log(`GEN: ${file} [${voice === ARTHUR ? 'Arthur' : 'Ellen'}]`);
  const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voice}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_turbo_v2_5',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    })
  });
  if (!res.ok) {
    console.error(`FAIL ${file}: ${res.status} ${await res.text()}`);
    return;
  }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  console.log(`OK: ${file} (${buf.length} bytes)`);
}

async function main() {
  console.log(`Generating ${PHRASES.length} audio files for Carolina Aula 4...`);
  for (const p of PHRASES) {
    await generate(p.text, p.file, p.voice);
    await new Promise(r => setTimeout(r, 350));
  }
  console.log('Done!');
}

main().catch(console.error);
