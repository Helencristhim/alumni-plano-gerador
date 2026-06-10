const fs = require('fs');
const path = require('path');

const API_KEY = process.env.ELEVENLABS_API_KEY;
const ARTHUR = 'sfJopaWaOtauCD3HKX6Q';
const ELLEN = 'BIvP0GN1cAtSRTxNHnWS';
const DIR = path.join(__dirname, '..', 'public', 'audio', 'maria-claudia-curimbaba');

const PHRASES = [
  // ===== Vocab (Ellen) =====
  { text: "Regarding", file: "aula8_regarding.mp3", voice: ELLEN },
  { text: "Acknowledge", file: "aula8_acknowledge.mp3", voice: ELLEN },
  { text: "Inquire", file: "aula8_inquire.mp3", voice: ELLEN },
  { text: "Attachment", file: "aula8_attachment.mp3", voice: ELLEN },
  { text: "Follow through", file: "aula8_follow_through.mp3", voice: ELLEN },
  { text: "Outline", file: "aula8_outline.mp3", voice: ELLEN },
  { text: "Notify", file: "aula8_notify.mp3", voice: ELLEN },
  { text: "Forward", file: "aula8_forward.mp3", voice: ELLEN },

  // ===== Vocab examples (alternate) =====
  { text: "I am writing regarding the Q3 financial report.", file: "aula8_i_am_writing_regarding.mp3", voice: ARTHUR },
  { text: "I would like to acknowledge receipt of your proposal.", file: "aula8_i_would_like_to_acknowledge.mp3", voice: ELLEN },
  { text: "I am writing to inquire about the delivery schedule.", file: "aula8_i_am_writing_to_inquire.mp3", voice: ARTHUR },
  { text: "Please find the contract attached for your review.", file: "aula8_please_find_the_contract.mp3", voice: ELLEN },
  { text: "We will follow through on the action items from the meeting.", file: "aula8_we_will_follow_through.mp3", voice: ARTHUR },
  { text: "I would like to outline the key changes to the contract.", file: "aula8_i_would_like_to_outline.mp3", voice: ELLEN },
  { text: "I wanted to notify you that the shipment has been delayed.", file: "aula8_i_wanted_to_notify.mp3", voice: ARTHUR },
  { text: "I have forwarded your email to the procurement team.", file: "aula8_i_have_forwarded.mp3", voice: ELLEN },

  // ===== Expressions (alternate) =====
  { text: "I am writing to...", file: "aula8_expr_i_am_writing_to.mp3", voice: ARTHUR },
  { text: "I am writing to follow up on our meeting last Thursday.", file: "aula8_expr_writing_example.mp3", voice: ELLEN },
  { text: "Please find attached...", file: "aula8_expr_please_find.mp3", voice: ARTHUR },
  { text: "Please find attached the revised contract for your approval.", file: "aula8_expr_find_example.mp3", voice: ELLEN },
  { text: "I look forward to...", file: "aula8_expr_i_look_forward.mp3", voice: ARTHUR },
  { text: "I look forward to hearing from you at your earliest convenience.", file: "aula8_expr_forward_example.mp3", voice: ELLEN },

  // ===== Grammar context passage (Ellen) =====
  { text: "Maria Claudia is writing an email to her Houston counterpart regarding the new logistics contract. Dear David, I am writing to follow up on our meeting last Thursday. Please find attached the revised contract with the agreed terms. I would like to outline three key changes: the discount has been increased to ten percent, the delivery clause has been updated, and the payment terms are now net 30. I wanted to notify you that the legal team has reviewed and approved the document. Could you please acknowledge receipt and forward it to your procurement team? I look forward to hearing from you at your earliest convenience. Best regards, Maria Claudia.", file: "aula8_grammar_context_passage.mp3", voice: ELLEN },

  // ===== Fill-in (alternate) =====
  { text: "I am writing regarding the Q3 financial report.", file: "aula8_fill_regarding.mp3", voice: ARTHUR },
  { text: "I would like to acknowledge receipt of your proposal.", file: "aula8_fill_acknowledge.mp3", voice: ELLEN },
  { text: "I am writing to inquire about the delivery schedule.", file: "aula8_fill_inquire.mp3", voice: ARTHUR },
  { text: "Please find the contract attached for your review.", file: "aula8_fill_attached.mp3", voice: ELLEN },
  { text: "We will follow through on the action items from the meeting.", file: "aula8_fill_follow_through.mp3", voice: ARTHUR },
  { text: "I would like to outline the key changes to the contract.", file: "aula8_fill_outline.mp3", voice: ELLEN },
  { text: "I wanted to notify you that the shipment has been delayed.", file: "aula8_fill_notify.mp3", voice: ARTHUR },
  { text: "I have forwarded your email to the procurement team.", file: "aula8_fill_forwarded.mp3", voice: ELLEN },

  // ===== Ordering =====
  { text: "Dear Mr. Chen, I am writing regarding the revised logistics contract. Please find attached the updated document for your review. I would like to outline three key changes to the terms. Could you please acknowledge receipt and forward it to your team? I look forward to hearing from you. Best regards, Maria Claudia.", file: "aula8_order_email_sequence.mp3", voice: ELLEN },

  // ===== Survival (Ellen) =====
  { text: "I am writing regarding the revised contract.", file: "aula8_surv_writing_regarding.mp3", voice: ELLEN },
  { text: "Please find attached the updated document.", file: "aula8_surv_find_attached.mp3", voice: ELLEN },
  { text: "I would like to acknowledge receipt of your email.", file: "aula8_surv_acknowledge_receipt.mp3", voice: ELLEN },
  { text: "Could you please forward this to the team?", file: "aula8_surv_forward_team.mp3", voice: ELLEN },
  { text: "I look forward to hearing from you.", file: "aula8_surv_look_forward.mp3", voice: ELLEN },

  // ===== Speech (Ellen) =====
  { text: "I am writing to follow up on our meeting last Thursday.", file: "aula8_speech_follow_up.mp3", voice: ELLEN },
  { text: "Please find attached the revised contract for your approval.", file: "aula8_speech_find_attached.mp3", voice: ELLEN },
  { text: "I would like to outline the key changes to the terms.", file: "aula8_speech_outline_changes.mp3", voice: ELLEN },
  { text: "Could you please acknowledge receipt of this document?", file: "aula8_speech_acknowledge.mp3", voice: ELLEN },
  { text: "I look forward to hearing from you at your earliest convenience.", file: "aula8_speech_look_forward.mp3", voice: ELLEN },

  // ===== Listening 1 (MC reading email = Ellen) =====
  { text: "Dear David, I am writing to follow up on our quarterly review meeting last Thursday. First, I would like to acknowledge receipt of the Pittsburgh revenue report you sent on Friday. Thank you for the detailed analysis. Please find attached the revised logistics contract with the updated terms we discussed. I would like to outline the three key changes. First, the discount has been increased from seven to ten percent. Second, the delivery clause now includes a penalty for delays beyond five business days. Third, the payment terms have been extended to net 30. I wanted to notify you that our legal team has reviewed and approved the document. Could you please forward it to your procurement team for final signature? I look forward to hearing from you at your earliest convenience. Best regards, Maria Claudia Curimbaba.", file: "aula8_ic_listening1_mc_email.mp3", voice: ELLEN },

  // ===== Listening 2 (David = Arthur) =====
  { text: "When I write professional emails, I follow a simple structure. First, I always start with a clear subject line. Something like: Revised Contract for Review. Then I use a formal greeting: Dear Maria Claudia. In the opening line, I state the purpose immediately. I am writing regarding the logistics contract. I never use informal language like Hey or Just checking in. I outline the key points using numbered lists so they are easy to follow. If I am attaching a file, I always say: Please find attached. Before I close, I include a clear call to action. Could you please acknowledge receipt? And I end with: I look forward to hearing from you. Best regards, David Chen. The whole email should be clear, professional, and action-oriented.", file: "aula8_ic_listening2_david_tips.mp3", voice: ARTHUR },

  // ===== Dialogue =====
  { text: "David, I just sent you an email regarding the revised contract. Did you receive it?", file: "aula8_ic_dlg_mc_1.mp3", voice: ELLEN },
  { text: "Yes, I would like to acknowledge receipt. I saw the attachment. Let me review the changes.", file: "aula8_ic_dlg_david_1.mp3", voice: ARTHUR },
  { text: "I outlined three key changes in the email. Did you see the updated delivery clause?", file: "aula8_ic_dlg_mc_2.mp3", voice: ELLEN },
  { text: "Yes, the penalty clause for late delivery is clear. I will forward the contract to our procurement team today.", file: "aula8_ic_dlg_david_2.mp3", voice: ARTHUR },
  { text: "Thank you. Could you also notify Sarah about the new payment terms?", file: "aula8_ic_dlg_mc_3.mp3", voice: ELLEN },
  { text: "Of course. I will follow through on that. She needs to update the accounting system.", file: "aula8_ic_dlg_david_3.mp3", voice: ARTHUR },
  { text: "I am also writing to inquire about the Houston shipping schedule. Do you have an update?", file: "aula8_ic_dlg_mc_4.mp3", voice: ELLEN },
  { text: "I will check with the logistics team and send you an email regarding the timeline by end of day.", file: "aula8_ic_dlg_david_4.mp3", voice: ARTHUR },
  { text: "Perfect. I look forward to hearing from you. Please find attached the shipping requirements document as well.", file: "aula8_ic_dlg_mc_5.mp3", voice: ELLEN },
  { text: "Got it. I will review both documents and reply formally. Best regards, as they say.", file: "aula8_ic_dlg_david_5.mp3", voice: ARTHUR },

  // ===== Error correction =====
  { text: "Hey David, I want to ask about the contract.", file: "aula8_ic_error_hey_david.mp3", voice: ARTHUR },
  { text: "Here is the file you asked for.", file: "aula8_ic_error_here_is.mp3", voice: ELLEN },
  { text: "Just checking in about the meeting.", file: "aula8_ic_error_just_checking.mp3", voice: ARTHUR },
  { text: "Let me know if you got this.", file: "aula8_ic_error_let_me_know.mp3", voice: ELLEN },
  { text: "Thanks, talk soon.", file: "aula8_ic_error_thanks_talk.mp3", voice: ARTHUR },
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
  console.log('Generating ' + unique.length + ' AULA 8 audio files...');
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
