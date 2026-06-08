#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = {
  ash: 'VU16byTywsWv5JpI8rbc',    // Male neutral
  riley: 'hA4zGnmTwX2NQiTRMt7o'   // Female neutral
};
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-de-andrade-brandao');

// Voice assignment rules:
// - Rafael is MALE → vocab words (1-2 words) = Ash
// - Phrases 3+ words = ALTERNATE Ash/Riley
// - Dialogue: Lisa Park (female) = Riley, Rafael (male) = Ash
// - Listening 1 (male speaker David) = Ash, Listening 2 (female speaker Maria) = Riley

const PHRASES = [
  // ===== Survival phrases (alternate Ash/Riley) =====
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: VOICES.ash },
  { text: "I am not sure I understand. Could you explain?", file: "i_am_not_sure_i_understand_could_you_explain.mp3", voice: VOICES.riley },
  { text: "Let me think about that for a moment.", file: "let_me_think_about_that_for_a_moment.mp3", voice: VOICES.ash },
  { text: "How do you say that in English?", file: "how_do_you_say_that_in_english.mp3", voice: VOICES.riley },
  { text: "Could you speak more slowly, please?", file: "could_you_speak_more_slowly_please.mp3", voice: VOICES.ash },

  // ===== Vocab words (Rafael is MALE → Ash) =====
  { text: "Introduce", file: "introduce.mp3", voice: VOICES.ash },
  { text: "Role", file: "role.mp3", voice: VOICES.ash },
  { text: "Responsible", file: "responsible.mp3", voice: VOICES.ash },
  { text: "Currently", file: "currently.mp3", voice: VOICES.ash },
  { text: "Team", file: "team.mp3", voice: VOICES.ash },
  { text: "Deal with", file: "deal_with.mp3", voice: VOICES.ash },
  { text: "Complex", file: "complex.mp3", voice: VOICES.ash },
  { text: "Client", file: "client.mp3", voice: VOICES.ash },

  // ===== Vocab example sentences (alternate Ash/Riley) =====
  { text: "Let me introduce myself. I am Rafael from TVT.", file: "let_me_introduce_myself_i_am_rafael_from_tvt.mp3", voice: VOICES.ash },
  { text: "My role at TVT is Commercial Director.", file: "my_role_at_tvt_is_commercial_director.mp3", voice: VOICES.riley },
  { text: "I am responsible for the sales team.", file: "i_am_responsible_for_the_sales_team.mp3", voice: VOICES.ash },
  { text: "I currently work in São Paulo.", file: "i_currently_work_in_sao_paulo.mp3", voice: VOICES.riley },
  { text: "My team has ten experienced people.", file: "my_team_has_ten_experienced_people.mp3", voice: VOICES.ash },
  { text: "I deal with technology clients every day.", file: "i_deal_with_technology_clients_every_day.mp3", voice: VOICES.riley },
  { text: "Our sales process is complex and technical.", file: "our_sales_process_is_complex_and_technical.mp3", voice: VOICES.ash },
  { text: "My clients are large international companies.", file: "my_clients_are_large_international_companies.mp3", voice: VOICES.riley },

  // ===== Dialogue: Lisa Park (female = Riley), Rafael (male = Ash) =====
  { text: "Hello! I am Lisa Park, VP of Strategic Partnerships at TechGlobal. Nice to meet you!", file: "hello_i_am_lisa_park_vp_of_strategic_partnerships.mp3", voice: VOICES.riley },
  { text: "Nice to meet you, Lisa! I am Rafael Brandão. I work at TVT here in São Paulo.", file: "nice_to_meet_you_lisa_i_am_rafael_brandao.mp3", voice: VOICES.ash },
  { text: "TVT? What is your role there?", file: "tvt_what_is_your_role_there.mp3", voice: VOICES.riley },
  { text: "I am the Commercial Director. I am responsible for the sales team.", file: "i_am_the_commercial_director_i_am_responsible.mp3", voice: VOICES.ash },
  { text: "Interesting! What kind of clients do you deal with?", file: "interesting_what_kind_of_clients_do_you_deal_with.mp3", voice: VOICES.riley },
  { text: "We deal with complex technology sales. Our clients are large companies.", file: "we_deal_with_complex_technology_sales.mp3", voice: VOICES.ash },
  { text: "That sounds challenging. Do you enjoy it?", file: "that_sounds_challenging_do_you_enjoy_it.mp3", voice: VOICES.riley },
  { text: "Absolutely! I love working with my team. We currently have some exciting projects.", file: "absolutely_i_love_working_with_my_team.mp3", voice: VOICES.ash },

  // ===== Practice sentences (Rafael as protagonist = Ash, alternate for general) =====
  { text: "I work at TVT in São Paulo.", file: "i_work_at_tvt_in_sao_paulo.mp3", voice: VOICES.ash },
  { text: "I am the Commercial Director at TVT.", file: "i_am_the_commercial_director_at_tvt.mp3", voice: VOICES.riley },
  { text: "I manage a team of ten people.", file: "i_manage_a_team_of_ten_people.mp3", voice: VOICES.ash },
  { text: "We sell technology solutions to large companies.", file: "we_sell_technology_solutions_to_large_companies.mp3", voice: VOICES.riley },

  // ===== Listening 1 (male speaker David = Ash) — full passage =====
  { text: "Good morning, everyone. My name is Rafael Brandão. I am the Commercial Director at TVT, a technology company based in São Paulo. I am responsible for the sales team. We deal with complex technology sales. Our clients are large international companies. I currently manage a team of ten experienced people.", file: "good_morning_everyone_my_name_is_rafael_brandao.mp3", voice: VOICES.ash },

  // ===== Additional practice sentences (alternate Ash/Riley) =====
  { text: "My name is Rafael Brandão and I work at TVT.", file: "my_name_is_rafael_brandao_and_i_work_at_tvt.mp3", voice: VOICES.ash },
  { text: "I am responsible for the sales department.", file: "i_am_responsible_for_the_sales_department.mp3", voice: VOICES.riley },
  { text: "We currently have ten people on the team.", file: "we_currently_have_ten_people_on_the_team.mp3", voice: VOICES.ash },
  { text: "Our clients are large technology companies.", file: "our_clients_are_large_technology_companies.mp3", voice: VOICES.riley },
  { text: "I deal with complex sales every day.", file: "i_deal_with_complex_sales_every_day.mp3", voice: VOICES.ash },

  // ===== Speech practice (Rafael = Ash) =====
  { text: "Let me introduce myself. I am Rafael Brandão.", file: "let_me_introduce_myself_i_am_rafael_brandao.mp3", voice: VOICES.ash },
  { text: "I work as Commercial Director at TVT.", file: "i_work_as_commercial_director_at_tvt.mp3", voice: VOICES.riley },
  { text: "My team deals with technology clients.", file: "my_team_deals_with_technology_clients.mp3", voice: VOICES.ash },
  { text: "The sales process is complex but exciting.", file: "the_sales_process_is_complex_but_exciting.mp3", voice: VOICES.riley },
  { text: "I enjoy working with international clients.", file: "i_enjoy_working_with_international_clients.mp3", voice: VOICES.ash },

  // ===== Additional IN CLASS phrases =====
  { text: "I am Rafael Brandão. I am the Commercial Director at TVT.", file: "i_am_rafael_brandao_i_am_the_commercial_director.mp3", voice: VOICES.ash },
  { text: "Let me introduce myself. I am Rafael Brandão, the Commercial Director at TVT.", file: "let_me_introduce_myself_rafael_commercial_director.mp3", voice: VOICES.ash },
  { text: "My team has ten experienced people. We deal with complex technology sales.", file: "my_team_has_ten_experienced_we_deal_complex.mp3", voice: VOICES.riley },
  { text: "Our clients are large international companies.", file: "our_clients_are_large_international_companies.mp3", voice: VOICES.ash },

  // ===== Ordering exercise — complete ordered sentence =====
  { text: "Good morning. My name is Rafael Brandão. I am the Commercial Director at TVT in São Paulo.", file: "order_l1_ordering.mp3", voice: VOICES.ash },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch(API_URL + '/' + voiceId, {
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
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const seen = new Set();
  const unique = PHRASES.filter(p => {
    const k = p.file.toLowerCase();
    if (seen.has(k)) return false;
    seen.add(k);
    return true;
  });

  console.log('Generating ' + unique.length + ' audio files for Rafael de Andrade Brandão...');
  let generated = 0;
  let skipped = 0;

  for (const p of unique) {
    const outPath = path.join(OUTPUT_DIR, p.file);
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
