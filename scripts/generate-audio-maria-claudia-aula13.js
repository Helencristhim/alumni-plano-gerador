const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab (Ellen) =====
  { text: "Pitch", file: "aula13_pitch.mp3", voice: ELLEN },
  { text: "Propose", file: "aula13_propose.mp3", voice: ELLEN },
  { text: "Feasible", file: "aula13_feasible.mp3", voice: ELLEN },
  { text: "Stakeholder", file: "aula13_stakeholder.mp3", voice: ELLEN },
  { text: "Timeline", file: "aula13_timeline.mp3", voice: ELLEN },
  { text: "ROI", file: "aula13_roi.mp3", voice: ELLEN },
  { text: "Scalable", file: "aula13_scalable.mp3", voice: ELLEN },
  { text: "Implementation", file: "aula13_implementation.mp3", voice: ELLEN },

  // ===== Vocab examples (alternate) =====
  { text: "Maria Claudia will pitch the expansion plan to the board.", file: "aula13_mc_will_pitch.mp3", voice: ARTHUR },
  { text: "I would like to propose a new partnership with the Houston team.", file: "aula13_i_would_like_to_propose.mp3", voice: ELLEN },
  { text: "The board wants to know if the project is feasible within the budget.", file: "aula13_the_board_wants.mp3", voice: ARTHUR },
  { text: "All stakeholders must approve the proposal before we proceed.", file: "aula13_all_stakeholders.mp3", voice: ELLEN },
  { text: "The project timeline spans six months, from January to June.", file: "aula13_the_project_timeline.mp3", voice: ARTHUR },
  { text: "The projected ROI for this venture is twenty percent.", file: "aula13_the_projected_roi.mp3", voice: ELLEN },
  { text: "We need a solution that is scalable across all three subsidiaries.", file: "aula13_we_need_a_solution.mp3", voice: ARTHUR },
  { text: "The implementation phase will begin in Q2.", file: "aula13_the_implementation_phase.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "I would like to propose...", file: "aula13_expr_i_would_like.mp3", voice: ARTHUR },
  { text: "I would like to propose expanding our logistics operations to Miami.", file: "aula13_expr_propose_example.mp3", voice: ELLEN },
  { text: "What I am suggesting is...", file: "aula13_expr_what_i_am.mp3", voice: ARTHUR },
  { text: "What I am suggesting is a phased approach to the expansion.", file: "aula13_expr_suggesting_example.mp3", voice: ELLEN },
  { text: "The key benefit is...", file: "aula13_expr_key_benefit.mp3", voice: ARTHUR },
  { text: "The key benefit is a twenty percent increase in ROI within two years.", file: "aula13_expr_benefit_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is pitching a new expansion plan to the board. I would like to propose opening a new logistics hub in Miami, she begins. What I am suggesting is a phased implementation over six months. The timeline spans from January to June. I would like to recommend starting with a feasibility study in Q1. The projected ROI is twenty percent within the first two years. All stakeholders have been consulted, and the solution is scalable across our three subsidiaries. The key benefit is that we will reduce shipping times to Houston by forty percent. I would recommend that we approve the budget today so implementation can begin on schedule.", file: "aula13_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in (alternate) =====
  { text: "Maria Claudia will pitch the expansion plan to the board.", file: "aula13_fill_pitch.mp3", voice: ARTHUR },
  { text: "I would like to propose a new partnership.", file: "aula13_fill_propose.mp3", voice: ELLEN },
  { text: "The board wants to know if the project is feasible.", file: "aula13_fill_feasible.mp3", voice: ARTHUR },
  { text: "All stakeholders must approve the proposal.", file: "aula13_fill_stakeholders.mp3", voice: ELLEN },
  { text: "The project timeline spans six months.", file: "aula13_fill_timeline.mp3", voice: ARTHUR },
  { text: "The projected ROI is twenty percent.", file: "aula13_fill_roi.mp3", voice: ELLEN },
  { text: "We need a solution that is scalable.", file: "aula13_fill_scalable.mp3", voice: ARTHUR },
  { text: "The implementation phase will begin in Q2.", file: "aula13_fill_implementation.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "Good morning. I would like to propose an expansion plan. What I am suggesting is a phased approach over six months. The projected ROI is twenty percent within two years. The solution is scalable across all three subsidiaries. I would recommend starting with a feasibility study. The key benefit is reduced shipping times to Houston.", file: "aula13_order_pitch_sequence.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "I would like to propose a new plan.", file: "aula13_surv_propose_plan.mp3", voice: ELLEN },
  { text: "What I am suggesting is a phased approach.", file: "aula13_surv_suggesting.mp3", voice: ELLEN },
  { text: "The projected ROI is very positive.", file: "aula13_surv_roi.mp3", voice: ELLEN },
  { text: "The solution is scalable and feasible.", file: "aula13_surv_scalable.mp3", voice: ELLEN },
  { text: "I would recommend starting in Q2.", file: "aula13_surv_recommend.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "I would like to propose expanding our logistics operations.", file: "aula13_speech_propose.mp3", voice: ELLEN },
  { text: "What I am suggesting is a phased implementation.", file: "aula13_speech_suggesting.mp3", voice: ELLEN },
  { text: "The projected ROI is twenty percent within two years.", file: "aula13_speech_roi.mp3", voice: ELLEN },
  { text: "The solution is scalable across all subsidiaries.", file: "aula13_speech_scalable.mp3", voice: ELLEN },
  { text: "I would recommend that we approve the budget today.", file: "aula13_speech_recommend.mp3", voice: ELLEN },

  // ===== Listening 1 (MC pitches = Ellen) =====
  { text: "Good morning, everyone. Thank you for your time today. I would like to propose a new strategic initiative: opening a logistics hub in Miami. What I am suggesting is a phased implementation over six months, starting in Q2. The timeline is aggressive but feasible. We have consulted all key stakeholders, including our partners in Houston and Pittsburgh. The projected ROI is twenty percent within the first two years. The solution is fully scalable. If we start with Miami, we can replicate the model in other cities. The key benefit is a forty percent reduction in shipping times to our US clients. I would recommend that we approve the initial budget of one point five million dollars today so the implementation team can begin the feasibility study next month. I am confident this is the right move for the holding.", file: "aula13_ic_listening1_mc_pitches.mp3", voice: ELLEN },

  // ===== Listening 2 (David = Arthur) =====
  { text: "Thank you, Maria Claudia. That was a compelling pitch. I would like to propose a complementary initiative for Pittsburgh. What I am suggesting is upgrading our manufacturing technology. The timeline would be similar, about six months. The projected ROI is fifteen percent, which is slightly lower than Miami, but the implementation cost is also lower. All stakeholders in Pittsburgh support this proposal. The key benefit is that the upgrade is scalable to our other manufacturing sites. I would recommend that we run both projects in parallel. The combined ROI would be even stronger. If the board approves both proposals today, we can begin the feasibility studies simultaneously.", file: "aula13_ic_listening2_david_proposal.mp3", voice: ARTHUR },

  // ===== Dialogue =====
  { text: "I would like to propose opening a logistics hub in Miami. The projected ROI is twenty percent.", file: "aula13_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "That sounds promising. Is the timeline feasible? Six months is quite aggressive.", file: "aula13_ic_dlg_david_1.mp3", voice: ARTHUR },
  { text: "What I am suggesting is a phased approach. Phase one is the feasibility study, phase two is implementation.", file: "aula13_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "Have all stakeholders been consulted? What does the Houston team think?", file: "aula13_ic_dlg_david_2.mp3", voice: ARTHUR },
  { text: "Yes. All stakeholders support the proposal. Houston is particularly enthusiastic about reduced shipping times.", file: "aula13_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "The key benefit for Houston is clear. But is the solution scalable to other locations?", file: "aula13_ic_dlg_david_3.mp3", voice: ARTHUR },
  { text: "Absolutely. The model is fully scalable. If Miami succeeds, we can replicate it in other cities.", file: "aula13_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "I would like to propose running the Pittsburgh upgrade in parallel. The combined ROI would be stronger.", file: "aula13_ic_dlg_david_4.mp3", voice: ARTHUR },
  { text: "That is an excellent idea. I would recommend that we approve both budgets today.", file: "aula13_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Agreed. The implementation teams can start the feasibility studies next month. Great pitch, Maria Claudia.", file: "aula13_ic_dlg_david_5.mp3", voice: ARTHUR },

  // ===== Error correction =====
  { text: "I would like to suggesting a new plan.", file: "aula13_ic_error_suggesting.mp3", voice: ARTHUR },
  { text: "I propose to expanding the operations.", file: "aula13_ic_error_to_expanding.mp3", voice: ELLEN },
  { text: "What I am suggest is a phased approach.", file: "aula13_ic_error_am_suggest.mp3", voice: ARTHUR },
  { text: "I would like recommend starting in Q2.", file: "aula13_ic_error_like_recommend.mp3", voice: ELLEN },
  { text: "The key benefit are reduced shipping times.", file: "aula13_ic_error_benefit_are.mp3", voice: ARTHUR },
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
  console.log('Generating ' + unique.length + ' AULA 13 audio files...');
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
