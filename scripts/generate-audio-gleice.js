const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'gleice-leonardo-rocha-de-souza');

// Voice rules:
// - Gleice is FEMALE → her lines/exercises = ELLEN
// - Mark Thompson is MALE → his lines = ARTHUR
// - Single words = ELLEN (student gender)
// - General phrases = ALTERNATE Arthur/Ellen

const PHRASES = [
  // ===== Emergency phrases (alternate) =====
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: ARTHUR },
  { text: "I do not understand. Could you explain?", file: "i_do_not_understand_could_you_explain.mp3", voice: ELLEN },
  { text: "Let me think about that for a moment.", file: "let_me_think_about_that_for_a_moment.mp3", voice: ARTHUR },
  { text: "That is a great question.", file: "that_is_a_great_question.mp3", voice: ELLEN },
  { text: "In my experience, I would say...", file: "in_my_experience_i_would_say.mp3", voice: ARTHUR },

  // ===== Vocab words (Gleice is female → ELLEN) =====
  { text: "Manage", file: "manage.mp3", voice: ELLEN },
  { text: "Lead", file: "lead.mp3", voice: ELLEN },
  { text: "Represent", file: "represent.mp3", voice: ELLEN },
  { text: "Industry", file: "industry.mp3", voice: ELLEN },
  { text: "Role", file: "role.mp3", voice: ELLEN },
  { text: "Project", file: "project.mp3", voice: ELLEN },
  { text: "Goal", file: "goal.mp3", voice: ELLEN },
  { text: "Challenge", file: "challenge.mp3", voice: ELLEN },

  // ===== Vocab example sentences (Gleice context = ELLEN) =====
  { text: "I manage a team of thirty-four people at Sanofi Medley.", file: "i_manage_a_team_of_thirty_four_people_at_sanofi.mp3", voice: ELLEN },
  { text: "Gleice leads the Commercial Excellence department.", file: "gleice_leads_the_commercial_excellence_dept.mp3", voice: ELLEN },
  { text: "I want to represent international brands in Brazil.", file: "i_want_to_represent_international_brands.mp3", voice: ELLEN },
  { text: "The pharmaceutical industry is very competitive.", file: "the_pharmaceutical_industry_is_very_competitive.mp3", voice: ARTHUR },
  { text: "My role is to improve commercial processes.", file: "my_role_is_to_improve_commercial_processes.mp3", voice: ELLEN },
  { text: "I have a new project to contact brands abroad.", file: "i_have_a_new_project_to_contact_brands_abroad.mp3", voice: ELLEN },
  { text: "My goal is to speak English with confidence.", file: "my_goal_is_to_speak_english_with_confidence.mp3", voice: ELLEN },
  { text: "The biggest challenge is speaking in real time.", file: "the_biggest_challenge_is_speaking_in_real_time.mp3", voice: ARTHUR },

  // ===== Fill-in sentences (alternate) =====
  { text: "I manage a team of thirty-four people.", file: "i_manage_a_team_of_thirty_four_people.mp3", voice: ELLEN },
  { text: "My goal is to represent international brands.", file: "my_goal_is_to_represent_international_brands.mp3", voice: ELLEN },
  { text: "She leads the Commercial Excellence team.", file: "she_leads_the_commercial_excellence_team.mp3", voice: ARTHUR },
  { text: "The pharmaceutical industry is growing fast.", file: "the_pharmaceutical_industry_is_growing_fast.mp3", voice: ELLEN },
  { text: "My biggest challenge is speaking in real time.", file: "my_biggest_challenge_is_speaking_in_real_time.mp3", voice: ARTHUR },

  // ===== Speech practice (Gleice = ELLEN) =====
  { text: "My name is Gleice. I am from Santo Andre, Brazil.", file: "my_name_is_gleice_i_am_from_santo_andre.mp3", voice: ELLEN },
  { text: "I work in the pharmaceutical industry.", file: "i_work_in_the_pharmaceutical_industry.mp3", voice: ELLEN },
  { text: "My name is Gleice. I am from Santo Andre.", file: "my_name_is_gleice_i_am_from_santo_andre_short.mp3", voice: ELLEN },

  // ===== Dialogue — Mark Thompson (male = ARTHUR), Gleice (female = ELLEN) =====
  { text: "Hi! I am Mark Thompson from PharmaTrade UK. Are you in the pharmaceutical industry too?", file: "dialogue_mark_1.mp3", voice: ARTHUR },
  { text: "Yes! I am Gleice. I manage the Commercial Excellence team at Sanofi Medley in Brazil.", file: "dialogue_gleice_1.mp3", voice: ELLEN },
  { text: "Interesting! What does your team do?", file: "dialogue_mark_2.mp3", voice: ARTHUR },
  { text: "We lead transformation projects. My role is to improve commercial processes.", file: "dialogue_gleice_2.mp3", voice: ELLEN },
  { text: "That sounds challenging. How big is your team?", file: "dialogue_mark_3.mp3", voice: ARTHUR },
  { text: "I lead a team of thirty-four people. It is a big challenge, but I love it.", file: "dialogue_gleice_3.mp3", voice: ELLEN },
  { text: "Impressive! Do you have any projects with international partners?", file: "dialogue_mark_4.mp3", voice: ARTHUR },
  { text: "Yes! My goal is to represent international brands in the Brazilian market.", file: "dialogue_gleice_4.mp3", voice: ELLEN },

  // ===== Grammar examples (alternate) =====
  { text: "I manage a large team.", file: "grammar_i_manage_a_large_team.mp3", voice: ELLEN },
  { text: "She leads the department.", file: "grammar_she_leads_the_department.mp3", voice: ARTHUR },
  { text: "We represent international brands.", file: "grammar_we_represent_intl_brands.mp3", voice: ELLEN },
  { text: "They work in the pharmaceutical industry.", file: "grammar_they_work_in_pharma.mp3", voice: ARTHUR },

  // ===== Listening 1 — Gleice full intro (ELLEN) =====
  { text: "Good morning. My name is Gleice Leonardo Rocha de Souza. I am from Santo Andre, Brazil. I manage a team of thirty-four people at Sanofi Medley. My role is Commercial Excellence Manager. I lead transformation projects in the pharmaceutical industry. I have a new goal. I want to represent international brands in Brazil. It is a big challenge, but I am ready.", file: "listening1_full_introduction.mp3", voice: ELLEN },

  // ===== Listening 2 — Mark intro (ARTHUR) =====
  { text: "Hello everyone. My name is Mark Thompson. I work at PharmaTrade UK. We represent pharmaceutical brands in the European market. Our team has twenty people. We manage partnerships with companies in ten countries. My role is Business Development Manager. Our biggest challenge is finding the right partners in new markets.", file: "listening2_mark_introduction.mp3", voice: ARTHUR },

  // ===== Order exercise (ELLEN) =====
  { text: "Good morning. My name is Gleice. I am from Santo Andre, Brazil. I manage a team of thirty-four people. I work in the pharmaceutical industry. My goal is to represent international brands in Brazil.", file: "order_l1_self_introduction.mp3", voice: ELLEN },

  // ===== Survival card IN CLASS (ELLEN) =====
  { text: "Let me introduce myself. I am Gleice.", file: "survival_ic_1.mp3", voice: ELLEN },
  { text: "I manage the Commercial Excellence team.", file: "survival_ic_2.mp3", voice: ELLEN },
  { text: "My role is to lead transformation projects.", file: "survival_ic_3.mp3", voice: ELLEN },
  { text: "I work in the pharmaceutical industry in Brazil.", file: "survival_ic_4.mp3", voice: ELLEN },
  { text: "My goal is to represent international brands.", file: "survival_ic_5.mp3", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Gleice Leonardo Rocha de Souza...');
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
      console.log('  OK (' + (size / 1024).toFixed(1) + 'KB): ' + p.file + ' [' + (p.voice === ARTHUR ? 'Arthur' : 'Ellen') + ']');
      // Rate limit: ~2 requests/second
      await new Promise(resolve => setTimeout(resolve, 500));
    } catch (err) {
      console.error('  FAIL: ' + p.file + ' → ' + err.message);
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total: ' + unique.length);
}

main().catch(console.error);
