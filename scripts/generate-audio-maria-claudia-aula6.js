const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab words (Ellen — female student) =====
  { text: "Submit", file: "aula6_submit.mp3", voice: ELLEN },
  { text: "Approve", file: "aula6_approve.mp3", voice: ELLEN },
  { text: "Review", file: "aula6_review.mp3", voice: ELLEN },
  { text: "Assign", file: "aula6_assign.mp3", voice: ELLEN },
  { text: "Display", file: "aula6_display.mp3", voice: ELLEN },
  { text: "Commission", file: "aula6_commission.mp3", voice: ELLEN },
  { text: "Distribute", file: "aula6_distribute.mp3", voice: ELLEN },
  { text: "Evaluate", file: "aula6_evaluate.mp3", voice: ELLEN },

  // ===== Vocab example sentences (alternate) =====
  { text: "Reports are submitted to the board every quarter.", file: "aula6_reports_are_submitted.mp3", voice: ARTHUR },
  { text: "The budget is approved by the shareholders.", file: "aula6_the_budget_is_approved.mp3", voice: ELLEN },
  { text: "Financial statements are reviewed by the auditors.", file: "aula6_financial_statements_are.mp3", voice: ARTHUR },
  { text: "Action items are assigned at the end of each meeting.", file: "aula6_action_items_are_assigned.mp3", voice: ELLEN },
  { text: "Contemporary paintings are displayed in the main gallery.", file: "aula6_contemporary_paintings_are.mp3", voice: ARTHUR },
  { text: "New artworks are commissioned by the museum every year.", file: "aula6_new_artworks_are.mp3", voice: ELLEN },
  { text: "Meeting minutes are distributed to all participants.", file: "aula6_meeting_minutes_are.mp3", voice: ARTHUR },
  { text: "Employee performance is evaluated twice a year.", file: "aula6_employee_performance_is.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "It is done by...", file: "aula6_expr_it_is_done_by.mp3", voice: ARTHUR },
  { text: "The report is reviewed by the finance team before submission.", file: "aula6_expr_done_by_example.mp3", voice: ELLEN },
  { text: "It is considered...", file: "aula6_expr_it_is_considered.mp3", voice: ARTHUR },
  { text: "This painting is considered one of the most important works of the century.", file: "aula6_expr_considered_example.mp3", voice: ELLEN },
  { text: "It has been...", file: "aula6_expr_it_has_been.mp3", voice: ARTHUR },
  { text: "The budget has been approved by the board.", file: "aula6_expr_has_been_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is explaining how her company operates to a new partner. Reports are submitted to the board every quarter. The annual budget is approved by the shareholders in January. Financial statements are reviewed by external auditors. Action items are assigned at the end of each meeting, and meeting minutes are distributed to all participants within 24 hours. On the art side, Maria Claudia explains that contemporary paintings are displayed in the company's lobby. New artworks are commissioned every two years. Each piece is evaluated by a committee before it is purchased.", file: "aula6_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in sentences (alternate) =====
  { text: "Reports are submitted to the board every quarter.", file: "aula6_fill_reports_submitted.mp3", voice: ARTHUR },
  { text: "The budget is approved by the shareholders.", file: "aula6_fill_budget_approved.mp3", voice: ELLEN },
  { text: "Financial statements are reviewed by the auditors.", file: "aula6_fill_statements_reviewed.mp3", voice: ARTHUR },
  { text: "Action items are assigned at the end of each meeting.", file: "aula6_fill_items_assigned.mp3", voice: ELLEN },
  { text: "Contemporary paintings are displayed in the main gallery.", file: "aula6_fill_paintings_displayed.mp3", voice: ARTHUR },
  { text: "New artworks are commissioned by the museum every year.", file: "aula6_fill_artworks_commissioned.mp3", voice: ELLEN },
  { text: "Meeting minutes are distributed to all participants.", file: "aula6_fill_minutes_distributed.mp3", voice: ARTHUR },
  { text: "Employee performance is evaluated twice a year.", file: "aula6_fill_performance_evaluated.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "The report is written by the finance team. It is reviewed by the department manager. Corrections are made based on the feedback. The final version is submitted to the board. The report is approved by the shareholders. Copies are distributed to all stakeholders.", file: "aula6_order_report_flow.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "The report is submitted every quarter.", file: "aula6_surv_report_submitted.mp3", voice: ELLEN },
  { text: "The budget has been approved by the board.", file: "aula6_surv_budget_approved.mp3", voice: ELLEN },
  { text: "Paintings are displayed in the main gallery.", file: "aula6_surv_paintings_displayed.mp3", voice: ELLEN },
  { text: "Minutes are distributed after every meeting.", file: "aula6_surv_minutes_distributed.mp3", voice: ELLEN },
  { text: "New artworks are commissioned every two years.", file: "aula6_surv_artworks_commissioned.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "Reports are submitted to the board every quarter.", file: "aula6_speech_reports_submitted.mp3", voice: ELLEN },
  { text: "The budget is approved by the shareholders in January.", file: "aula6_speech_budget_approved.mp3", voice: ELLEN },
  { text: "Contemporary paintings are displayed in our lobby.", file: "aula6_speech_paintings_displayed.mp3", voice: ELLEN },
  { text: "Meeting minutes are distributed within 24 hours.", file: "aula6_speech_minutes_distributed.mp3", voice: ELLEN },
  { text: "Each artwork is evaluated before it is purchased.", file: "aula6_speech_artwork_evaluated.mp3", voice: ELLEN },

  // ===== Listening 1 (MC = Ellen) =====
  { text: "Let me explain how our company operates. All financial reports are submitted to the board every quarter. The annual budget is prepared by the finance team and approved by the shareholders in January. Every transaction is reviewed by our external auditors. At the operational level, action items are assigned during weekly meetings, and minutes are distributed within 24 hours. On a personal note, I am passionate about art. Contemporary paintings are displayed throughout our offices. New pieces are commissioned every two years, and each artwork is carefully evaluated by a selection committee before it is purchased. Art and business are connected in everything we do.", file: "aula6_ic_listening1_company_operates.mp3", voice: ELLEN },

  // ===== Listening 2 (David = Arthur) =====
  { text: "In Pittsburgh, our processes are slightly different. Reports are submitted monthly, not quarterly. They are reviewed by both the local manager and the regional director. The budget is prepared in November and approved in December, one month earlier than Sao Paulo. Meeting minutes are written by a dedicated assistant and distributed the same day. We also have art in our offices, but the pieces are selected differently. Artworks are chosen by an employee committee, not commissioned. They are rotated every six months so everyone can enjoy different pieces. Each selection is evaluated based on employee feedback.", file: "aula6_ic_listening2_david_process.mp3", voice: ARTHUR },

  // ===== Dialogue =====
  { text: "David, how are reports handled in Pittsburgh?", file: "aula6_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "Reports are submitted monthly and reviewed by both the local manager and the regional director.", file: "aula6_ic_dlg_david_1.mp3", voice: ARTHUR },
  { text: "Interesting. In Sao Paulo, they are submitted quarterly. When is your budget approved?", file: "aula6_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "The budget is prepared in November and approved in December. One month earlier than yours.", file: "aula6_ic_dlg_david_2.mp3", voice: ARTHUR },
  { text: "That is efficient. How are meeting minutes distributed?", file: "aula6_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "They are written by a dedicated assistant and distributed the same day.", file: "aula6_ic_dlg_david_3.mp3", voice: ARTHUR },
  { text: "We should adopt that practice. And I noticed the art in your lobby. How are the pieces selected?", file: "aula6_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "Artworks are chosen by an employee committee and rotated every six months.", file: "aula6_ic_dlg_david_4.mp3", voice: ARTHUR },
  { text: "That is a wonderful idea. In Sao Paulo, new pieces are commissioned every two years.", file: "aula6_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Both approaches work well. It is considered important to have art in the workplace.", file: "aula6_ic_dlg_david_5.mp3", voice: ARTHUR },

  // ===== Error correction =====
  { text: "The report is write by the team.", file: "aula6_ic_error_is_write.mp3", voice: ARTHUR },
  { text: "The paintings is displayed in the gallery.", file: "aula6_ic_error_paintings_is.mp3", voice: ELLEN },
  { text: "The budget are approved by the board.", file: "aula6_ic_error_budget_are.mp3", voice: ARTHUR },
  { text: "Minutes is distributed after the meeting.", file: "aula6_ic_error_minutes_is.mp3", voice: ELLEN },
  { text: "The artwork is evaluate by the committee.", file: "aula6_ic_error_is_evaluate.mp3", voice: ARTHUR },
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
  console.log('Generating ' + unique.length + ' AULA 6 audio files...');
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
