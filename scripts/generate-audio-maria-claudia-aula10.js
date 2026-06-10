const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab (Ellen) =====
  { text: "Oversee", file: "aula10_oversee.mp3", voice: ELLEN },
  { text: "Subsidiary", file: "aula10_subsidiary.mp3", voice: ELLEN },
  { text: "Facilitate", file: "aula10_facilitate.mp3", voice: ELLEN },
  { text: "Forecast", file: "aula10_forecast.mp3", voice: ELLEN },
  { text: "Composition", file: "aula10_composition.mp3", voice: ELLEN },
  { text: "Evaluate", file: "aula10_evaluate.mp3", voice: ELLEN },
  { text: "Leverage", file: "aula10_leverage.mp3", voice: ELLEN },
  { text: "Integrate", file: "aula10_integrate.mp3", voice: ELLEN },

  // ===== Vocab examples (alternate) =====
  { text: "Maria Claudia oversees the financial operations of the holding.", file: "aula10_mc_oversees.mp3", voice: ARTHUR },
  { text: "The holding has three subsidiaries in different sectors.", file: "aula10_holding_has_three.mp3", voice: ELLEN },
  { text: "She facilitates the quarterly review meetings.", file: "aula10_she_facilitates.mp3", voice: ARTHUR },
  { text: "The forecast for Q4 shows steady growth.", file: "aula10_forecast_q4.mp3", voice: ELLEN },
  { text: "The composition of this painting is remarkable.", file: "aula10_composition_remarkable.mp3", voice: ARTHUR },
  { text: "Performance is evaluated twice a year.", file: "aula10_performance_evaluated.mp3", voice: ELLEN },
  { text: "Our volume gives us leverage to negotiate.", file: "aula10_volume_leverage.mp3", voice: ARTHUR },
  { text: "Maria Claudia integrates art and business in everything she does.", file: "aula10_mc_integrates.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "Looking back at...", file: "aula10_expr_looking_back.mp3", voice: ARTHUR },
  { text: "Looking back at this quarter, our results exceeded expectations.", file: "aula10_expr_looking_back_example.mp3", voice: ELLEN },
  { text: "Overall, I would say...", file: "aula10_expr_overall.mp3", voice: ARTHUR },
  { text: "Overall, I would say the holding is in a strong position.", file: "aula10_expr_overall_example.mp3", voice: ELLEN },
  { text: "To summarize...", file: "aula10_expr_to_summarize.mp3", voice: ARTHUR },
  { text: "To summarize, we achieved growth in all three subsidiaries.", file: "aula10_expr_summarize_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is hosting a business dinner for her Houston and Pittsburgh counterparts at an art gallery in Sao Paulo. She oversees the evening's agenda. Let's begin with a toast, she says. Looking back at this year, our revenue is higher than last year by fifteen percent. The forecast for next quarter is positive. Reports are submitted on time, and every action item has been completed. I believe we have the leverage to negotiate even better contracts next year. If we continue at this pace, we will exceed our annual targets. She then turns to the art on the walls. I find this composition absolutely stunning. In my opinion, it is the highlight of the gallery. What is your take on it, David? Overall, the evening integrates business discussion with art appreciation.", file: "aula10_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in (alternate) =====
  { text: "Maria Claudia oversees the financial operations of the holding.", file: "aula10_fill_oversees.mp3", voice: ARTHUR },
  { text: "Revenue is higher than last year by fifteen percent.", file: "aula10_fill_revenue_higher.mp3", voice: ELLEN },
  { text: "Let's begin with a review of the quarterly results.", file: "aula10_fill_lets_begin.mp3", voice: ARTHUR },
  { text: "Reports are submitted to the board every quarter.", file: "aula10_fill_reports_submitted.mp3", voice: ELLEN },
  { text: "If we continue at this pace, we will exceed our targets.", file: "aula10_fill_if_continue.mp3", voice: ARTHUR },
  { text: "I find this painting absolutely stunning.", file: "aula10_fill_find_stunning.mp3", voice: ELLEN },
  { text: "I am writing regarding the revised contract.", file: "aula10_fill_writing_regarding.mp3", voice: ARTHUR },
  { text: "Maria Claudia integrates art and business in everything she does.", file: "aula10_fill_integrates.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "Good evening, everyone. Welcome to this special dinner. Let's begin with a toast to a successful quarter. Looking back, our revenue is higher than last year. The forecast shows continued growth for all subsidiaries. Now, let me show you the art collection. I find this piece stunning. To summarize, we achieved our goals in business and enjoyed great art tonight.", file: "aula10_order_dinner_sequence.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "Looking back, our results exceeded expectations.", file: "aula10_surv_looking_back.mp3", voice: ELLEN },
  { text: "If we continue at this pace, we will succeed.", file: "aula10_surv_if_continue.mp3", voice: ELLEN },
  { text: "I find this absolutely stunning.", file: "aula10_surv_find_stunning.mp3", voice: ELLEN },
  { text: "To summarize, we achieved all our goals.", file: "aula10_surv_to_summarize.mp3", voice: ELLEN },
  { text: "It was a pleasure hosting you tonight.", file: "aula10_surv_pleasure_hosting.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "Looking back at this quarter, our results exceeded expectations.", file: "aula10_speech_looking_back.mp3", voice: ELLEN },
  { text: "If we continue at this pace, we will exceed our annual targets.", file: "aula10_speech_if_continue.mp3", voice: ELLEN },
  { text: "I find this composition absolutely stunning.", file: "aula10_speech_find_stunning.mp3", voice: ELLEN },
  { text: "Reports are submitted on time and every action item is completed.", file: "aula10_speech_reports_submitted.mp3", voice: ELLEN },
  { text: "To summarize, we achieved growth in all three subsidiaries.", file: "aula10_speech_to_summarize.mp3", voice: ELLEN },

  // ===== Listening 1 (MC dinner speech = Ellen) =====
  { text: "Good evening, everyone. Welcome to this very special dinner. I am delighted to host you here at the Galeria Contemporanea in Sao Paulo. Looking back at this year, I am proud of what we have achieved together. Our total revenue is higher than last year by fifteen percent. The Houston subsidiary showed the strongest growth, and Pittsburgh met all its targets. Reports are submitted on time, budgets are approved, and every action item from our quarterly reviews has been completed. The forecast for next year is very positive. If we continue at this pace, we will exceed our annual targets by at least ten percent. I believe we have the leverage to negotiate even better contracts with our vendors. Now, before we sit down to dinner, I would like to show you something. I find this painting behind me absolutely stunning. The composition is bold, the palette is vibrant, and in my opinion, it is the highlight of this gallery. What is your take on it? To summarize, this has been a remarkable year for the holding. Let us toast to continued success. Cheers.", file: "aula10_ic_listening1_mc_dinner.mp3", voice: ELLEN },

  // ===== Listening 2 (David toast = Arthur) =====
  { text: "Thank you, Maria Claudia, for hosting this wonderful evening. If you ask me, this is the best business dinner I have attended all year. Looking back at our partnership, I am impressed by how much we have achieved. Revenue in Pittsburgh is higher than expected. We negotiated better contracts, and I believe our leverage in the market is stronger than ever. I would like to acknowledge Maria Claudia's leadership. She oversees every detail, facilitates every meeting, and integrates art and business like no one else. I find this gallery absolutely stunning. The composition of the paintings and the atmosphere of the evening create a unique perspective on what business can be. Overall, I would say that the future of our partnership is very bright. If we continue working together like this, we will achieve extraordinary things. To summarize, great results, great art, great company. Cheers.", file: "aula10_ic_listening2_david_toast.mp3", voice: ARTHUR },

  // ===== Dialogue =====
  { text: "David, I am so glad you could join us tonight. What is your take on the gallery?", file: "aula10_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "It is absolutely stunning. I find the large abstract painting near the entrance particularly powerful.", file: "aula10_ic_dlg_david_1.mp3", voice: ARTHUR },
  { text: "I agree. The composition is remarkable. Looking back, I remember when we first discussed combining business dinners with art.", file: "aula10_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "It was a great idea. If you ask me, it makes the evening much more memorable. How are the Q3 results?", file: "aula10_ic_dlg_david_2.mp3", voice: ARTHUR },
  { text: "Revenue is higher than last year. Reports are submitted on time. The forecast is very positive.", file: "aula10_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "That is excellent. If we continue at this pace, we will exceed our targets. Do we have leverage for the new vendor contract?", file: "aula10_ic_dlg_david_3.mp3", voice: ARTHUR },
  { text: "Absolutely. I believe our volume gives us strong leverage. We are willing to negotiate better terms.", file: "aula10_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "I will follow up with the procurement team. Let me also acknowledge your team's excellent work this quarter.", file: "aula10_ic_dlg_david_4.mp3", voice: ARTHUR },
  { text: "Thank you, David. To summarize, we achieved our goals and enjoyed a beautiful evening of art. Let us toast.", file: "aula10_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Cheers, Maria Claudia. Overall, I would say this has been the best quarter yet. Here is to an even better next one.", file: "aula10_ic_dlg_david_5.mp3", voice: ARTHUR },

  // ===== Error correction (mixed from all lessons) =====
  { text: "Revenue is more higher than last year.", file: "aula10_ic_error_more_higher.mp3", voice: ARTHUR },
  { text: "Let's to begin with the toast.", file: "aula10_ic_error_lets_to.mp3", voice: ELLEN },
  { text: "The report is write by the team.", file: "aula10_ic_error_is_write.mp3", voice: ARTHUR },
  { text: "If we will continue, we exceed our targets.", file: "aula10_ic_error_will_continue.mp3", voice: ELLEN },
  { text: "I am think this painting is beautiful.", file: "aula10_ic_error_am_think.mp3", voice: ARTHUR },
];

async function gen(text, voiceId, outPath) {
  const r = await fetch('https://api.elevenlabs.io/v1/text-to-speech/' + voiceId, {
    method: 'POST',
    headers: { 'xi-api-key': API_KEY, 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, model_id: 'eleven_multilingual_v2', voice_settings: { stability: 0.5, similarity_boost: 0.75 } }),
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
  const unique = PHRASES.filter(p => { const k = p.file.toLowerCase(); if (seen.has(k)) return false; seen.add(k); return true; });
  console.log('Generating ' + unique.length + ' AULA 10 audio files...');
  let generated = 0, skipped = 0;
  for (const p of unique) {
    const outPath = path.join(DIR, p.file);
    if (fs.existsSync(outPath)) { console.log('SKIP: ' + p.file); skipped++; }
    else {
      try {
        const bytes = await gen(p.text, p.voice, outPath);
        console.log('OK [' + (p.voice === ELLEN ? 'ellen' : 'arthur') + ']: ' + p.file + ' (' + (bytes / 1024).toFixed(1) + 'KB)');
        generated++;
        await new Promise(r => setTimeout(r, 500));
      } catch (e) { console.error('FAIL: ' + p.file + ' — ' + e.message); }
    }
  }
  console.log('\nDone! Generated: ' + generated + ' | Skipped: ' + skipped + ' | Total: ' + unique.length);
}
main();
