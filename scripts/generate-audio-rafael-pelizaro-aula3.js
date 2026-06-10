const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'rafael-pelizaro');

// Voice rules:
// - Rafael is MALE -> his lines/exercises = ARTHUR
// - Catherine Wells is FEMALE CFO -> her lines = ELLEN
// - Single words = ARTHUR (student gender)
// - General phrases = ALTERNATE Arthur/Ellen

const PHRASES = [
  // ===== Vocab words (Arthur - student male) =====
  { text: "KPI", file: "l3_kpi.mp3", voice: ARTHUR },
  { text: "Revenue", file: "l3_revenue.mp3", voice: ARTHUR },
  { text: "Growth", file: "l3_growth.mp3", voice: ARTHUR },
  { text: "Decline", file: "l3_decline.mp3", voice: ARTHUR },
  { text: "Quarter", file: "l3_quarter.mp3", voice: ARTHUR },
  { text: "Budget", file: "l3_budget.mp3", voice: ARTHUR },
  { text: "Forecast", file: "l3_forecast.mp3", voice: ARTHUR },
  { text: "ROI", file: "l3_roi.mp3", voice: ARTHUR },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "Our main KPI this quarter is customer acquisition cost.", file: "l3_our_main_kpi_this_quarter.mp3", voice: ARTHUR },
  { text: "Revenue increased by 12 percent compared to last quarter.", file: "l3_revenue_increased_by_12_percent.mp3", voice: ELLEN },
  { text: "We are seeing strong growth in the cloud services division.", file: "l3_we_are_seeing_strong_growth.mp3", voice: ARTHUR },
  { text: "There was a slight decline in hardware sales this month.", file: "l3_there_was_a_slight_decline.mp3", voice: ELLEN },
  { text: "Q2 results were higher than Q1 across all departments.", file: "l3_q2_results_were_higher.mp3", voice: ARTHUR },
  { text: "We need to stay within the budget for the next quarter.", file: "l3_we_need_to_stay_within_budget.mp3", voice: ELLEN },
  { text: "The forecast shows a 15 percent increase in revenue for Q3.", file: "l3_the_forecast_shows_15_percent.mp3", voice: ARTHUR },
  { text: "The ROI on our cloud migration project exceeded expectations.", file: "l3_the_roi_on_cloud_migration.mp3", voice: ELLEN },

  // ===== Grammar context sentences (alternate) =====
  { text: "Cloud revenue is higher than on-premise revenue.", file: "l3_cloud_revenue_is_higher.mp3", voice: ARTHUR },
  { text: "Our Q2 budget was lower than Q1.", file: "l3_our_q2_budget_was_lower.mp3", voice: ELLEN },
  { text: "The new platform is more profitable than the legacy system.", file: "l3_the_new_platform_is_more_profitable.mp3", voice: ARTHUR },
  { text: "Customer satisfaction is better than last year.", file: "l3_customer_satisfaction_is_better.mp3", voice: ELLEN },

  // ===== Fill-in sentences (alternate) =====
  { text: "Revenue in Q2 was higher than in Q1.", file: "l3_fill_revenue_q2_higher.mp3", voice: ARTHUR },
  { text: "The cloud division is more profitable than hardware.", file: "l3_fill_cloud_more_profitable.mp3", voice: ELLEN },
  { text: "Our costs this quarter are lower than last quarter.", file: "l3_fill_costs_lower.mp3", voice: ARTHUR },
  { text: "Growth in LATAM is faster than in Europe.", file: "l3_fill_growth_latam_faster.mp3", voice: ELLEN },
  { text: "The new forecast is better than the original estimate.", file: "l3_fill_forecast_better.mp3", voice: ARTHUR },

  // ===== Dialogue (Rafael=Arthur, Catherine=Ellen) =====
  { text: "Good afternoon, everyone. I would like to present the Q2 results for the IT division. Let me start with revenue.", file: "l3_dialogue_rafael_1.mp3", voice: ARTHUR },
  { text: "Thank you, Rafael. What were the key numbers for Q2?", file: "l3_dialogue_catherine_2.mp3", voice: ELLEN },
  { text: "Revenue was 2.3 million, which is 12 percent higher than Q1. Cloud services drove most of the growth.", file: "l3_dialogue_rafael_3.mp3", voice: ARTHUR },
  { text: "That is impressive. How does cloud compare to on-premise?", file: "l3_dialogue_catherine_4.mp3", voice: ELLEN },
  { text: "Cloud revenue is 40 percent higher than on-premise. And the ROI on our migration project was 3.2x, which exceeded the forecast.", file: "l3_dialogue_rafael_5.mp3", voice: ARTHUR },
  { text: "Good. What about the budget? Are we on track?", file: "l3_dialogue_catherine_6.mp3", voice: ELLEN },
  { text: "Yes. Our spending is 5 percent lower than the approved budget. We saved by renegotiating vendor contracts.", file: "l3_dialogue_rafael_7.mp3", voice: ARTHUR },
  { text: "Excellent work. And what is the forecast for Q3?", file: "l3_dialogue_catherine_8.mp3", voice: ELLEN },

  // ===== Listening 1 (Arthur - Rafael presenting) =====
  { text: "Good afternoon, board members. I am presenting the Q2 KPI report for IT. Revenue for the quarter was 2.3 million dollars, which is 12 percent higher than Q1. Cloud services generated 1.4 million, making it more profitable than on-premise by a significant margin. Customer acquisition cost dropped by 8 percent, lower than our target of 5 percent. Our budget utilization was 95 percent, and spending was lower than the approved budget. The ROI on the cloud migration project was 3.2 times, which is better than the industry average of 2.5 times. Looking at the forecast for Q3, we expect revenue growth of 15 percent. Hardware sales may see a slight decline, but cloud revenue should more than compensate.", file: "l3_listening1_kpi_presentation.mp3", voice: ARTHUR },

  // ===== Listening 2 (Ellen - CFO questions) =====
  { text: "Rafael, thank you for the Q2 report. I have a few questions. First, you mentioned that cloud revenue is higher than on-premise. By how much exactly? Second, the customer acquisition cost is lower than last quarter, but is it lower than the industry benchmark? And finally, your forecast shows growth of 15 percent for Q3. What assumptions are behind that number? Is it more conservative than the Q2 actuals, or more optimistic?", file: "l3_listening2_cfo_questions.mp3", voice: ELLEN },

  // ===== Survival card L3 (Arthur - student protagonist) =====
  { text: "Revenue increased by 12 percent compared to last quarter.", file: "l3_survival_revenue_increased.mp3", voice: ARTHUR },
  { text: "Our costs are lower than the approved budget.", file: "l3_survival_costs_lower.mp3", voice: ARTHUR },
  { text: "The ROI exceeded our forecast by a significant margin.", file: "l3_survival_roi_exceeded.mp3", voice: ARTHUR },
  { text: "Cloud services are more profitable than on-premise solutions.", file: "l3_survival_cloud_more_profitable.mp3", voice: ARTHUR },
  { text: "The forecast for Q3 shows a 15 percent increase in revenue.", file: "l3_survival_forecast_q3.mp3", voice: ARTHUR },

  // ===== Speech practice L3 (Arthur) =====
  { text: "Our Q2 revenue was 2.3 million dollars, which is 12 percent higher than Q1.", file: "l3_speech_q2_revenue.mp3", voice: ARTHUR },
  { text: "Cloud services are more profitable than on-premise solutions for our company.", file: "l3_speech_cloud_profitable.mp3", voice: ARTHUR },
  { text: "The forecast for Q3 shows continued growth and lower operational costs.", file: "l3_speech_forecast_q3.mp3", voice: ARTHUR },
];

if (!fs.existsSync(DIR)) fs.mkdirSync(DIR, { recursive: true });

async function generate(text, file, voiceId) {
  const filepath = path.join(DIR, file);
  if (fs.existsSync(filepath)) {
    console.log(`SKIP (exists): ${file}`);
    return;
  }
  console.log(`Generating: ${file} (${voiceId === ARTHUR ? 'Arthur' : 'Ellen'})`);
  const res = await fetch(`https://api.elevenlabs.io/v1/text-to-speech/${voiceId}`, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({
      text,
      model_id: 'eleven_multilingual_v2',
      voice_settings: { stability: 0.5, similarity_boost: 0.75 }
    })
  });
  if (!res.ok) { console.error(`FAIL: ${file} — ${res.status} ${await res.text()}`); return; }
  const buf = Buffer.from(await res.arrayBuffer());
  fs.writeFileSync(filepath, buf);
  console.log(`OK: ${file} (${(buf.length / 1024).toFixed(1)} KB)`);
}

async function main() {
  if (!API_KEY) { console.error('Set ELEVENLABS_API_KEY env var'); process.exit(1); }
  console.log(`Generating ${PHRASES.length} audio files for Rafael Pelizaro - Aula 3...`);
  for (const p of PHRASES) {
    await generate(p.text, p.file, p.voice);
    await new Promise(r => setTimeout(r, 500));
  }
  console.log('Done!');
}

main().catch(console.error);
