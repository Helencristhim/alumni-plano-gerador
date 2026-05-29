#!/usr/bin/env node
/**
 * Generate ElevenLabs MP3 audios for Roberto Rezende — Lesson 1.
 *
 * Usage:
 *   ELEVENLABS_API_KEY=sk_... node scripts/generate-roberto-rezende-audio.js
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

const API_KEY = process.env.ELEVENLABS_API_KEY;
if (!API_KEY) {
  console.error('ERROR: set ELEVENLABS_API_KEY env var first.');
  process.exit(1);
}

// Correct voice IDs (May 2026)
const VOICES = {
  arthur: 'sfJopaWaOtauCD3HKX6Q',
  ellen:  'BIvP0GN1cAtSRTxNHnWS',
};
const MODEL_ID = 'eleven_multilingual_v2';
const OUTPUT_DIR = path.join(__dirname, '..', 'public', 'audio', 'roberto-rezende');

if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

// ===== AudioMap extracted from professor/roberto-rezende.html =====
const audioMap = {
  "Could you repeat that, please?": "could_you_repeat_that_please.mp3",
  "I am not sure I understand. Could you explain?": "i_am_not_sure_i_understand_could_you_explain.mp3",
  "Let me think about that for a moment.": "let_me_think_about_that_for_a_moment.mp3",
  "That is a great question.": "that_is_a_great_question.mp3",
  "In my experience, I would say...": "in_my_experience_i_would_say.mp3",
  "Pipeline": "pipeline.mp3",
  "Forecast": "forecast.mp3",
  "Follow-up": "follow_up.mp3",
  "Headquarters": "headquarters.mp3",
  "Oversee": "oversee.mp3",
  "Deal with": "deal_with.mp3",
  "Report to": "report_to.mp3",
  "Currently": "currently.mp3",
  "Responsible for": "responsible_for.mp3",
  "Background": "background.mp3",
  "We have ten new clients in our pipeline this quarter.": "we_have_ten_new_clients_in_our_pipeline_this_quarter.mp3",
  "The sales forecast for the next quarter looks promising.": "the_sales_forecast_for_the_next_quarter_looks_promising.mp3",
  "I need to do a follow-up with the client after the meeting.": "i_need_to_do_a_follow_up_with_the_client_after_the_meeting.mp3",
  "Our headquarters is located in Shanghai, China.": "our_headquarters_is_located_in_shanghai_china.mp3",
  "I oversee all sales operations in the Brazilian market.": "i_oversee_all_sales_operations_in_the_brazilian_market.mp3",
  "I deal with both industrial and agricultural clients.": "i_deal_with_both_industrial_and_agricultural_clients.mp3",
  "I report to the regional manager in Hong Kong.": "i_report_to_the_regional_manager_in_hong_kong.mp3",
  "I am currently developing a new market strategy.": "i_am_currently_developing_a_new_market_strategy.mp3",
  "I am responsible for the sales pipeline in Brazil.": "i_am_responsible_for_the_sales_pipeline_in_brazil.mp3",
  "My background is in mechanical engineering.": "my_background_is_in_mechanical_engineering.mp3",
  "Roberto oversees all sales operations in Brazil.": "roberto_oversees_all_sales_operations_in_brazil.mp3",
  "He is currently developing a new market strategy.": "he_is_currently_developing_a_new_market_strategy.mp3",
  "Every week, he reports to the Hong Kong office.": "every_week_he_reports_to_the_hong_kong_office.mp3",
  "Right now, the team is preparing for a trade fair.": "right_now_the_team_is_preparing_for_a_trade_fair.mp3",
  "Roberto deals with clients from three different segments.": "roberto_deals_with_clients_from_three_different_segments.mp3",
  "Good morning. My name is Roberto Rezende.": "good_morning_my_name_is_roberto_rezende.mp3",
  "I work as a sales executive at a Chinese diesel engine company.": "i_work_as_a_sales_executive_at_a_chinese_diesel_engine_compa.mp3",
  "I am responsible for the Brazilian market.": "i_am_responsible_for_the_brazilian_market.mp3",
  "I deal with industrial, agricultural, and generator clients.": "i_deal_with_industrial_agricultural_and_generator_clients.mp3",
  "I am currently working on three major deals this quarter.": "i_am_currently_working_on_three_major_deals_this_quarter.mp3",
  "My background is in mechanical engineering. I have a PhD.": "my_background_is_in_mechanical_engineering_i_have_a_phd.mp3",
  "I oversee sales operations for the Brazilian market.": "i_oversee_sales_operations_for_the_brazilian_market.mp3",
  "I am currently working on a deal with a major agricultural company.": "i_am_currently_working_on_a_deal_with_a_major_agricultural_c.mp3",
  "My name is Roberto Rezende. I work in sales at a diesel engine company.": "my_name_is_roberto_rezende_i_work_in_sales_at_a_diesel_engin.mp3",
  "I oversee the Brazilian market.": "i_oversee_the_brazilian_market.mp3",
  "I am currently working on three major deals.": "i_am_currently_working_on_three_major_deals.mp3",
  "The forecast for this quarter looks promising.": "the_forecast_for_this_quarter_looks_promising.mp3",
  // Dialogue — Wei Lin lines = Ellen, Roberto lines = Arthur
  "Good morning. You must be Roberto from the Brazil office. I am Wei Lin from Shanghai headquarters.": "good_morning_you_must_be_roberto_from_the_brazil_office.mp3",
  "Nice to meet you, Wei Lin. I oversee sales operations for the Brazilian market.": "nice_to_meet_you_wei_lin_i_oversee_sales_operations.mp3",
  "How is the pipeline looking this quarter?": "how_is_the_pipeline_looking_this_quarter.mp3",
  "We are currently working on three major deals. The forecast looks promising.": "we_are_currently_working_on_three_major_deals_the_forecast.mp3",
  "Are you responsible for the agricultural segment as well?": "are_you_responsible_for_the_agricultural_segment_as_well.mp3",
  "Yes, I deal with industrial, agricultural, and generator clients.": "yes_i_deal_with_industrial_agricultural_and_generator_clien.mp3",
  "Who do you report to at the regional level?": "who_do_you_report_to_at_the_regional_level.mp3",
  "I report to Mr. Zhang in Hong Kong. We have a weekly call every Monday.": "i_report_to_mr_zhang_in_hong_kong_we_have_a_weekly_call.mp3",
  "My name is Roberto Rezende. I oversee sales at a diesel engine company in Brazil.": "my_name_is_roberto_rezende_i_oversee_sales_at_a_diesel_engin.mp3",
  "We are currently working on expanding our pipeline in the agricultural segment.": "we_are_currently_working_on_expanding_our_pipeline.mp3",
  "The forecast for this quarter looks very promising.": "the_forecast_for_this_quarter_looks_very_promising.mp3",
  "I need to follow up with the client about the new contract.": "i_need_to_follow_up_with_the_client_about_the_new_contract.mp3",
  "Could I have a moment to check the latest numbers?": "could_i_have_a_moment_to_check_the_latest_numbers.mp3",
  "We currently have ten potential clients in our pipeline.": "we_currently_have_ten_potential_clients_in_our_pipeline.mp3",
  "My background is in mechanical engineering, but I currently work in sales.": "my_background_is_in_mechanical_engineering_but_i_currently.mp3",
  "We are currently developing new partnerships in the agricultural sector.": "we_are_currently_developing_new_partnerships_in_the_agricul.mp3",
  "I have a PhD in engineering.": "i_have_a_phd_in_engineering.mp3",
  "Roberto works at a diesel engine company.": "roberto_works_at_a_diesel_engine_company.mp3",
  "He oversees the Brazilian market.": "he_oversees_the_brazilian_market.mp3",
  "He is currently working on three major deals.": "he_is_currently_working_on_three_major_deals.mp3",
  "The team is preparing for a trade fair next month.": "the_team_is_preparing_for_a_trade_fair_next_month.mp3",
  "I am Roberto Rezende, a sales executive at a Chinese diesel engine company.": "i_am_roberto_rezende_a_sales_executive.mp3",
  "I am responsible for the industrial and agricultural segments.": "i_am_responsible_for_the_industrial_and_agricultural_segmen.mp3",
  "I report to Mr. Zhang in the Hong Kong office. We have a weekly call every Monday.": "i_report_to_mr_zhang_in_the_hong_kong_office.mp3",
  "I will follow up with you next week about the contract details.": "i_will_follow_up_with_you_next_week_about_the_contract_detai.mp3",
  "We currently have ten clients in our pipeline. Three deals are in the final stage.": "we_currently_have_ten_clients_three_deals_final_stage.mp3",
  "I oversee sales operations for the Brazilian market. I deal with industrial and agricultural clients.": "i_oversee_sales_operations_i_deal_with_industrial.mp3",
  "The forecast for this quarter looks very promising. We expect a fifteen percent increase.": "the_forecast_looks_very_promising_we_expect_fifteen_percent.mp3",
};

// Also handle the ordering audio
const orderAudio = {
  "[order-l1]": "order_l1_self_introduction.mp3",
};

// ===== Voice assignment =====
// Wei Lin's dialogue lines (Ellen)
const weiLinLines = new Set([
  "Good morning. You must be Roberto from the Brazil office. I am Wei Lin from Shanghai headquarters.",
  "How is the pipeline looking this quarter?",
  "Are you responsible for the agricultural segment as well?",
  "Who do you report to at the regional level?",
]);

function assignVoice(text) {
  // Skip placeholder/ordering entries
  if (text.startsWith('[')) return 'arthur';

  // Dialogue: Wei Lin = Ellen, Roberto = Arthur
  if (weiLinLines.has(text)) return 'ellen';

  // Single words (1-2 words) = ALWAYS Arthur
  const wordCount = text.split(/\s+/).length;
  if (wordCount <= 2) return 'arthur';

  // Sentences (3+ words) = alternate Arthur/Ellen
  return null; // Will be assigned during list building
}

// Build generation list
const list = [];
const seen = new Set();
let sentenceToggle = false; // false=arthur, true=ellen

for (const [text, filename] of Object.entries(audioMap)) {
  if (seen.has(filename)) continue;
  seen.add(filename);

  let voice = assignVoice(text);
  if (voice === null) {
    // Alternating sentences
    voice = sentenceToggle ? 'ellen' : 'arthur';
    sentenceToggle = !sentenceToggle;
  }

  list.push({ text, filename, voice });
}

// Add order audio
for (const [text, filename] of Object.entries(orderAudio)) {
  if (!seen.has(filename)) {
    seen.add(filename);
    // For ordering, generate a complete self-introduction as Arthur (Roberto)
    list.push({
      text: "Good morning. My name is Roberto Rezende. I work as a sales executive at a Chinese diesel engine company. I am responsible for the Brazilian market. I deal with industrial, agricultural, and generator clients. I am currently working on three major deals this quarter. My background is in mechanical engineering. I have a PhD.",
      filename,
      voice: 'arthur'
    });
  }
}

// Skip the placeholder entry
const filteredList = list.filter(item => item.filename !== 'placeholder_not_used.mp3');

function tts(text, voiceId) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({
      text,
      model_id: MODEL_ID,
      voice_settings: { stability: 0.5, similarity_boost: 0.75 },
    });
    const req = https.request({
      hostname: 'api.elevenlabs.io',
      path: `/v1/text-to-speech/${voiceId}`,
      method: 'POST',
      headers: {
        'xi-api-key': API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
        'Content-Length': Buffer.byteLength(data),
      },
    }, (res) => {
      const chunks = [];
      res.on('data', (c) => chunks.push(c));
      res.on('end', () => {
        if (res.statusCode !== 200) {
          return reject(new Error(`HTTP ${res.statusCode}: ${Buffer.concat(chunks).toString()}`));
        }
        resolve(Buffer.concat(chunks));
      });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  console.log(`Generating ${filteredList.length} audios in ${OUTPUT_DIR}...`);
  console.log(`Voice IDs — Arthur: ${VOICES.arthur}, Ellen: ${VOICES.ellen}`);
  let ok = 0, skip = 0, fail = 0;

  for (let i = 0; i < filteredList.length; i++) {
    const item = filteredList[i];
    const out = path.join(OUTPUT_DIR, item.filename);

    // Skip if file already exists and is > 1KB
    if (fs.existsSync(out) && fs.statSync(out).size > 1000) {
      skip++;
      console.log(`  [${i + 1}/${filteredList.length}] SKIP ${item.filename} (exists)`);
      continue;
    }

    try {
      const buf = await tts(item.text, VOICES[item.voice]);
      fs.writeFileSync(out, buf);
      ok++;
      console.log(`  [${i + 1}/${filteredList.length}] OK ${item.voice.toUpperCase()} — ${item.text.substring(0, 60)}...`);
    } catch (e) {
      fail++;
      console.error(`  [${i + 1}/${filteredList.length}] FAIL ${item.filename}: ${e.message}`);
    }

    // Rate-limit pause (250ms between calls)
    await new Promise(r => setTimeout(r, 250));
  }

  console.log(`\nDone. ok=${ok} skip=${skip} fail=${fail}`);
  console.log(`Total files in ${OUTPUT_DIR}: ${fs.readdirSync(OUTPUT_DIR).filter(f => f.endsWith('.mp3')).length}`);
}

main().catch((e) => { console.error(e); process.exit(1); });
