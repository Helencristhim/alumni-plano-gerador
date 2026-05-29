const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'marlene-landucci');

// Marlene = female → Ellen for her lines, vocab, survival, exercises
// Tom = male → Arthur for his dialogue lines
// General grammar examples: alternate Arthur/Ellen
const PHRASES = [
  // ===== Survival / Emergency phrases (Marlene = Ellen) =====
  { text: "Could you repeat that, please?", voice: ELLEN, file: "could_you_repeat_that_please.mp3" },
  { text: "I do not understand.", voice: ELLEN, file: "i_do_not_understand.mp3" },
  { text: "How do you say this in English?", voice: ELLEN, file: "how_do_you_say_this_in_english.mp3" },
  { text: "Could you speak slowly, please?", voice: ELLEN, file: "could_you_speak_slowly_please.mp3" },
  { text: "Nice to meet you.", voice: ELLEN, file: "nice_to_meet_you.mp3" },

  // ===== Vocab words (single words — Ellen for female student) =====
  { text: "Introduce", voice: ELLEN, file: "introduce.mp3" },
  { text: "Travel", voice: ELLEN, file: "travel.mp3" },
  { text: "Property", voice: ELLEN, file: "property.mp3" },
  { text: "Manage", voice: ELLEN, file: "manage.mp3" },
  { text: "Hobby", voice: ELLEN, file: "hobby.mp3" },
  { text: "Nationality", voice: ELLEN, file: "nationality.mp3" },
  { text: "Currently", voice: ELLEN, file: "currently.mp3" },
  { text: "Independent", voice: ELLEN, file: "independent.mp3" },

  // ===== Vocab example sentences (Marlene context = Ellen) =====
  { text: "Let me introduce myself. I am Marlene.", voice: ELLEN, file: "let_me_introduce_myself_i_am_marlene.mp3" },
  { text: "I love to travel to Italy and Turkey.", voice: ELLEN, file: "i_love_to_travel_to_italy_and_turkey.mp3" },
  { text: "I manage properties in São Paulo.", voice: ELLEN, file: "i_manage_properties_in_sao_paulo.mp3" },
  { text: "She manages her own business.", voice: ELLEN, file: "she_manages_her_own_business.mp3" },
  { text: "Tennis is my favorite hobby.", voice: ELLEN, file: "tennis_is_my_favorite_hobby.mp3" },
  { text: "My nationality is Brazilian.", voice: ELLEN, file: "my_nationality_is_brazilian.mp3" },
  { text: "I currently live in São Paulo.", voice: ELLEN, file: "i_currently_live_in_sao_paulo.mp3" },
  { text: "I want to be an independent traveler.", voice: ELLEN, file: "i_want_to_be_an_independent_traveler.mp3" },

  // ===== Grammar examples — "to be" conjugation (alternate Arthur/Ellen) =====
  { text: "I am from Brazil. I am Brazilian.", voice: ELLEN, file: "i_am_from_brazil_i_am_brazilian.mp3" },
  { text: "She is a property manager in São Paulo.", voice: ELLEN, file: "she_is_a_property_manager_in_sao_paulo.mp3" },
  { text: "We are planning a trip to Italy.", voice: ELLEN, file: "we_are_planning_a_trip_to_italy.mp3" },
  { text: "He is from Turkey. He is Turkish.", voice: ARTHUR, file: "he_is_from_turkey_he_is_turkish.mp3" },
  { text: "They are independent travelers.", voice: ELLEN, file: "they_are_independent_travelers.mp3" },
  { text: "I am currently learning English.", voice: ELLEN, file: "i_am_currently_learning_english.mp3" },
  { text: "She is a teacher.", voice: ARTHUR, file: "she_is_a_teacher.mp3" },
  { text: "We are travelers.", voice: ELLEN, file: "we_are_travelers.mp3" },
  { text: "He is from England.", voice: ARTHUR, file: "he_is_from_england.mp3" },
  { text: "They are at the airport.", voice: ARTHUR, file: "they_are_at_the_airport.mp3" },
  { text: "It is a beautiful day.", voice: ARTHUR, file: "it_is_a_beautiful_day.mp3" },

  // ===== Fill-in / Practice sentences (Marlene context = Ellen) =====
  { text: "Hi, my name is Marlene. I am from Brazil.", voice: ELLEN, file: "hi_my_name_is_marlene_i_am_from_brazil.mp3" },
  { text: "I manage properties in São Paulo and Americana.", voice: ELLEN, file: "i_manage_properties_in_sao_paulo_and_americana.mp3" },
  { text: "I love to travel. I am planning a trip to Italy.", voice: ELLEN, file: "i_love_to_travel_i_am_planning_a_trip_to_italy.mp3" },

  // ===== Speech cards / Pronunciation (Marlene = Ellen) =====
  { text: "My name is Marlene.", voice: ELLEN, file: "my_name_is_marlene.mp3" },
  { text: "I am from Brazil.", voice: ELLEN, file: "i_am_from_brazil.mp3" },
  { text: "I do not speak English very well.", voice: ELLEN, file: "i_do_not_speak_english_very_well.mp3" },

  // ===== Dialogue — Tom (male) = Arthur =====
  { text: "Hi there! Are you traveling to Italy too?", voice: ARTHUR, file: "hi_there_are_you_traveling_to_italy_too.mp3" },
  { text: "Nice to meet you, Marlene! I am Tom. I am from England.", voice: ARTHUR, file: "nice_to_meet_you_marlene_i_am_tom_i_am_from_england.mp3" },
  { text: "That is wonderful! What do you do in Brazil?", voice: ARTHUR, file: "that_is_wonderful_what_do_you_do_in_brazil.mp3" },
  { text: "I am a teacher. I travel every year. It is my hobby!", voice: ARTHUR, file: "i_am_a_teacher_i_travel_every_year_it_is_my_hobby.mp3" },

  // ===== Dialogue — Marlene (female) = Ellen =====
  { text: "Yes! I am Marlene. I am from Brazil.", voice: ELLEN, file: "yes_i_am_marlene_i_am_from_brazil.mp3" },
  { text: "Nice to meet you, Tom! This is my first trip alone.", voice: ELLEN, file: "nice_to_meet_you_tom_this_is_my_first_trip_alone.mp3" },
  { text: "I manage properties in São Paulo. And you?", voice: ELLEN, file: "i_manage_properties_in_sao_paulo_and_you.mp3" },
  { text: "I love traveling! I am currently learning English for my trips.", voice: ELLEN, file: "i_love_traveling_i_am_currently_learning_english.mp3" },

  // ===== Listening 1 — Airport announcement (Ellen voice) =====
  { text: "Good afternoon, ladies and gentlemen. Welcome to Leonardo da Vinci International Airport in Rome. Flight AL0050 from São Paulo has arrived at Gate B7. All passengers, please proceed to baggage claim area three. If you need assistance, please ask any airport staff member. We wish you a pleasant stay in Italy. Thank you.", voice: ELLEN, file: "lp_listen1_airport_announcement.mp3" },

  // ===== Listening 2 — Marlene's full self-introduction (Ellen voice) =====
  { text: "Hello, everyone. My name is Marlene Landucci. I am from Brazil. I currently live in São Paulo, but I also have a home in Americana. I am a veterinarian by training, but now I manage my own properties. My hobbies are tennis and walking. I love to travel, and I am planning trips to Italy and Turkey. I am learning English because I want to be an independent traveler. Nice to meet you all.", voice: ELLEN, file: "lp_listen2_self_introduction.mp3" },

  // ===== Ordering exercise — correct self-introduction (Ellen voice) =====
  { text: "Hi, my name is Marlene. I am from Brazil. I manage properties in São Paulo. I love to travel. Nice to meet you!", voice: ELLEN, file: "order_l1_self_introduction.mp3" },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: {
        stability: 0.5,
        similarity_boost: 0.75,
        style: 0.0,
        use_speaker_boost: true
      }
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
  const unique = PHRASES.filter(p => { const k = p.text.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });

  console.log('Generating ' + unique.length + ' audio files for Marlene Landucci — Aula 1...');
  let generated = 0;
  let skipped = 0;
  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) {
      console.log('SKIP: ' + p.file);
      skipped++;
    } else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes/1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch(e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total entries: ' + unique.length);
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
