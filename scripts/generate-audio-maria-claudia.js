const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

// Voice rules:
// - Single words (1-2 words) = ALWAYS Arthur
// - Phrases (3+ words) = ALTERNATE Arthur/Ellen
// - Maria Claudia lines (female) = Ellen
// - David Chen lines (male) = Arthur

const PHRASES = [
  // ===== Emergency phrases (alternate) =====
  { text: "Could you repeat that, please?", file: "could_you_repeat_that_please.mp3", voice: ARTHUR },
  { text: "I am not sure I understand. Could you explain?", file: "i_am_not_sure_i_understand_could_you_explain.mp3", voice: ELLEN },
  { text: "Let me think about that for a moment.", file: "let_me_think_about_that_for_a_moment.mp3", voice: ARTHUR },
  { text: "How do you say this in English?", file: "how_do_you_say_this_in_english.mp3", voice: ELLEN },
  { text: "Could you speak more slowly, please?", file: "could_you_speak_more_slowly_please.mp3", voice: ARTHUR },

  // ===== Vocab words (1-2 words → ALWAYS Arthur) =====
  { text: "Oversee", file: "oversee.mp3", voice: ARTHUR },
  { text: "Holding", file: "holding.mp3", voice: ARTHUR },
  { text: "Subsidiary", file: "subsidiary.mp3", voice: ARTHUR },
  { text: "Counterpart", file: "counterpart.mp3", voice: ARTHUR },
  { text: "Stakeholder", file: "stakeholder.mp3", voice: ARTHUR },
  { text: "Joint Venture", file: "joint_venture.mp3", voice: ARTHUR },
  { text: "Procurement", file: "procurement.mp3", voice: ARTHUR },
  { text: "Revenue", file: "revenue.mp3", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "I oversee the financial and sales operations of the holding.", file: "i_oversee_the_financial_and_sales_operations.mp3", voice: ARTHUR },
  { text: "Our holding company owns three subsidiaries in different sectors.", file: "our_holding_company_owns_three_subsidiaries.mp3", voice: ELLEN },
  { text: "The subsidiary in Houston reports directly to us.", file: "the_subsidiary_in_houston_reports_directly.mp3", voice: ARTHUR },
  { text: "My counterpart in Pittsburgh handles manufacturing operations.", file: "my_counterpart_in_pittsburgh_handles.mp3", voice: ELLEN },
  { text: "All stakeholders must approve the annual budget.", file: "all_stakeholders_must_approve_the_annual_budget.mp3", voice: ARTHUR },
  { text: "We are planning a joint venture with a Texas-based company.", file: "we_are_planning_a_joint_venture.mp3", voice: ELLEN },
  { text: "The procurement process takes about three months.", file: "the_procurement_process_takes_about_three_months.mp3", voice: ARTHUR },
  { text: "Our revenue increased by twelve percent last quarter.", file: "our_revenue_increased_by_twelve_percent.mp3", voice: ELLEN },

  // ===== Maria Claudia speech/intro phrases (female = Ellen) =====
  { text: "I am responsible for managing three subsidiaries.", file: "i_am_responsible_for_managing_three_subsidiaries.mp3", voice: ELLEN },
  { text: "I deal with international partners in Houston and Pittsburgh.", file: "i_deal_with_international_partners.mp3", voice: ELLEN },
  { text: "I am based in Sao Paulo, Brazil.", file: "i_am_based_in_sao_paulo_brazil.mp3", voice: ELLEN },
  { text: "I am responsible for the financial operations of the holding.", file: "i_am_responsible_for_the_financial_operations.mp3", voice: ELLEN },
  { text: "I deal with procurement and vendor negotiations.", file: "i_deal_with_procurement_and_vendor_negotiations.mp3", voice: ELLEN },
  { text: "I am based in the Sao Paulo headquarters.", file: "i_am_based_in_the_sao_paulo_headquarters.mp3", voice: ELLEN },

  // ===== Grammar context passage (long — Ellen for Maria Claudia narrative) =====
  { text: "Maria Claudia oversees the financial operations of a family holding company in Sao Paulo. She is responsible for three subsidiaries that operate in different sectors. Every month, she deals with her counterparts in Houston and Pittsburgh to review revenue targets and procurement contracts. The stakeholders expect quarterly reports, and Maria Claudia is currently working on a joint venture with a new partner in Texas.", file: "grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in-the-blank sentences (alternate) =====
  { text: "The holding company oversees all subsidiaries.", file: "fill_the_holding_company_oversees.mp3", voice: ARTHUR },
  { text: "She deals with stakeholders on a weekly basis.", file: "fill_she_deals_with_stakeholders.mp3", voice: ELLEN },
  { text: "The procurement department reports to Maria Claudia.", file: "fill_the_procurement_department_reports.mp3", voice: ARTHUR },
  { text: "Revenue from the Houston subsidiary grew last year.", file: "fill_revenue_from_the_houston_subsidiary.mp3", voice: ELLEN },
  { text: "Her counterpart in Pittsburgh manages the factory.", file: "fill_her_counterpart_in_pittsburgh.mp3", voice: ARTHUR },
  { text: "They are planning a new joint venture this year.", file: "fill_they_are_planning_a_new_joint_venture.mp3", voice: ELLEN },
  { text: "The subsidiary needs to increase its revenue.", file: "fill_the_subsidiary_needs_to_increase.mp3", voice: ARTHUR },
  { text: "All stakeholders approved the new budget.", file: "fill_all_stakeholders_approved_the_new_budget.mp3", voice: ELLEN },

  // ===== Survival card phrases (Maria Claudia = Ellen) =====
  { text: "Let me introduce myself. I am Maria Claudia from Sao Paulo.", file: "surv_let_me_introduce_myself.mp3", voice: ELLEN },
  { text: "I oversee the financial and sales operations of our holding.", file: "surv_i_oversee_the_financial_and_sales.mp3", voice: ELLEN },
  { text: "I am responsible for managing three subsidiaries.", file: "surv_i_am_responsible_for_managing.mp3", voice: ELLEN },
  { text: "I deal with international partners in Houston and Pittsburgh.", file: "surv_i_deal_with_international_partners.mp3", voice: ELLEN },
  { text: "I am currently working on expanding our joint ventures.", file: "surv_i_am_currently_working_on_expanding.mp3", voice: ELLEN },

  // ===== Speech practice cards (Maria Claudia = Ellen) =====
  { text: "I oversee the operations of our holding company.", file: "speech_i_oversee_the_operations.mp3", voice: ELLEN },
  { text: "I am responsible for three subsidiaries in different sectors.", file: "speech_i_am_responsible_for_three.mp3", voice: ELLEN },
  { text: "I deal with counterparts in Houston and Pittsburgh every month.", file: "speech_i_deal_with_counterparts.mp3", voice: ELLEN },
  { text: "Our revenue grew twelve percent last quarter.", file: "speech_our_revenue_grew_twelve.mp3", voice: ELLEN },
  { text: "I am currently working on a joint venture with a Texas partner.", file: "speech_i_am_currently_working_on_jv.mp3", voice: ELLEN },

  // ===== Listening 1 — Executive intro (Maria Claudia = Ellen, long passage) =====
  { text: "Good morning, everyone. My name is Maria Claudia Curimbaba. I am based in Sao Paulo, Brazil. I oversee the financial and sales operations of our family holding company. We have three subsidiaries in different sectors. I am responsible for managing relationships with our counterparts in Houston and Pittsburgh. Our revenue has been growing steadily, and I am currently working on expanding our joint ventures. I deal with procurement, stakeholder relations, and strategic planning on a daily basis.", file: "listening_1_executive_intro.mp3", voice: ELLEN },

  // ===== Listening 2 — Meeting opening (Maria Claudia = Ellen) =====
  { text: "Good morning. Let me start by introducing our agenda for today. First, we will review the revenue numbers from Q3. Second, I would like to discuss the joint venture proposal from our Houston counterpart. Third, we need to address the procurement timeline for the new subsidiary. All stakeholders should have received the report by email. Let us begin.", file: "listening_2_meeting_opening.mp3", voice: ELLEN },

  // ===== Dialogue — David Chen (male = Arthur), Maria Claudia (female = Ellen) =====
  { text: "Hi! I am David Chen from our Pittsburgh office. Are you the new managing director?", file: "dlg_hi_i_am_david_chen.mp3", voice: ARTHUR },
  { text: "Nice to meet you, David. I am Maria Claudia. I oversee the financial and sales operations of the holding here in Sao Paulo.", file: "dlg_nice_to_meet_you_david.mp3", voice: ELLEN },
  { text: "Great to meet you! What exactly do you handle on a daily basis?", file: "dlg_great_to_meet_you.mp3", voice: ARTHUR },
  { text: "I am responsible for managing three subsidiaries. I also deal with procurement contracts and stakeholder relations.", file: "dlg_i_am_responsible_for_managing.mp3", voice: ELLEN },
  { text: "That sounds like a lot! Do you work with the Houston team as well?", file: "dlg_that_sounds_like_a_lot.mp3", voice: ARTHUR },
  { text: "Yes, I deal with my counterpart in Houston regularly. We are currently working on a joint venture together.", file: "dlg_yes_i_deal_with_my_counterpart.mp3", voice: ELLEN },
  { text: "Impressive! How is the revenue looking this year?", file: "dlg_impressive_how_is_the_revenue.mp3", voice: ARTHUR },
  { text: "Our revenue increased by twelve percent last quarter. We are on track to meet our annual targets.", file: "dlg_our_revenue_increased.mp3", voice: ELLEN },

  // ===== Error correction / Spot the Error (alternate) =====
  { text: "She collaborate with many departments.", file: "ic_error_she_collaborates.mp3", voice: ARTHUR },
  { text: "I am currently work on a new project.", file: "ic_error_currently_working.mp3", voice: ELLEN },
  { text: "The meetings are doing by the internet.", file: "ic_error_meetings_held_online.mp3", voice: ARTHUR },
  { text: "He oversee the sales department.", file: "ic_error_he_oversees.mp3", voice: ELLEN },
  { text: "I am responsible of the budget.", file: "ic_error_responsible_for.mp3", voice: ARTHUR },

  // ===== Expressions (short — alternate) =====
  { text: "I am responsible for...", file: "expr_i_am_responsible_for.mp3", voice: ELLEN },
  { text: "I deal with...", file: "expr_i_deal_with.mp3", voice: ARTHUR },
  { text: "I am based in...", file: "expr_i_am_based_in.mp3", voice: ELLEN },
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

  console.log('Generating ' + unique.length + ' audio files for Maria Claudia Curimbaba...');
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
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) {
        console.error('FAIL: ' + p.file + ' — ' + e.message);
      }
    }
  }

  console.log('\nDone! Generated: ' + generated + ', Skipped: ' + skipped + ', Total entries: ' + unique.length);
  console.log('Audio files saved to: ' + DIR);
}

main().catch(e => { console.error(e); process.exit(1); });
