const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-pelizaro');

// Voice rules:
// - Rafael is MALE → his lines/exercises = ARTHUR
// - Sarah Chen is FEMALE → her lines = ELLEN
// - Single words = ARTHUR (student gender)
// - General phrases = ALTERNATE Arthur/Ellen

const PHRASES = [
  // ===== Emergency phrases (alternate) =====
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: ARTHUR },
  { text: "I am not sure I understand. Could you explain?", file: "i_am_not_sure_i_understand_could_you_explain.mp3", voice: ELLEN },
  { text: "Let me think about that for a moment.", file: "let_me_think_about_that_for_a_moment.mp3", voice: ARTHUR },
  { text: "That is a great question.", file: "that_is_a_great_question.mp3", voice: ELLEN },
  { text: "In my experience, I would say...", file: "in_my_experience_i_would_say.mp3", voice: ARTHUR },

  // ===== Vocab words (Rafael is male → ARTHUR) =====
  { text: "Manage", file: "manage.mp3", voice: ARTHUR },
  { text: "Lead", file: "lead.mp3", voice: ARTHUR },
  { text: "Implement", file: "implement.mp3", voice: ARTHUR },
  { text: "Deploy", file: "deploy.mp3", voice: ARTHUR },
  { text: "Report", file: "report.mp3", voice: ARTHUR },
  { text: "Stakeholder", file: "stakeholder.mp3", voice: ARTHUR },
  { text: "Vendor", file: "vendor.mp3", voice: ARTHUR },
  { text: "Milestone", file: "milestone.mp3", voice: ARTHUR },

  // ===== Vocab example sentences (Rafael context = ARTHUR, general = alternate) =====
  { text: "I manage three IT projects for a major bank in Brazil.", file: "i_manage_three_it_projects_for_a_major_bank.mp3", voice: ARTHUR },
  { text: "Rafael leads a remote team of twelve developers.", file: "rafael_leads_a_remote_team_of_twelve.mp3", voice: ELLEN },
  { text: "We plan to implement the new ERP module next quarter.", file: "we_plan_to_implement_the_new_erp_module.mp3", voice: ARTHUR },
  { text: "The IT team will deploy the update on Friday.", file: "the_it_team_will_deploy_the_update_on_friday.mp3", voice: ELLEN },
  { text: "I need to report our progress to the board this afternoon.", file: "i_need_to_report_our_progress_to_the_board.mp3", voice: ARTHUR },
  { text: "The stakeholders are expecting a detailed project update.", file: "the_stakeholders_are_expecting_a_detailed.mp3", voice: ELLEN },
  { text: "We are negotiating with a new vendor for cloud services.", file: "we_are_negotiating_with_a_new_vendor.mp3", voice: ARTHUR },
  { text: "We reached an important milestone last month.", file: "we_reached_an_important_milestone_last_month.mp3", voice: ELLEN },

  // ===== Grammar examples (alternate) =====
  { text: "Rafael manages technology systems for banks.", file: "rafael_manages_technology_systems_for_banks.mp3", voice: ARTHUR },
  { text: "He leads meetings with his remote team every day.", file: "he_leads_meetings_with_his_remote_team.mp3", voice: ELLEN },
  { text: "The company implements new solutions regularly.", file: "the_company_implements_new_solutions.mp3", voice: ARTHUR },
  { text: "They deploy updates every Friday.", file: "they_deploy_updates_every_friday.mp3", voice: ELLEN },
  { text: "She reports progress to the board every week.", file: "she_reports_progress_to_the_board.mp3", voice: ARTHUR },

  // ===== Fill-in sentences (alternate) =====
  { text: "Rafael is an IT Project Manager based in Sao Paulo.", file: "fill_rafael_is_an_it_project_manager.mp3", voice: ARTHUR },
  { text: "He manages technology systems for banks and e-commerce companies.", file: "fill_he_manages_technology_systems.mp3", voice: ELLEN },
  { text: "Every day, he leads meetings with his remote team.", file: "fill_every_day_he_leads_meetings.mp3", voice: ARTHUR },
  { text: "His stakeholders include CFOs, CTOs, and business directors.", file: "fill_his_stakeholders_include_cfos.mp3", voice: ELLEN },
  { text: "Last quarter, his team deployed a new payment system.", file: "fill_last_quarter_his_team_deployed.mp3", voice: ARTHUR },
  { text: "He works with several international vendors for cloud infrastructure.", file: "fill_he_works_with_several_vendors.mp3", voice: ELLEN },

  // ===== Speech practice (Rafael = ARTHUR) =====
  { text: "I am an IT Project Manager based in Sao Paulo.", file: "i_am_an_it_project_manager_based_in_sp.mp3", voice: ARTHUR },
  { text: "I manage technology systems for banks and e-commerce.", file: "i_manage_technology_systems_for_banks.mp3", voice: ARTHUR },
  { text: "I lead a remote team of twelve developers.", file: "i_lead_a_remote_team_of_twelve_developers.mp3", voice: ARTHUR },

  // ===== Speech cards extra (ARTHUR) =====
  { text: "I am an IT Project Manager. I manage technology systems for banks and e-commerce companies.", file: "speech_i_am_an_it_project_manager.mp3", voice: ARTHUR },
  { text: "Every week, I report our progress to stakeholders and manage meetings with vendors.", file: "speech_every_week_i_report_our_progress.mp3", voice: ARTHUR },
  { text: "We implemented and deployed a new payment platform for a major bank last quarter.", file: "speech_we_implemented_and_deployed.mp3", voice: ARTHUR },

  // ===== Dialogue — Sarah Chen (female = ELLEN), Rafael (male = ARTHUR) =====
  { text: "Hi! I am Sarah Chen, IT Director at GlobalTech in Singapore. Are you attending the cloud infrastructure panel?", file: "dialogue_sarah_1.mp3", voice: ELLEN },
  { text: "Nice to meet you, Sarah! I am Rafael Pelizaro. I manage IT projects for banks and e-commerce companies here in Brazil.", file: "dialogue_rafael_2.mp3", voice: ARTHUR },
  { text: "That sounds interesting! What kind of projects do you lead?", file: "dialogue_sarah_3.mp3", voice: ELLEN },
  { text: "I lead a remote team of twelve developers. We implement and deploy technology systems. Our latest project was a payment platform for a major bank.", file: "dialogue_rafael_4.mp3", voice: ARTHUR },
  { text: "Impressive! Do you work with international vendors?", file: "dialogue_sarah_5.mp3", voice: ELLEN },
  { text: "Yes, we work with several vendors for cloud services. I report our progress to stakeholders every week.", file: "dialogue_rafael_6.mp3", voice: ARTHUR },
  { text: "That is great experience! We are looking for partners in Latin America. Could we connect after the panel?", file: "dialogue_sarah_7.mp3", voice: ELLEN },
  { text: "Absolutely! I would love to discuss this further. Here is my business card.", file: "dialogue_rafael_8.mp3", voice: ARTHUR },

  // ===== Listening 1 — Rafael full intro (ARTHUR) =====
  { text: "Good afternoon, everyone. My name is Rafael Pelizaro. I am an IT Project Manager based in Sao Paulo, Brazil. I manage technology systems for banks and e-commerce companies. I lead a remote team of twelve developers, and we implement and deploy solutions for major clients. Last quarter, we reached an important milestone: we deployed a new payment platform. I report our progress to stakeholders every week, and I work with international vendors for cloud infrastructure.", file: "listening1_full_intro.mp3", voice: ARTHUR },

  // ===== Listening 2 — Q&A question (ELLEN) =====
  { text: "Thank you for your presentation, Rafael. I have a question about your deployment process. How many vendors do you work with for cloud services? And how do you manage communication with a remote team of twelve developers across different time zones?", file: "listening2_full_qa.mp3", voice: ELLEN },

  // ===== Order exercise (ARTHUR) =====
  { text: "Good afternoon. My name is Rafael Pelizaro. I am an IT Project Manager based in Sao Paulo. I manage technology systems for banks and e-commerce. I lead a remote team of twelve developers. We deploy solutions for major clients.", file: "order_l1_ordering.mp3", voice: ARTHUR },

  // ===== Survival card (Rafael = ARTHUR) =====
  { text: "We deployed a new payment platform last quarter.", file: "we_deployed_a_new_payment_platform.mp3", voice: ARTHUR },
  { text: "I would love to discuss this further.", file: "i_would_love_to_discuss_this_further.mp3", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' audio files for Rafael Pelizaro...');
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
