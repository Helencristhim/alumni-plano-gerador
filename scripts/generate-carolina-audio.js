const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'carolina-paludetto-rodrigues');

// Voice rules:
// - Carolina is FEMALE → her lines/exercises = ELLEN
// - Alex (exchange student) is MALE → his lines = ARTHUR
// - Single words = ELLEN (student gender)
// - General phrases = ALTERNATE Arthur/Ellen

const PHRASES = [
  // ===== Vocab words (Carolina is female → ELLEN) =====
  { text: "Introduce", file: "introduce.mp3", voice: ELLEN },
  { text: "Describe", file: "describe.mp3", voice: ELLEN },
  { text: "Struggle", file: "struggle.mp3", voice: ELLEN },
  { text: "Grade", file: "grade.mp3", voice: ELLEN },
  { text: "Goal", file: "goal.mp3", voice: ELLEN },
  { text: "Creative", file: "creative.mp3", voice: ELLEN },
  { text: "Improve", file: "improve.mp3", voice: ELLEN },
  { text: "Confident", file: "confident.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate) =====
  { text: "Let me introduce myself. I am Carolina.", file: "let_me_introduce_myself_i_am_carolina.mp3", voice: ELLEN },
  { text: "Can you describe your favorite book?", file: "can_you_describe_your_favorite_book.mp3", voice: ARTHUR },
  { text: "I struggle with English grammar sometimes.", file: "i_struggle_with_english_grammar_sometimes.mp3", voice: ELLEN },
  { text: "My grades are great in most subjects.", file: "my_grades_are_great_in_most_subjects.mp3", voice: ELLEN },
  { text: "My goal is to improve my English this year.", file: "my_goal_is_to_improve_my_english_this_year.mp3", voice: ARTHUR },
  { text: "She is a very creative person who writes stories.", file: "she_is_a_very_creative_person_who_writes_stories.mp3", voice: ARTHUR },
  { text: "I want to improve my vocabulary every week.", file: "i_want_to_improve_my_vocabulary_every_week.mp3", voice: ELLEN },
  { text: "I feel more confident when I practice speaking.", file: "i_feel_more_confident_when_i_practice_speaking.mp3", voice: ELLEN },

  // ===== Speech practice (Carolina = ELLEN) =====
  { text: "Hi, my name is Carolina. Nice to meet you.", file: "hi_my_name_is_carolina_nice_to_meet_you.mp3", voice: ELLEN },
  { text: "I am a student at Colegio Saint Louis.", file: "i_am_a_student_at_colegio_saint_louis.mp3", voice: ELLEN },
  { text: "I am good at writing stories.", file: "i_am_good_at_writing_stories.mp3", voice: ELLEN },
  { text: "I struggle with English grammar.", file: "i_struggle_with_english_grammar.mp3", voice: ELLEN },
  { text: "My goal is to speak English confidently.", file: "my_goal_is_to_speak_english_confidently.mp3", voice: ELLEN },

  // ===== Survival card (alternate) =====
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: ARTHUR },
  { text: "How do you say this in English?", file: "how_do_you_say_this_in_english.mp3", voice: ELLEN },
  { text: "I am not sure I understand.", file: "i_am_not_sure_i_understand.mp3", voice: ARTHUR },
  { text: "Could you speak more slowly?", file: "could_you_speak_more_slowly.mp3", voice: ELLEN },
  { text: "I am good at writing, but I struggle with speaking.", file: "i_am_good_at_writing_but_i_struggle_with_speaking.mp3", voice: ELLEN },

  // ===== Dialogue — Alex (male = ARTHUR), Carolina (female = ELLEN) =====
  { text: "Hi! I am Alex, a new exchange student. What is your name?", file: "hi_i_am_alex_a_new_exchange_student_what_is_your_name.mp3", voice: ARTHUR },
  { text: "Hi! I am Carolina. Welcome to our school!", file: "hi_i_am_carolina_welcome_to_our_school.mp3", voice: ELLEN },
  { text: "Thanks! What do you like to do after school?", file: "thanks_what_do_you_like_to_do_after_school.mp3", voice: ARTHUR },
  { text: "I play handball and I write stories.", file: "i_play_handball_and_i_write_stories.mp3", voice: ELLEN },
  { text: "That sounds great! Are you good at sports?", file: "that_sounds_great_are_you_good_at_sports.mp3", voice: ARTHUR },
  { text: "I am good at handball, but I struggle with English.", file: "i_am_good_at_handball_but_i_struggle_with_english.mp3", voice: ELLEN },
  { text: "Do not worry. What is your goal for English?", file: "do_not_worry_what_is_your_goal_for_english.mp3", voice: ARTHUR },
  { text: "I want to improve and feel more confident speaking.", file: "i_want_to_improve_and_feel_more_confident_speaking.mp3", voice: ELLEN },

  // ===== Fill-in phrases =====
  { text: "I struggle with English at school.", file: "i_struggle_with_english_at_school.mp3", voice: ELLEN },
  { text: "She is very creative. She writes stories.", file: "she_is_very_creative_she_writes_stories.mp3", voice: ARTHUR },
  { text: "My goal is to improve my grades.", file: "my_goal_is_to_improve_my_grades.mp3", voice: ELLEN },

  // ===== Grammar/oral drilling =====
  { text: "Let me introduce myself. I am Carolina Paludetto Rodrigues.", file: "let_me_introduce_myself_i_am_carolina_paludetto_rodrigues.mp3", voice: ELLEN },
  { text: "My name is Carolina Paludetto Rodrigues.", file: "my_name_is_carolina_paludetto_rodrigues.mp3", voice: ELLEN },
  { text: "I play handball twice a week.", file: "i_play_handball_twice_a_week.mp3", voice: ELLEN },
  { text: "My goal is to improve my English.", file: "my_goal_is_to_improve_my_english.mp3", voice: ELLEN },
  { text: "I am a creative student who loves writing and handball.", file: "i_am_a_creative_student_who_loves_writing_and_handball.mp3", voice: ELLEN },
  { text: "I am Carolina. I describe myself as creative and determined.", file: "i_am_carolina_i_describe_myself_as_creative_and_determined.mp3", voice: ELLEN },

  // ===== Grammar practice (IN CLASS) =====
  { text: "Carolina plays handball every week.", file: "carolina_plays_handball_every_week.mp3", voice: ARTHUR },
  { text: "She doesn't like math tests.", file: "she_doesnt_like_math_tests.mp3", voice: ARTHUR },
  { text: "Do you write stories?", file: "do_you_write_stories.mp3", voice: ARTHUR },
  { text: "I am good at writing.", file: "i_am_good_at_writing.mp3", voice: ELLEN },

  // ===== Context text (listening) =====
  { text: "Hi, my name is Maya. I am fifteen years old and I live in London.", file: "hi_my_name_is_maya_i_am_fifteen_years_old.mp3", voice: ELLEN },
  { text: "I am good at drawing and I love art class. I struggle with science, but my goal is to improve this year.", file: "i_am_good_at_drawing_and_i_love_art_class.mp3", voice: ELLEN },
  { text: "I am a very creative person. I describe myself as curious and friendly. I want to feel more confident speaking in front of the class.", file: "i_am_a_very_creative_person_i_describe_myself.mp3", voice: ELLEN },

  // ===== Listening 1 — student intro (longer audio) =====
  { text: "Hi everyone! My name is Sofia. I am fourteen years old and I am from Madrid, Spain. I go to an international school. I am good at swimming and reading. I love adventure books, especially The Hunger Games. I struggle with history because there are so many dates to remember. My goal is to improve my history grades this semester. My friends describe me as creative and confident. I want to introduce myself to more students from other countries.", file: "listening1_student_intro.mp3", voice: ELLEN },

  // ===== Listening 2 — hobbies interview (longer audio) =====
  { text: "My name is Lucas. I am thirteen years old. I play soccer three times a week. I am good at sports, but I struggle with English. My grades in English are not great. My goal is to improve my English so I can talk to players from other countries. I don't feel confident speaking English yet, but I want to improve. My friends describe me as creative because I like to draw plays on the whiteboard.", file: "listening2_hobbies_interview.mp3", voice: ARTHUR },

  // ===== Ordering exercise =====
  { text: "Hi! Let me introduce myself. My name is Carolina. I am a student at Colegio Saint Louis in Sao Paulo. I am good at writing stories and playing handball. I struggle with English, but my goal is to improve. I want to feel more confident speaking English.", file: "order_l1_self_introduction.mp3", voice: ELLEN },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => {
    const k = p.file.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' audio files for Carolina Paludetto Rodrigues...');
  let generated = 0;
  let skipped = 0;

  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('  SKIP (exists): ' + p.file);
      skipped++;
      continue;
    }
    try {
      const size = await gen(p.text, p.voice, outPath);
      generated++;
      console.log('  OK: ' + p.file + ' (' + Math.round(size / 1024) + ' KB)');
      // Rate limit: wait 500ms between calls
      await new Promise(r => setTimeout(r, 500));
    } catch (e) {
      console.error('  FAIL: ' + p.file + ' - ' + e.message);
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + unique.length);
}

main();
