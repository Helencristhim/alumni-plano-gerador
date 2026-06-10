const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

// Voice rules:
// - Single words (1-2 words) = Ellen (female student)
// - MC protagonist exercises = Ellen
// - Male character lines (David) = Arthur
// - General phrases = ALTERNATE Arthur/Ellen

const PHRASES = [
  // ===== Vocab words (Ellen — female student) =====
  { text: "Revenue", file: "aula4_revenue.mp3", voice: ELLEN },
  { text: "Profit", file: "aula4_profit.mp3", voice: ELLEN },
  { text: "Budget", file: "aula4_budget.mp3", voice: ELLEN },
  { text: "Forecast", file: "aula4_forecast.mp3", voice: ELLEN },
  { text: "Expenses", file: "aula4_expenses.mp3", voice: ELLEN },
  { text: "Growth", file: "aula4_growth.mp3", voice: ELLEN },
  { text: "Margin", file: "aula4_margin.mp3", voice: ELLEN },
  { text: "Quarter", file: "aula4_quarter.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate Arthur/Ellen) =====
  { text: "Our revenue increased by twelve percent last quarter.", file: "aula4_our_revenue_increased.mp3", voice: ARTHUR },
  { text: "The company reported a net profit of two million dollars.", file: "aula4_the_company_reported.mp3", voice: ELLEN },
  { text: "We need to approve the budget for next quarter.", file: "aula4_we_need_to_approve.mp3", voice: ARTHUR },
  { text: "The forecast shows steady growth through Q4.", file: "aula4_the_forecast_shows.mp3", voice: ELLEN },
  { text: "Our operating expenses are lower than last year.", file: "aula4_our_operating_expenses.mp3", voice: ARTHUR },
  { text: "We achieved ten percent growth compared to Q2.", file: "aula4_we_achieved_ten_percent.mp3", voice: ELLEN },
  { text: "Our profit margin improved from eight to twelve percent.", file: "aula4_our_profit_margin_improved.mp3", voice: ARTHUR },
  { text: "Q3 results exceeded our expectations.", file: "aula4_q3_results_exceeded.mp3", voice: ELLEN },

  // ===== Key expressions (alternate) =====
  { text: "Compared to last quarter...", file: "aula4_expr_compared_to.mp3", voice: ARTHUR },
  { text: "Compared to last quarter, our revenue is up twelve percent.", file: "aula4_expr_compared_example.mp3", voice: ELLEN },
  { text: "The numbers show that...", file: "aula4_expr_numbers_show.mp3", voice: ARTHUR },
  { text: "The numbers show that our profit margin has improved significantly.", file: "aula4_expr_numbers_example.mp3", voice: ELLEN },
  { text: "We are on track to...", file: "aula4_expr_on_track.mp3", voice: ARTHUR },
  { text: "We are on track to exceed our annual revenue target.", file: "aula4_expr_on_track_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (narrative = Ellen) =====
  { text: "Maria Claudia is presenting the Q3 financial results to the board. Revenue is higher than Q2 by twelve percent. The profit margin improved from eight percent to twelve percent. Operating expenses are lower than last year because the procurement team negotiated better contracts. The Houston subsidiary showed the strongest growth, with revenue up fifteen percent compared to Q2. The forecast for Q4 is positive, and the budget has been approved. Overall, Q3 results are better than expected.", file: "aula4_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in-the-blank sentences (alternate) =====
  { text: "Our revenue is higher than last quarter.", file: "aula4_fill_revenue_higher.mp3", voice: ARTHUR },
  { text: "Operating expenses decreased by five percent.", file: "aula4_fill_expenses_decreased.mp3", voice: ELLEN },
  { text: "The profit margin improved from eight to twelve percent.", file: "aula4_fill_profit_margin.mp3", voice: ARTHUR },
  { text: "The forecast for Q4 shows steady growth.", file: "aula4_fill_forecast_q4.mp3", voice: ELLEN },
  { text: "We need to approve the budget for next year.", file: "aula4_fill_approve_budget.mp3", voice: ARTHUR },
  { text: "Q3 profit exceeded two million dollars.", file: "aula4_fill_q3_profit.mp3", voice: ELLEN },
  { text: "The Houston subsidiary achieved fifteen percent growth.", file: "aula4_fill_houston_growth.mp3", voice: ARTHUR },
  { text: "Q3 results are better than expected.", file: "aula4_fill_results_better.mp3", voice: ELLEN },

  // ===== Ordering audio (combined) =====
  { text: "Good morning. Let's review the Q3 financial results. First, our total revenue for Q3 was twelve million dollars. Compared to Q2, that is an increase of twelve percent. Our operating expenses were lower than expected. The profit margin improved from eight to twelve percent. The forecast for Q4 shows continued growth.", file: "aula4_order_financial_sequence.mp3", voice: ELLEN },

  // ===== Survival card phrases (MC = Ellen) =====
  { text: "Our revenue increased by twelve percent this quarter.", file: "aula4_surv_revenue_increased.mp3", voice: ELLEN },
  { text: "Compared to last year, our profit margin is higher.", file: "aula4_surv_profit_margin_higher.mp3", voice: ELLEN },
  { text: "The budget for next quarter is three million dollars.", file: "aula4_surv_budget_next_quarter.mp3", voice: ELLEN },
  { text: "We are on track to meet our annual targets.", file: "aula4_surv_on_track.mp3", voice: ELLEN },
  { text: "The forecast shows steady growth for Q4.", file: "aula4_surv_forecast_q4.mp3", voice: ELLEN },

  // ===== Speech practice (MC = Ellen) =====
  { text: "Our revenue increased by twelve percent compared to last quarter.", file: "aula4_speech_revenue_increased.mp3", voice: ELLEN },
  { text: "The profit margin is higher than Q2, at twelve percent.", file: "aula4_speech_profit_margin.mp3", voice: ELLEN },
  { text: "Operating expenses are lower than last year.", file: "aula4_speech_expenses_lower.mp3", voice: ELLEN },
  { text: "We are on track to exceed our annual targets.", file: "aula4_speech_on_track.mp3", voice: ELLEN },
  { text: "The forecast for Q4 shows steady growth.", file: "aula4_speech_forecast_q4.mp3", voice: ELLEN },

  // ===== IN CLASS — Listening 1 (MC presenting Q3 = Ellen) =====
  { text: "Good morning, everyone. Thank you for joining the Q3 review. Let me start with the headline numbers. Our total revenue for Q3 was twelve million dollars. That is higher than Q2 by twelve percent. The profit margin improved from eight percent to twelve percent. This is the best margin we have had in three years. Operating expenses decreased by five percent compared to last year. The procurement team negotiated better contracts with our suppliers. Looking at our subsidiaries, Houston showed the strongest growth at fifteen percent. Pittsburgh was steady at eight percent. The forecast for Q4 is positive. We are on track to exceed our annual target of forty-five million dollars. The budget for Q4 has been approved. Are there any questions?", file: "aula4_ic_listening1_q3_results.mp3", voice: ELLEN },

  // ===== IN CLASS — Listening 2 (David reporting = Arthur) =====
  { text: "Thanks, Maria Claudia. Let me share the Pittsburgh numbers in more detail. Our revenue for Q3 was three point five million dollars. That is eight percent higher than Q2. However, our expenses were slightly higher than expected because of the new logistics contract. The profit margin in Pittsburgh is ten percent, which is lower than Houston's fifteen percent. We need to work on reducing expenses next quarter. The forecast shows that we can improve the margin to twelve percent by Q4 if we renegotiate two key contracts. Compared to last year, overall growth is positive. We are on track to meet our targets.", file: "aula4_ic_listening2_david_revenue.mp3", voice: ARTHUR },

  // ===== IN CLASS — Dialogue lines =====
  { text: "Good morning, David. Let's review the Q3 numbers. Revenue is looking strong this quarter.", file: "aula4_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "Good morning, Maria Claudia. Yes, total revenue is higher than Q2. Twelve million dollars overall.", file: "aula4_ic_dlg_david_1.mp3", voice: ARTHUR },
  { text: "That is excellent. How does the profit margin compare to last quarter?", file: "aula4_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "The margin improved from eight to twelve percent. Better than expected.", file: "aula4_ic_dlg_david_2.mp3", voice: ARTHUR },
  { text: "And what about expenses? Are they lower than Q2?", file: "aula4_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "Operating expenses decreased by five percent. The procurement team did a great job.", file: "aula4_ic_dlg_david_3.mp3", voice: ARTHUR },
  { text: "Good. The numbers show that Houston is growing faster than Pittsburgh. Fifteen percent versus eight.", file: "aula4_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "That is correct. But Pittsburgh's forecast for Q4 is very positive. We are on track to close the gap.", file: "aula4_ic_dlg_david_4.mp3", voice: ARTHUR },
  { text: "Let's approve the Q4 budget then. Three million for Houston, two point five for Pittsburgh.", file: "aula4_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Agreed. Compared to last year, we are in a much stronger position. Great quarter, Maria Claudia.", file: "aula4_ic_dlg_david_5.mp3", voice: ARTHUR },

  // ===== IN CLASS — Error correction sentences =====
  { text: "Revenue is more higher than last quarter.", file: "aula4_ic_error_more_higher.mp3", voice: ARTHUR },
  { text: "The profit is gooder than Q2.", file: "aula4_ic_error_gooder.mp3", voice: ELLEN },
  { text: "Our expenses is lower than expected.", file: "aula4_ic_error_expenses_is.mp3", voice: ARTHUR },
  { text: "The growth is more better this year.", file: "aula4_ic_error_more_better.mp3", voice: ELLEN },
  { text: "We achieved ten percents growth.", file: "aula4_ic_error_percents.mp3", voice: ARTHUR },
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

  console.log('Generating ' + unique.length + ' AULA 4 audio files for Maria Claudia Curimbaba...');
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

  console.log('\nDone! Generated: ' + generated + ' | Skipped: ' + skipped + ' | Total: ' + unique.length);
}

main();
