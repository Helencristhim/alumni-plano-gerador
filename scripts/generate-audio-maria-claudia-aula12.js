const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab (Ellen) =====
  { text: "Tax return", file: "aula12_tax_return.mp3", voice: ELLEN },
  { text: "Audit", file: "aula12_audit.mp3", voice: ELLEN },
  { text: "Deduction", file: "aula12_deduction.mp3", voice: ELLEN },
  { text: "Compliance", file: "aula12_compliance.mp3", voice: ELLEN },
  { text: "Liability", file: "aula12_liability.mp3", voice: ELLEN },
  { text: "Fiscal year", file: "aula12_fiscal_year.mp3", voice: ELLEN },
  { text: "Revenue stream", file: "aula12_revenue_stream.mp3", voice: ELLEN },
  { text: "Write-off", file: "aula12_write_off.mp3", voice: ELLEN },

  // ===== Vocab examples (alternate) =====
  { text: "We have filed our tax return for the fiscal year.", file: "aula12_we_have_filed.mp3", voice: ARTHUR },
  { text: "The company has been under audit since January.", file: "aula12_the_company_has_been.mp3", voice: ELLEN },
  { text: "We have claimed several deductions for business travel.", file: "aula12_we_have_claimed.mp3", voice: ARTHUR },
  { text: "The holding has maintained compliance with tax regulations for five years.", file: "aula12_the_holding_has_maintained.mp3", voice: ELLEN },
  { text: "Our tax liability has decreased since we restructured.", file: "aula12_our_tax_liability.mp3", voice: ARTHUR },
  { text: "Our fiscal year has ended on December 31st since 2018.", file: "aula12_our_fiscal_year.mp3", voice: ELLEN },
  { text: "We have diversified our revenue streams since the acquisition.", file: "aula12_we_have_diversified.mp3", voice: ARTHUR },
  { text: "The accountant has recommended a write-off for the old equipment.", file: "aula12_the_accountant_has.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "We have been... for, since...", file: "aula12_expr_we_have_been.mp3", voice: ARTHUR },
  { text: "We have been working with this accounting firm for three years.", file: "aula12_expr_been_working_example.mp3", voice: ELLEN },
  { text: "Since the restructuring...", file: "aula12_expr_since_restructuring.mp3", voice: ARTHUR },
  { text: "Since the restructuring, our tax liability has decreased significantly.", file: "aula12_expr_since_example.mp3", voice: ELLEN },
  { text: "For the past...", file: "aula12_expr_for_the_past.mp3", voice: ARTHUR },
  { text: "For the past two quarters, revenue has exceeded projections.", file: "aula12_expr_for_past_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is meeting with the company's accountant to review the fiscal year. We have filed our tax return for this fiscal year, the accountant explains. The company has maintained compliance with all regulations since the restructuring in 2022. We have claimed several deductions for business travel and equipment. Our tax liability has decreased significantly since last year. The audit team has been reviewing our records for the past three months. They have not found any issues. We have diversified our revenue streams since the acquisition of the Texas subsidiary. The accountant has recommended a write-off for the old logistics equipment.", file: "aula12_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in (alternate) =====
  { text: "We have filed our tax return for the fiscal year.", file: "aula12_fill_tax_return.mp3", voice: ARTHUR },
  { text: "The company has been under audit since January.", file: "aula12_fill_audit.mp3", voice: ELLEN },
  { text: "We have claimed several deductions for business travel.", file: "aula12_fill_deductions.mp3", voice: ARTHUR },
  { text: "The holding has maintained compliance for five years.", file: "aula12_fill_compliance.mp3", voice: ELLEN },
  { text: "Our tax liability has decreased since we restructured.", file: "aula12_fill_liability.mp3", voice: ARTHUR },
  { text: "Our fiscal year ends on December 31st.", file: "aula12_fill_fiscal_year.mp3", voice: ELLEN },
  { text: "We have diversified our revenue streams since the acquisition.", file: "aula12_fill_revenue_streams.mp3", voice: ARTHUR },
  { text: "The accountant recommended a write-off for the old equipment.", file: "aula12_fill_write_off.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "Let me review the financial records for this fiscal year. We have filed the tax return with the government. We have claimed all eligible deductions. The audit team has been reviewing our records for three months. Our tax liability has decreased since the restructuring. We have maintained full compliance with all tax regulations.", file: "aula12_order_fiscal_sequence.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "We have filed our tax return for this fiscal year.", file: "aula12_surv_tax_return.mp3", voice: ELLEN },
  { text: "The company has maintained compliance since 2022.", file: "aula12_surv_compliance.mp3", voice: ELLEN },
  { text: "Our tax liability has decreased since the restructuring.", file: "aula12_surv_liability.mp3", voice: ELLEN },
  { text: "We have been working with this firm for five years.", file: "aula12_surv_working_firm.mp3", voice: ELLEN },
  { text: "The audit has been in progress for three months.", file: "aula12_surv_audit_progress.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "We have filed our tax return for this fiscal year.", file: "aula12_speech_tax_return.mp3", voice: ELLEN },
  { text: "The company has maintained compliance since the restructuring.", file: "aula12_speech_compliance.mp3", voice: ELLEN },
  { text: "Our tax liability has decreased since last year.", file: "aula12_speech_liability.mp3", voice: ELLEN },
  { text: "We have diversified our revenue streams since the acquisition.", file: "aula12_speech_revenue_streams.mp3", voice: ELLEN },
  { text: "The audit team has been reviewing our records for three months.", file: "aula12_speech_audit_team.mp3", voice: ELLEN },

  // ===== Listening 1 (MC with accountant = Ellen) =====
  { text: "Good morning. Thank you for meeting with me today. I would like to review the fiscal year results. We have filed our tax return for this fiscal year, and I am pleased to report that everything is in order. The company has maintained full compliance with all tax regulations since the restructuring in 2022. We have claimed several deductions this year, including business travel, equipment purchases, and the new office renovation. Our tax liability has decreased by eight percent since last year. This is mainly because we have diversified our revenue streams since the acquisition of the Texas subsidiary. The audit team has been reviewing our records for the past three months, and they have not found any issues. I have also recommended a write-off for the old logistics equipment. For the past two quarters, revenue has exceeded our projections. Overall, the holding is in excellent financial health.", file: "aula12_ic_listening1_mc_accountant.mp3", voice: ELLEN },

  // ===== Listening 2 (David = Arthur) =====
  { text: "Thank you, Maria Claudia. Let me share the Pittsburgh fiscal update. We have completed our tax filing for this fiscal year as well. Our compliance record has been clean since 2020. We have claimed deductions for the new manufacturing equipment we purchased in Q2. Our tax liability is slightly higher than last year because revenue has grown significantly. We have been working with a new accounting firm since September, and they have already identified two additional deduction opportunities. The audit in Pittsburgh has been completed. It took four months, but the results are positive. We have maintained all required documentation since the last audit in 2023. For the past year, our revenue stream from the logistics division has been our strongest performer.", file: "aula12_ic_listening2_david_fiscal.mp3", voice: ARTHUR },

  // ===== Dialogue =====
  { text: "Good morning. We have filed the tax return for this fiscal year. Everything is in order.", file: "aula12_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "That is good news. How long has the audit been in progress?", file: "aula12_ic_dlg_accountant_1.mp3", voice: ARTHUR },
  { text: "The audit team has been reviewing our records for three months. They have not found any issues.", file: "aula12_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "Excellent. Have you claimed all eligible deductions?", file: "aula12_ic_dlg_accountant_2.mp3", voice: ARTHUR },
  { text: "Yes. We have claimed deductions for business travel, equipment, and the office renovation.", file: "aula12_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "Good. Your tax liability has decreased since the restructuring. That is a positive trend.", file: "aula12_ic_dlg_accountant_3.mp3", voice: ARTHUR },
  { text: "We have also diversified our revenue streams since the acquisition. That has helped.", file: "aula12_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "I would recommend a write-off for the old logistics equipment. It has been inactive for two years.", file: "aula12_ic_dlg_accountant_4.mp3", voice: ARTHUR },
  { text: "That makes sense. We have been considering that since last quarter. Let us proceed.", file: "aula12_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "I will prepare the documentation. The holding has maintained excellent compliance for five years. Well done.", file: "aula12_ic_dlg_accountant_5.mp3", voice: ARTHUR },

  // ===== Error correction =====
  { text: "We have worked here since three years.", file: "aula12_ic_error_since_three.mp3", voice: ARTHUR },
  { text: "I have been here for January.", file: "aula12_ic_error_for_january.mp3", voice: ELLEN },
  { text: "The audit has started since last month.", file: "aula12_ic_error_has_started_since.mp3", voice: ARTHUR },
  { text: "We have maintain compliance for five years.", file: "aula12_ic_error_have_maintain.mp3", voice: ELLEN },
  { text: "She has filed the return since the fiscal year.", file: "aula12_ic_error_since_fiscal.mp3", voice: ARTHUR },
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
  console.log('Generating ' + unique.length + ' AULA 12 audio files...');
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
