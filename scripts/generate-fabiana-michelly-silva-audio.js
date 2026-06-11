#!/usr/bin/env node
/**
 * Aula 1 — Fabiana Michelly Silva — "Who Is Fabiana in English?"
 * ElevenLabs audio generator.
 * Voices: arthur=Mark/male/single words, ellen=Fabiana/female/phrases (alternating).
 */
const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) { console.error('No ELEVENLABS_API_KEY found.'); process.exit(1); }

const API_URL = 'https://api.elevenlabs.io/v1/text-to-speech';
const VOICES = {
  arthur: 'sfJopaWaOtauCD3HKX6Q',
  ellen:  'BIvP0GN1cAtSRTxNHnWS'
};
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'fabiana-michelly-silva');

function toFilename(text) {
  return text.toLowerCase().replace(/[^a-z0-9 ]/g, '').replace(/ +/g, '_').substring(0, 60);
}

const phrases = [
  // --- Vocab single words (Arthur) ---
  { text: 'Supply Chain', file: 'supply_chain.mp3', voice: 'arthur' },
  { text: 'Vendor', file: 'vendor.mp3', voice: 'arthur' },
  { text: 'Procurement', file: 'procurement.mp3', voice: 'arthur' },
  { text: 'Stakeholder', file: 'stakeholder.mp3', voice: 'arthur' },
  { text: 'Responsible', file: 'responsible.mp3', voice: 'arthur' },
  { text: 'Currently', file: 'currently.mp3', voice: 'arthur' },
  { text: 'Global Operations', file: 'global_operations.mp3', voice: 'arthur' },
  { text: 'Deal with', file: 'deal_with.mp3', voice: 'arthur' },

  // --- Vocab example sentences (alternating Ellen/Arthur) ---
  { text: 'Our supply chain covers five countries in Latin America.', file: 'our_supply_chain_covers_five_countries_in_latin_america.mp3', voice: 'ellen' },
  { text: 'We work with fifteen different vendors for our equipment.', file: 'we_work_with_fifteen_different_vendors_for_our_equipment.mp3', voice: 'arthur' },
  { text: 'The procurement process takes about three weeks.', file: 'the_procurement_process_takes_about_three_weeks.mp3', voice: 'ellen' },
  { text: 'Every stakeholder received a copy of the quarterly report.', file: 'every_stakeholder_received_a_copy_of_the_quarterly_report.mp3', voice: 'arthur' },
  { text: 'She is responsible for the entire logistics operation.', file: 'she_is_responsible_for_the_entire_logistics_operation.mp3', voice: 'ellen' },
  { text: 'I am currently managing a new project.', file: 'i_am_currently_managing_a_new_project.mp3', voice: 'arthur' },
  { text: 'Bloomberg has global operations in over 170 countries.', file: 'bloomberg_has_global_operations_in_over_170_countries.mp3', voice: 'ellen' },
  { text: 'I deal with vendor contracts every single day.', file: 'i_deal_with_vendor_contracts_every_single_day.mp3', voice: 'arthur' },

  // --- Fill-in sentences (alternating Arthur/Ellen) ---
  { text: 'I work in the supply chain department at Bloomberg.', file: 'i_work_in_the_supply_chain_department_at_bloomberg.mp3', voice: 'arthur' },
  { text: 'She is responsible for procurement.', file: 'she_is_responsible_for_procurement.mp3', voice: 'ellen' },
  { text: 'We deal with international vendors every day.', file: 'we_deal_with_international_vendors_every_day.mp3', voice: 'arthur' },
  { text: 'Currently, I manage fifteen vendor contracts.', file: 'currently_i_manage_fifteen_vendor_contracts.mp3', voice: 'ellen' },
  { text: 'My role involves coordinating global operations.', file: 'my_role_involves_coordinating_global_operations.mp3', voice: 'arthur' },
  { text: 'Every stakeholder receives a monthly report.', file: 'every_stakeholder_receives_a_monthly_report.mp3', voice: 'ellen' },

  // --- Speech card phrases (alternating Ellen/Arthur) ---
  { text: 'Hi, I am Fabiana. I work at Bloomberg.', file: 'hi_i_am_fabiana_i_work_at_bloomberg.mp3', voice: 'ellen' },
  { text: 'I am responsible for procurement and vendor management.', file: 'i_am_responsible_for_procurement_and_vendor_management.mp3', voice: 'arthur' },
  { text: 'I deal with international suppliers on a daily basis.', file: 'i_deal_with_international_suppliers_on_a_daily_basis.mp3', voice: 'ellen' },
  { text: 'Currently, I manage the supply chain for Latin America.', file: 'currently_i_manage_the_supply_chain_for_latin_america.mp3', voice: 'arthur' },
  { text: 'My role involves coordinating logistics and global operations.', file: 'my_role_involves_coordinating_logistics_and_global_oper.mp3', voice: 'ellen' },
  { text: 'We work with fifteen key vendors for our terminal equipment.', file: 'we_work_with_fifteen_key_vendors_for_our_terminal_equipment.mp3', voice: 'arthur' },

  // --- Survival card (alternating Ellen/Arthur) ---
  { text: 'Could you repeat that, please?', file: 'could_you_repeat_that_please.mp3', voice: 'ellen' },
  { text: 'I am not sure I understand. Could you explain?', file: 'i_am_not_sure_i_understand_could_you_explain.mp3', voice: 'arthur' },
  { text: 'Let me think about that for a moment.', file: 'let_me_think_about_that_for_a_moment.mp3', voice: 'ellen' },

  // --- Dialogue: Mark (Arthur) / Fabiana (Ellen) ---
  { text: 'Hi there! I do not think we have met. I am Mark Thompson from the London office.', file: 'hi_there_i_do_not_think_we_have_met_i_am_mark_thompson.mp3', voice: 'arthur' },
  { text: 'Nice to meet you, Mark! I am Fabiana. I work in the supply chain department here.', file: 'nice_to_meet_you_mark_i_am_fabiana_i_work_in_supply_chain.mp3', voice: 'ellen' },
  { text: 'Great! What exactly do you deal with in supply chain?', file: 'great_what_exactly_do_you_deal_with_in_supply_chain.mp3', voice: 'arthur' },
  { text: 'I am responsible for procurement. I deal with vendors who provide our terminal equipment.', file: 'i_am_responsible_for_procurement_i_deal_with_vendors.mp3', voice: 'ellen' },
  { text: 'Interesting! So you work with the Bloomberg Terminal hardware?', file: 'interesting_so_you_work_with_the_bloomberg_terminal.mp3', voice: 'arthur' },
  { text: 'Yes, currently I manage the logistics for all terminal deliveries in Latin America.', file: 'yes_currently_i_manage_the_logistics_for_all_terminal.mp3', voice: 'ellen' },
  { text: 'That sounds like a big operation. How many vendors do you work with?', file: 'that_sounds_like_a_big_operation_how_many_vendors.mp3', voice: 'arthur' },
  { text: 'We have about fifteen key vendors. I report to the regional operations director.', file: 'we_have_about_fifteen_key_vendors_i_report_to_regional.mp3', voice: 'ellen' },

  // --- Grammar examples (alternating Arthur/Ellen) ---
  { text: 'I work at Bloomberg.', file: 'i_work_at_bloomberg.mp3', voice: 'arthur' },
  { text: 'She deals with international vendors.', file: 'she_deals_with_international_vendors.mp3', voice: 'ellen' },
  { text: 'My role involves procurement and logistics.', file: 'my_role_involves_procurement_and_logistics.mp3', voice: 'arthur' },
  { text: 'I am responsible for terminal equipment.', file: 'i_am_responsible_for_terminal_equipment.mp3', voice: 'ellen' },

  // --- Oral drilling IN CLASS (alternating Ellen/Arthur) ---
  { text: 'I work at Bloomberg in the supply chain department.', file: 'i_work_at_bloomberg_in_the_supply_chain_department.mp3', voice: 'ellen' },
  { text: 'I deal with vendors who provide our terminal equipment.', file: 'i_deal_with_vendors_who_provide_our_terminal_equipment.mp3', voice: 'arthur' },
  { text: 'I am responsible for vendor management in Latin America.', file: 'i_am_responsible_for_vendor_management_in_latin_america.mp3', voice: 'ellen' },
  { text: 'Currently, I coordinate deliveries across five countries.', file: 'currently_i_coordinate_deliveries_across_five_countries.mp3', voice: 'arthur' },
  { text: 'I report to the regional operations director.', file: 'i_report_to_the_regional_operations_director.mp3', voice: 'ellen' },

  // --- Listening 1: Elevator pitch (Ellen — full paragraph) ---
  { text: 'Good morning, everyone. My name is Fabiana Michelly Silva. I work at Bloomberg in the supply chain department. I am responsible for procurement and vendor management in Latin America. Currently, I deal with fifteen key vendors who provide terminal equipment for our trading desks. My role involves coordinating logistics, managing contracts, and working with stakeholders across five countries. I have been in supply chain management for several years, and I truly enjoy the global aspect of my work.', file: 'listening_1_elevator_pitch.mp3', voice: 'ellen' },

  // --- Listening 2: Meeting intro (Arthur) ---
  { text: 'Welcome to our quarterly operations meeting. Today, I would like to update you on our supply chain performance. We currently work with fifteen vendors across the region. Our procurement team has been dealing with some delivery delays, but we are on track to meet our targets. The stakeholders have been informed about the timeline changes. Let me walk you through the numbers.', file: 'listening_2_meeting_intro.mp3', voice: 'arthur' },

  // --- Ordering (Ellen — full introduction) ---
  { text: 'Hi, I am Fabiana Michelly Silva. I work at Bloomberg in the supply chain department. I am responsible for procurement in Latin America. My role involves coordinating logistics and managing vendor contracts. Currently, I deal with fifteen key vendors across the region. I report to the regional operations director.', file: 'order_l1_professional_intro.mp3', voice: 'ellen' }
];

async function generateAudio(text, voiceId, outputPath) {
  const resp = await fetch(`${API_URL}/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text: text,
      model_id: 'eleven_turbo_v2_5',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    })
  });
  if (!resp.ok) {
    const err = await resp.text();
    throw new Error(`ElevenLabs error (${resp.status}): ${err}`);
  }
  const buffer = Buffer.from(await resp.arrayBuffer());
  fs.writeFileSync(outputPath, buffer);
  return buffer.length;
}

async function main() {
  if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

  const seen = new Set();
  const unique = phrases.filter(p => {
    const key = p.file;
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });

  console.log(`Generating ${unique.length} audio files for Fabiana Michelly Silva...`);
  let generated = 0, skipped = 0;

  for (const p of unique) {
    const outputPath = path.join(OUTPUT_DIR, p.file);
    const voiceId = VOICES[p.voice] || VOICES.arthur;

    if (fs.existsSync(outputPath)) {
      console.log(`  SKIP (exists): ${p.file}`);
      skipped++;
      continue;
    }

    try {
      const bytes = await generateAudio(p.text, voiceId, outputPath);
      console.log(`  OK [${p.voice}]: ${p.file} (${(bytes/1024).toFixed(1)}KB)`);
      generated++;
      await new Promise(r => setTimeout(r, 500));
    } catch (err) {
      console.error(`  FAIL: ${p.file} — ${err.message}`);
    }
  }

  // Build audioMap
  const audioMap = {};
  for (const p of unique) {
    audioMap[p.text] = `/audio/fabiana-michelly-silva/${p.file}`;
  }

  const mapPath = path.join(OUTPUT_DIR, 'audioMap.json');
  fs.writeFileSync(mapPath, JSON.stringify(audioMap, null, 2));
  console.log(`\nDone: ${generated} generated, ${skipped} skipped`);
  console.log(`audioMap saved to ${mapPath}`);
}

main().catch(err => { console.error(err); process.exit(1); });
