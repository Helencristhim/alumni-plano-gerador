#!/usr/bin/env node
const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = { ash: 'VU16byTywsWv5JpI8rbc', riley: 'hA4zGnmTwX2NQiTRMt7o' };
const API_KEY = process.env.ELEVENLABS_API_KEY;
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-de-andrade-brandao');

const PHRASES = [
  // Vocab words (Rafael=male → Ash)
  { text: "Company", file: "aula3_company.mp3", voice: VOICES.ash },
  { text: "Industry", file: "aula3_industry.mp3", voice: VOICES.ash },
  { text: "Headquarters", file: "aula3_headquarters.mp3", voice: VOICES.ash },
  { text: "Branch", file: "aula3_branch.mp3", voice: VOICES.ash },
  { text: "Employee", file: "aula3_employee.mp3", voice: VOICES.ash },
  { text: "Product", file: "aula3_product.mp3", voice: VOICES.ash },
  { text: "Revenue", file: "aula3_revenue.mp3", voice: VOICES.ash },
  { text: "Expand", file: "aula3_expand.mp3", voice: VOICES.ash },

  // Vocab examples (alternate)
  { text: "TVT is a technology company based in São Paulo.", file: "aula3_tvt_is_a_technology_company.mp3", voice: VOICES.ash },
  { text: "The technology industry is growing fast in Brazil.", file: "aula3_the_technology_industry_is_growing.mp3", voice: VOICES.riley },
  { text: "Our headquarters is in São Paulo.", file: "aula3_our_headquarters_is_in_sao_paulo.mp3", voice: VOICES.ash },
  { text: "We have branches in three cities.", file: "aula3_we_have_branches_in_three_cities.mp3", voice: VOICES.riley },
  { text: "TVT has over two hundred employees.", file: "aula3_tvt_has_over_two_hundred_employees.mp3", voice: VOICES.ash },
  { text: "Our main product is technology solutions for businesses.", file: "aula3_our_main_product_is_technology_solutions.mp3", voice: VOICES.riley },
  { text: "Our revenue increased last year.", file: "aula3_our_revenue_increased_last_year.mp3", voice: VOICES.ash },
  { text: "We plan to expand to new markets next year.", file: "aula3_we_plan_to_expand_to_new_markets.mp3", voice: VOICES.riley },

  // Dialogue: Sofia (Riley) + Rafael (Ash)
  { text: "Rafael, can you tell me about TVT? What kind of company is it?", file: "aula3_dialogue_sofia_1.mp3", voice: VOICES.riley },
  { text: "Of course. TVT is a technology company. Our headquarters is in São Paulo.", file: "aula3_dialogue_rafael_2.mp3", voice: VOICES.ash },
  { text: "How big is the company?", file: "aula3_dialogue_sofia_3.mp3", voice: VOICES.riley },
  { text: "There are over two hundred employees. We have branches in three cities.", file: "aula3_dialogue_rafael_4.mp3", voice: VOICES.ash },
  { text: "What products does TVT offer?", file: "aula3_dialogue_sofia_5.mp3", voice: VOICES.riley },
  { text: "Our main product is technology solutions for large businesses. There is a strong demand for our services.", file: "aula3_dialogue_rafael_6.mp3", voice: VOICES.ash },
  { text: "Is the company growing?", file: "aula3_dialogue_sofia_7.mp3", voice: VOICES.riley },
  { text: "Yes! Our revenue increased last year, and we plan to expand to new markets.", file: "aula3_dialogue_rafael_8.mp3", voice: VOICES.ash },

  // Listening passages
  { text: "Good morning. I am Thomas Wright, CEO of NextWave Technologies. Our company was founded in 2015. There are currently one hundred and fifty employees in our headquarters in Austin, Texas. We also have branches in London and Tokyo. Our main product is cloud security software. There is a growing demand for cybersecurity in the industry. Our revenue doubled last year. We plan to expand to South America next year.", file: "aula3_listening_intro.mp3", voice: VOICES.ash },
  { text: "Hi, I am Laura Chen. I work in Human Resources at GreenTech Solutions. There are about eighty employees in our company. Our headquarters is in Chicago, but there is also a branch in Denver. We are a company in the renewable energy industry. There are many opportunities for growth here. Our employees are our most important asset. There is a great team culture, and we always support each other.", file: "aula3_listening_meeting.mp3", voice: VOICES.riley },

  // Fill-in sentences (alternate)
  { text: "There are over two hundred employees at TVT.", file: "aula3_fill_there_are_over_two_hundred.mp3", voice: VOICES.ash },
  { text: "Our headquarters is located in downtown São Paulo.", file: "aula3_fill_our_headquarters_is_located.mp3", voice: VOICES.riley },
  { text: "The company has branches in three different cities.", file: "aula3_fill_the_company_has_branches.mp3", voice: VOICES.ash },
  { text: "There is a growing demand for technology products.", file: "aula3_fill_there_is_a_growing_demand.mp3", voice: VOICES.riley },
  { text: "TVT plans to expand to international markets.", file: "aula3_fill_tvt_plans_to_expand.mp3", voice: VOICES.ash },
  { text: "Our revenue has been growing every year.", file: "aula3_fill_our_revenue_has_been_growing.mp3", voice: VOICES.riley },

  // Speech cards (alternate)
  { text: "TVT is a technology company. Our headquarters is in São Paulo.", file: "aula3_speech_tvt_is_a_technology.mp3", voice: VOICES.ash },
  { text: "There are over two hundred employees. We have branches in three cities.", file: "aula3_speech_there_are_over_two_hundred.mp3", voice: VOICES.riley },
  { text: "Our main product is technology solutions. There is a strong demand.", file: "aula3_speech_our_main_product.mp3", voice: VOICES.ash },
  { text: "Our revenue increased last year. We plan to expand to new markets.", file: "aula3_speech_our_revenue_increased.mp3", voice: VOICES.riley },

  // Survival card (alternate)
  { text: "Our headquarters is in São Paulo.", file: "aula3_survival_our_headquarters.mp3", voice: VOICES.ash },
  { text: "There are over two hundred employees.", file: "aula3_survival_there_are_over.mp3", voice: VOICES.riley },
  { text: "Our main product is technology solutions.", file: "aula3_survival_our_main_product.mp3", voice: VOICES.ash },
  { text: "The company is expanding to new markets.", file: "aula3_survival_the_company_is_expanding.mp3", voice: VOICES.riley },
  { text: "Could you tell me more about your company?", file: "aula3_survival_could_you_tell_me.mp3", voice: VOICES.ash },

  // Grammar examples (alternate)
  { text: "There is a meeting room on each floor.", file: "aula3_gram_there_is_a_meeting_room.mp3", voice: VOICES.ash },
  { text: "There are fifty employees in our department.", file: "aula3_gram_there_are_fifty_employees.mp3", voice: VOICES.riley },
  { text: "Is there a branch in Rio?", file: "aula3_gram_is_there_a_branch.mp3", voice: VOICES.ash },
  { text: "Are there any international clients?", file: "aula3_gram_are_there_any_international.mp3", voice: VOICES.riley },
  { text: "There isn't a branch in Europe.", file: "aula3_gram_there_isnt_a_branch.mp3", voice: VOICES.ash },
  { text: "There aren't any offices in Asia.", file: "aula3_gram_there_arent_any_offices.mp3", voice: VOICES.riley },

  // Ordering
  { text: "TVT is a technology company based in São Paulo. There are over two hundred employees. Our headquarters is in downtown São Paulo, and we have branches in three cities. Our main product is technology solutions for large businesses. Our revenue increased last year, and we plan to expand to new markets.", file: "aula3_order_l3_ordering.mp3", voice: VOICES.ash },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch(API_URL + '/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
  });
  if (!r.ok) throw new Error(r.status + ': ' + (await r.text()).substring(0, 200));
  const buf = Buffer.from(await r.arrayBuffer());
  fs.writeFileSync(outPath, buf);
  return buf.length;
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY'); process.exit(1); }
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });
  const seen = new Set();
  const unique = PHRASES.filter(p => { const k = p.file.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });
  console.log('Generating ' + unique.length + ' audio files for Rafael Aula 3...');
  let ok = 0, skip = 0;
  for (const p of unique) {
    const out = path.join(OUTPUT_DIR, p.file);
    if (fs.existsSync(out)) { console.log('  SKIP: ' + p.file); skip++; continue; }
    try {
      const sz = await gen(p.text, p.voice, out);
      ok++;
      console.log('  OK: ' + p.file + ' (' + Math.round(sz/1024) + 'KB)');
      await new Promise(r => setTimeout(r, 500));
    } catch(e) { console.error('  FAIL: ' + p.file + ' - ' + e.message); }
  }
  console.log('\nDone! OK: ' + ok + ', Skip: ' + skip + ', Total: ' + unique.length);
}
main();
