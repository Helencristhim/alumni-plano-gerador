const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carolina-paludetto-rodrigues');

// Voice rules:
// - Carolina is FEMALE → her lines/exercises = ELLEN
// - Noah is MALE → his lines = ARTHUR
// - Single vocab words → ELLEN (student gender)
// - General phrases → ALTERNATE Arthur/Ellen
// - Dialogue lines → by character gender

const PHRASES = [
  // ===== Vocab words (Carolina is female → ELLEN) =====
  { text: "Subject", file: "aula3_subject.mp3", voice: ELLEN },
  { text: "Classmate", file: "aula3_classmate.mp3", voice: ELLEN },
  { text: "Favorite", file: "aula3_favorite.mp3", voice: ELLEN },
  { text: "Assignment", file: "aula3_assignment.mp3", voice: ELLEN },
  { text: "Break", file: "aula3_break.mp3", voice: ELLEN },
  { text: "Attend", file: "aula3_attend.mp3", voice: ELLEN },
  { text: "Participate", file: "aula3_participate.mp3", voice: ELLEN },
  { text: "Recess", file: "aula3_recess.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate Ellen/Arthur) =====
  { text: "My favorite subject is English.", file: "aula3_my_favorite_subject_is_english.mp3", voice: ELLEN },
  { text: "Do you have many classmates in your class?", file: "aula3_do_you_have_many_classmates.mp3", voice: ARTHUR },
  { text: "What is your favorite thing about school?", file: "aula3_what_is_your_favorite_thing.mp3", voice: ELLEN },
  { text: "The teacher gave us a big assignment for the weekend.", file: "aula3_the_teacher_gave_us.mp3", voice: ARTHUR },
  { text: "We have a short break after every two classes.", file: "aula3_we_have_a_short_break.mp3", voice: ELLEN },
  { text: "Does Carolina attend school every day?", file: "aula3_does_carolina_attend.mp3", voice: ARTHUR },
  { text: "I always participate in class discussions.", file: "aula3_i_always_participate.mp3", voice: ELLEN },
  { text: "During recess, I play with my friends.", file: "aula3_during_recess_i_play.mp3", voice: ARTHUR },

  // ===== Grammar discovery sentences (alternate) =====
  { text: "Do you like English?", file: "aula3_do_you_like_english.mp3", voice: ELLEN },
  { text: "Does she play handball?", file: "aula3_does_she_play_handball.mp3", voice: ARTHUR },
  { text: "Do they have a break at ten?", file: "aula3_do_they_have_a_break.mp3", voice: ELLEN },
  { text: "Does your teacher give homework every day?", file: "aula3_does_your_teacher_give.mp3", voice: ARTHUR },

  // ===== Dialogue — Noah (ARTHUR) and Carolina (ELLEN) =====
  { text: "Hi Carolina! I am visiting your school today. What subjects do you have?", file: "aula3_dialogue_noah_1.mp3", voice: ARTHUR },
  { text: "Hi Noah! We have English, math, science, and Portuguese. My favorite subject is English.", file: "aula3_dialogue_carolina_1.mp3", voice: ELLEN },
  { text: "That is cool! Do your classmates like English too?", file: "aula3_dialogue_noah_2.mp3", voice: ARTHUR },
  { text: "Some do, some do not. Most of them like recess the best!", file: "aula3_dialogue_carolina_2.mp3", voice: ELLEN },
  { text: "Do you have many assignments every day?", file: "aula3_dialogue_noah_3.mp3", voice: ARTHUR },
  { text: "Yes, our teachers give us assignments almost every day. I always participate in class to understand better.", file: "aula3_dialogue_carolina_3.mp3", voice: ELLEN },
  { text: "Does your school have long breaks between classes?", file: "aula3_dialogue_noah_4.mp3", voice: ARTHUR },
  { text: "We have a ten-minute break after every two classes. I usually talk with my classmates during break.", file: "aula3_dialogue_carolina_4.mp3", voice: ELLEN },

  // ===== Listening 1 — Lily (ELLEN, female) =====
  { text: "Hi, my name is Lily. I am thirteen and I go to school in Sydney.", file: "aula3_listening1_lily.mp3", voice: ELLEN },
  { text: "My favorite subject is art. I attend school five days a week. I always participate in class. We have a twenty-minute recess after the third class. I love recess because I play with my classmates. My teachers give us assignments every day, but I do not mind because I like learning.", file: "aula3_listening1_full.mp3", voice: ELLEN },

  // ===== Listening 2 — James (ARTHUR, male) =====
  { text: "Good morning! My name is James. I am fourteen and I go to school in London.", file: "aula3_listening2_james.mp3", voice: ARTHUR },
  { text: "I have many subjects at school, but my favorite is science. I attend all my classes and I usually participate. We have two breaks during the day. My classmates and I play football during recess. Our teachers give us many assignments, especially in math. I sometimes do my assignments during break.", file: "aula3_listening2_full.mp3", voice: ARTHUR },

  // ===== Survival card (Carolina = ELLEN) =====
  { text: "Do you have English class today?", file: "aula3_survival_1.mp3", voice: ELLEN },
  { text: "What time does the break start?", file: "aula3_survival_3.mp3", voice: ELLEN },
  { text: "I always participate in class.", file: "aula3_survival_4.mp3", voice: ELLEN },
  { text: "Does your school have a long recess?", file: "aula3_survival_5.mp3", voice: ELLEN },

  // ===== Speech cards (Carolina = ELLEN) =====
  { text: "I attend school five days a week and my favorite subject is English.", file: "aula3_speech_1.mp3", voice: ELLEN },
  { text: "Do you have many classmates in your class? I have about thirty.", file: "aula3_speech_2.mp3", voice: ELLEN },
  { text: "Our teachers give us assignments every day, but I always do them on time.", file: "aula3_speech_3.mp3", voice: ELLEN },
  { text: "We have a short break after every two classes and a long recess at noon.", file: "aula3_speech_4.mp3", voice: ELLEN },
  { text: "I always participate in class because it helps me learn better.", file: "aula3_speech_5.mp3", voice: ELLEN },

  // ===== Fill-in-blank sentences (alternate) =====
  { text: "I attend English class on Mondays and Wednesdays.", file: "aula3_fill_1.mp3", voice: ELLEN },
  { text: "Does she participate in all the class discussions?", file: "aula3_fill_2.mp3", voice: ARTHUR },
  { text: "My favorite subject at school is English.", file: "aula3_fill_3.mp3", voice: ELLEN },
  { text: "Do your classmates like the new teacher?", file: "aula3_fill_4.mp3", voice: ARTHUR },
  { text: "The teacher gave us a difficult assignment for homework.", file: "aula3_fill_5.mp3", voice: ELLEN },

  // ===== Ordering audio =====
  { text: "First, I attend my first class at eight o'clock. Then, we have a short break after two classes. After that, I participate in class discussions. During recess, I play with my classmates. Finally, I do my assignments after school.", file: "aula3_order_l3.mp3", voice: ELLEN },

  // ===== Grammar practice sentences (alternate) =====
  { text: "Does she play handball at school?", file: "aula3_does_she_play_handball_school.mp3", voice: ARTHUR },
  { text: "Do your classmates attend every class?", file: "aula3_do_classmates_attend.mp3", voice: ELLEN },
  { text: "Does the teacher give assignments on Fridays?", file: "aula3_does_teacher_give.mp3", voice: ARTHUR },
  { text: "Do you participate in group activities?", file: "aula3_do_you_participate.mp3", voice: ELLEN },
  { text: "Does Carolina like recess?", file: "aula3_does_carolina_like_recess.mp3", voice: ARTHUR },
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
      model_id: 'eleven_monolingual_v1',
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
  console.log(`Generating ${PHRASES.length} audio files for Carolina Aula 3...`);
  for (const p of PHRASES) {
    await generate(p.text, p.file, p.voice);
    await new Promise(r => setTimeout(r, 350));
  }
  console.log('Done!');
}

main().catch(console.error);
